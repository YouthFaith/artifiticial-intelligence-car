import RPi.GPIO as GPIO
import time
import socket
from threading import Thread
import inspect
import ctypes
import cv2
import zlib
import numpy as np

LEFT_FORWARD = [19, 26]
RIGHT_FORWARD = [6, 13]
LEFT_BACK = [16, 12]
RIGHT_BACK = [20, 21]

HOLDER = 5
ULTRASONIC = [23, 24]

SPEED_LIST = [20, 40, 60, 80, 100]

OUTSIDE_LEFT = 22
INSIDE_LEFT = 27
INSIDE_RIGHT = 17
OUTSIDE_RIGHT = 4

CURRENT_SPEED = 20

SERVER_ADDRESS = ("10.42.0.43", 8888)

def _async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

class Holder:
    def __init__(self):
        GPIO.setup(HOLDER, GPIO.OUT)
        GPIO.output(HOLDER, GPIO.LOW)
        self.pwm = GPIO.PWM(HOLDER, 50)
        self.pwm.start(90)
        time.sleep(0.5)
        self.pwm.ChangeDutyCycle(2.5 + 90 / 18)
        self.current_angel = 90
        self.thread = Thread(target=self.change_status)
        self.thread.start()

    def change_status(self):
        now_angel = 0
        while 1:
            if now_angel != self.current_angel:
                now_angel = self.current_angel
                self.pwm.ChangeDutyCycle(2.5 + self.current_angel / 18)
                time.sleep(0.5)

    def __del__(self):
        self.pwm.stop()
        del self.pwm
        del self.current_angel
        stop_thread(self.thread)
        del self.thread

    def turn(self, value):
        if self.current_angel < 30:
            self.current_angel = 30
            return
        elif self.current_angel > 150:
            self.current_angel = 150
            return
        else:
            self.current_angel += value

class Ultrasonic:
    def __init__(self, socket=None, wheels=None):
        GPIO.setup(ULTRASONIC[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(ULTRASONIC[1], GPIO.IN)
        self.socket = None
        self.distance = socket
        self.wheels = wheels
        self.instance = None

    def start(self):
        self.instance = Thread(target=self.read_dist)
        self.instance.start()

    def set_socket(self, socket):
        self.socket = socket

    def __del__(self):
        stop_thread(self.instance)
        del self.distance
        del self.instance

    def get_instance(self):
        return self.distance

    def read_dist(self):
        while 1:
            time.sleep(0.5)
            GPIO.output(ULTRASONIC[0], GPIO.HIGH)
            time.sleep(0.003)
            GPIO.output(ULTRASONIC[0], GPIO.LOW)
            while GPIO.input(ULTRASONIC[1]) == 0:
                pass
            t1 = time.time()
            while GPIO.input(ULTRASONIC[1]) == 1:
                pass
            t2 = time.time()
            self.distance = (t2 - t1) * 340 / 2 * 100
            if self.distance <= 20:
                self.wheels.stop()
            if self.socket is None:
                pass
            else:
                try:
                    self.socket.send(b'DISTANCE' + b'\n' + str(self.distance).encode('utf-8') + b'\n')
                except:
                    pass

class Tracing:
    def __init__(self, distance=None, wheels=None):
        GPIO.setup(OUTSIDE_LEFT, GPIO.IN)
        GPIO.setup(INSIDE_LEFT, GPIO.IN)
        GPIO.setup(INSIDE_RIGHT, GPIO.IN)
        GPIO.setup(OUTSIDE_RIGHT, GPIO.IN)
        self.wheels = wheels
        self.distance = distance
        self.thread = None

    def start(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        self.wheels.set_forward_or_back("FORWARD")
        while 1:
            time.sleep(0.1)
            if self.distance.get_instance() < 20:
                continue
            status = [GPIO.input(OUTSIDE_LEFT), GPIO.input(INSIDE_LEFT), GPIO.input(INSIDE_RIGHT), GPIO.input(OUTSIDE_RIGHT)]
            if status[0] == 1 and status[1] == 0 and status[2] == 0 and status[3] == 1:
                self.wheels.set_forward_or_back("FORWARD")
                self.wheels.set_left_or_right("NONE")
                self.wheels.change_status()
            elif status[0] == 1 and status[1] == 1 and status[2] == 0 and status[3] == 1:
                self.wheels.set_forward_or_back("FORWARD")
                self.wheels.set_left_or_right("RIGHT")
                self.wheels.change_status()8 
            elif status[0] == 1 and status[1] == 0 and status[2] == 1 and status[3] == 1:
                self.wheels.set_forward_or_back("FORWARD")
                self.wheels.set_left_or_right("LEFT")
                self.wheels.change_status()
            elif status[0] == 0 and status[1] == 0:
                self.wheels.set_forward_or_back("NONE")
                self.wheels.set_left_or_right("LEFT")
                self.wheels.change_status()
            elif status[1] == 0 and status[2] == 0:
                self.wheels.set_forward_or_back("NONE")
                self.wheels.set_left_or_right("RIGHT")
                self.wheels.change_status()

    def stop(self):
        if self.thread is not None:
            self.wheels.set_left_or_right("NONE")
            self.wheels.set_forward_or_back("NONE")
            self.wheels.change_status()
            stop_thread(self.thread)

class Wheel:
    def __init__(self, pin_left, pin_right):
        GPIO.setup(pin_left, GPIO.OUT)
        GPIO.setup(pin_right, GPIO.OUT)
        self.pwm_left = GPIO.PWM(pin_left, 50)
        self.pwm_right = GPIO.PWM(pin_right, 50)
        self.pwm_left.start(0)
        self.pwm_right.start(0)

    def __del__(self):
        self.pwm_left.stop()
        self.pwm_right.stop()
        del self.pwm_right
        del self.pwm_left

    def change_speed_forward(self, speed):
        self.pwm_left.ChangeDutyCycle(speed)
        self.pwm_right.ChangeDutyCycle(0)

    def change_speed_back(self, speed):
        self.pwm_left.ChangeDutyCycle(0)
        self.pwm_right.ChangeDutyCycle(speed)

class Wheels:
    def __init__(self):
        self.left_back = Wheel(LEFT_BACK[0], LEFT_BACK[1])
        self.left_forward = Wheel(LEFT_FORWARD[0], LEFT_FORWARD[1])
        self.right_back = Wheel(RIGHT_BACK[0], RIGHT_BACK[1])
        self.right_forward = Wheel(RIGHT_FORWARD[0], RIGHT_FORWARD[1])
        self.forward_or_back = None
        self.left_or_right = None

    def __del__(self):
        del self.left_back
        del self.left_forward
        del self.right_back
        del self.right_forward
        del self.forward_or_back
        del self.left_or_right

    def stop(self):
        self.left_forward.change_speed_forward(0)
        self.right_forward.change_speed_forward(0)
        self.right_back.change_speed_forward(0)
        self.left_back.change_speed_forward(0)

    def set_forward_or_back(self, string):
        if string == "NONE":
            self.forward_or_back = None
        else:
            self.forward_or_back = string

    def set_left_or_right(self, string):
        if string == "NONE":
            self.left_or_right = None
        else:
            self.left_or_right = string

    def change_status(self):
        if self.forward_or_back is None:
            if self.left_or_right is None:
                self.left_back.change_speed_forward(0)
                self.left_forward.change_speed_forward(0)
                self.right_back.change_speed_forward(0)
                self.right_forward.change_speed_forward(0)
            elif self.left_or_right == "LEFT":
                self.left_forward.change_speed_back(CURRENT_SPEED - 10)
                self.left_back.change_speed_back(CURRENT_SPEED - 10)
                self.right_forward.change_speed_forward(CURRENT_SPEED + 10)
                self.right_back.change_speed_forward(CURRENT_SPEED + 10)
            elif self.left_or_right == "RIGHT":
                self.right_forward.change_speed_back(CURRENT_SPEED - 10)
                self.right_back.change_speed_back(CURRENT_SPEED - 10)
                self.left_forward.change_speed_forward(CURRENT_SPEED - 10)
                self.left_back.change_speed_forward(CURRENT_SPEED - 10)
        elif self.forward_or_back == "FORWARD":
            if self.left_or_right is None:
                self.left_forward.change_speed_forward(CURRENT_SPEED)
                self.left_back.change_speed_forward(CURRENT_SPEED)
                self.right_back.change_speed_forward(CURRENT_SPEED)
                self.right_forward.change_speed_forward(CURRENT_SPEED)
            elif self.left_or_right == "LEFT":
                self.left_back.change_speed_forward(CURRENT_SPEED - 10)
                self.left_forward.change_speed_forward(CURRENT_SPEED - 10)
                self.right_forward.change_speed_forward(CURRENT_SPEED + 10)
                self.right_back.change_speed_forward(CURRENT_SPEED + 10)
            elif self.left_or_right == "RIGHT":
                self.left_forward.change_speed_forward(CURRENT_SPEED + 10)
                self.left_back.change_speed_forward(CURRENT_SPEED + 10)
                self.right_back.change_speed_forward(CURRENT_SPEED - 10)
                self.right_forward.change_speed_forward(CURRENT_SPEED - 10)
        elif self.forward_or_back == "BACK":
            if self.left_or_right is None:
                self.left_forward.change_speed_back(CURRENT_SPEED)
                self.left_back.change_speed_back(CURRENT_SPEED)
                self.right_back.change_speed_back(CURRENT_SPEED)
                self.right_forward.change_speed_back(CURRENT_SPEED)
            elif self.left_or_right == "LEFT":
                self.left_back.change_speed_back(CURRENT_SPEED - 10)
                self.left_forward.change_speed_back(CURRENT_SPEED - 10)
                self.right_forward.change_speed_back(CURRENT_SPEED + 10)
                self.right_back.change_speed_back(CURRENT_SPEED + 10)
            elif self.left_or_right == "RIGHT":
                self.left_forward.change_speed_back(CURRENT_SPEED + 10)
                self.left_back.change_speed_back(CURRENT_SPEED + 10)
                self.right_back.change_speed_back(CURRENT_SPEED - 10)
                self.right_forward.change_speed_back(CURRENT_SPEED - 10)

class Car:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = "manual_driver"
        self.client_socket_thread = None
        self.video_socket_thread = None
        self.client_socket = None
        self.init_pin()
        self.wheels = Wheels()
        self.holder = Holder()
        self.ultrasonic = Ultrasonic(wheels=self.wheels)
        self.tracing = Tracing(distance=self.ultrasonic, wheels=self.wheels)
        self.init_server()
        self.init_video()
        self.init_modules()

    def __del__(self):
        del self.wheels
        del self.ultrasonic
        del self.client_socket
        del self.holder
        stop_thread(self.client_socket_thread)
        stop_thread(self.video_socket_thread)
        GPIO.cleanup()

    def init_modules(self):
        self.ultrasonic.start()

    def init_video(self):
        self.video_socket_thread = Thread(target=self.send_video)
        self.video_socket_thread.start()

    def send_video(self):
        while 1:
            if self.client_socket is None:
                pass
            else:
                video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                cap = cv2.VideoCapture(0)
                while cap.isOpened():
                    _, frame = cap.read()
                    frame = cv2.flip(frame, 0)
                    size = min([int(i / 2) for i in frame.shape[0:2]])
                    sframe = cv2.resize(frame, (size, size))
                    enfra = cv2.imencode('.jpg', sframe)[1]
                    data = zlib.compress(enfra, zlib.Z_BEST_COMPRESSION)
                    data_encode = np.array(data)
                    str_encode = data_encode.tostring()
                    try:
                        video_socket.sendto(str_encode, (self.client_socket[1][0], 8889))
                        cv2.waitKey(1)
                    except:
                        cap.release()
                        break
                video_socket.close()

    @staticmethod
    def init_pin():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def init_server(self):
        self.socket.bind(SERVER_ADDRESS)
        self.socket.listen(1)
        self.client_socket_thread = Thread(target=self.accept_client)
        self.client_socket_thread.start()

    def accept_client(self):
        while 1:
            self.client_socket = self.socket.accept()
            self.ultrasonic.set_socket(self.client_socket[0])
            print("{} connected!".format(self.client_socket[1][0]))
            try:
                while 1:
                    data = self.client_socket[0].recv(1024)
                    if data == b"":
                        print("{} disconnected!".format(self.client_socket[1][0]))
                        self.wheels.stop()
                        self.client_socket[0].close()
                        self.client_socket = None
                        break
                    else:
                        self.handle_data(data.decode('utf-8'))
            finally:
                print("No client is connected!")

    def handle_data(self, data):
        data_list = data.split('\n')
        if data_list[0][:5] == "LEVEL":
            global CURRENT_SPEED
            CURRENT_SPEED = SPEED_LIST[int(data_list[0][-1])]
        elif data_list[0] == "MANUAL_DRIVER":
            self.status = "manual_driver"
            self.tracing.stop()
        elif data_list[0] == "AUTOMATIC_TRACING":
            self.status = "automatic_tracing"
            self.tracing.start()
        else:
            if self.ultrasonic.get_instance() < 20:
                if data_list[0] == "BACK":
                    self.wheels.set_forward_or_back(data_list[0])
                    self.wheels.change_status()
            else:
                if self.status == "manual_driver":
                    if data_list[0] == "FORWARD":
                        self.wheels.set_forward_or_back(data_list[0])
                    elif data_list[0] == "BACK":
                        self.wheels.set_forward_or_back(data_list[0])
                    elif data_list[0] == "NONE_FB":
                        self.wheels.set_forward_or_back("NONE")
                    elif data_list[0] == "LEFT":
                        self.wheels.set_left_or_right(data_list[0])
                    elif data_list[0] == "RIGHT":
                        self.wheels.set_left_or_right(data_list[0])
                    elif data_list[0] == "NONE_LR":
                        self.wheels.set_left_or_right("NONE")
                    elif data_list[0] == "TURN_LEFT_ON":
                        self.holder.turn(5)
                    elif data_list[0] == "TURN_RIGHT_ON":
                        self.holder.turn(-5)
                    else:
                        pass
                self.wheels.change_status()
                if len(data_list) != 2:
                    self.handle_data("".join(data_list[1:]))

if __name__ == "__main__":
    a = Car()
