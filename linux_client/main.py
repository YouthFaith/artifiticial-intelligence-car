# -*- coding: utf-8 -*-
import os
import cv2
import sys
import zlib
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtNetwork import QTcpSocket, QUdpSocket, QAbstractSocket, QHostAddress
from main_windows_ui import Ui_Main_Windows

class Control(QWidget, Ui_Main_Windows):
    def __init__(self, parent=None):
        super(Control, self).__init__(parent)
        self.setupUi(self)
        self.function = "manual_driver"
        self.ip = ""
        self.port = 0
        self.forward_or_back = None
        self.left_or_right = None
        self.holder = None
        self.car_socket = QTcpSocket(self)
        self.monitoring_socket = QUdpSocket(self)
        self.monitoring_socket.bind(QHostAddress("10.42.0.1"), 8889)
        self.connect_to_car()
        self.set_connect()

    def set_connect(self):
        for i in self.LEVELS:
            i.clicked.connect(self.on_level_change)
        for i in self.FUNCTIONS:
            i.clicked.connect(self.on_function_change)
        self.car_socket.readyRead.connect(self.on_handle_data)
        self.monitoring_socket.readyRead.connect(self.on_show_video)
        self.manual_driver.clicked.connect(self.on_manual_driver)
        self.automatic_tracing.clicked.connect(self.on_automatic_tracing)

    def on_manual_driver(self):
        if self.manual_driver.isChecked():
            if self.function == "automatic_tracing":
                self.function = "manual_driver"
                self.car_socket.write(b"MANUAL_DRIVER" + b'\n')
                self.car_socket.flush()

    def on_automatic_tracing(self):
        if self.automatic_tracing.isChecked():
            if self.function == "manual_driver":
                self.function = "automatic_tracing"
                self.car_socket.write(b"AUTOMATIC_TRACING" + b'\n')
                self.car_socket.flush()

    def on_show_video(self):
        data = self.monitoring_socket.readDatagram(65535)[0]
        data = zlib.decompress(data)
        video_show = QPixmap()
        video_show.loadFromData(data)
        self.video.setPixmap(video_show)

    def on_handle_data(self):
        data = str(self.car_socket.readAll(), encoding='utf-8')
        self.handle_data(data)

    def handle_data(self, data):
        data_list = data.split('\n')
        # print(data_list)
        if data_list[0] == "DISTANCE":
            distance_data = data_list[1].split('.')
            self.barrier_distance.setText(distance_data[0] + '.' + distance_data[1][:2] + 'cm')
        if len(data_list) != 3:
            self.handle_data("".join(data_list[2:]))

    def on_level_change(self):
        for i in self.LEVELS:
            if i.isChecked():
                index = self.LEVELS.index(i)
                self.current_speed.setText("LEVEL " + str(index + 1))
                self.car_socket.write(b'LEVEL ' + str(index).encode('utf-8') + b'\n')
                self.car_socket.flush()
                return

    def on_function_change(self):
        pass

    def connect_to_car(self):
        if os.path.exists("car.config"):
            with open("car.config") as f:
                self.ip = f.readline()[:-1]
                self.port = f.readline()[:]
                self.car_socket.connectToHost(self.ip, int(self.port))
                self.car_socket.connected.connect(self.on_show_connect)
                self.car_socket.error.connect(self.on_show_error)
        else:
            QMessageBox.critical("error", "no find config file!")
            exit(1)

    def on_show_connect(self):
        QMessageBox.critical(self, "connection", "succeed to connect to car!")

    def on_show_error(self, arg__1):
        QMessageBox.critical(self, "connection", "fail to connect to car!")
        # exit(1)

    def keyPressEvent(self, a0):
        if not a0.isAutoRepeat():
            if a0.key() == Qt.Key_W:
                if self.forward_or_back is None:
                    self.forward_or_back = "FORWARD"
                    data = "FORWARD"
                else:
                    return
            elif a0.key() == Qt.Key_S:
                if self.forward_or_back is None:
                    self.forward_or_back = "BACK"
                    data = "BACK"
                else:
                    return
            elif a0.key() == Qt.Key_A:
                if self.left_or_right is None:
                    self.left_or_right = "LEFT"
                    data = "LEFT"
                else:
                    return
            elif a0.key() == Qt.Key_D:
                if self.left_or_right is None:
                    self.left_or_right = "RIGHT"
                    data = "RIGHT"
                else:
                    return
            elif a0.key() == Qt.Key_Left:
                if self.holder is None:
                    self.holder = "TURN_LEFT_ON"
                    data = "TURN_LEFT_ON"
                else:
                    return
            elif a0.key() == Qt.Key_Right:
                if self.holder is None:
                    self.holder == "TURN_RIGHT_ON"
                    data = "TURN_RIGHT_ON"
                else:
                    return
            else:
                return
            self.car_socket.write(data.encode('utf-8') + b'\n')
            self.car_socket.flush()

    def keyReleaseEvent(self, a0):
        if not a0.isAutoRepeat():
            if a0.key() == Qt.Key_W:
                if self.forward_or_back == "FORWARD":
                    self.forward_or_back = None
                    data = "NONE_FB"
                else:
                    return
            elif a0.key() == Qt.Key_S:
                if self.forward_or_back == "BACK":
                    self.forward_or_back = None
                    data = "NONE_FB"
                else:
                    return
            elif a0.key() == Qt.Key_A:
                if self.left_or_right == "LEFT":
                    self.left_or_right = None
                    data = "NONE_LR"
                else:
                    return
            elif a0.key() == Qt.Key_D:
                if self.left_or_right == "RIGHT":
                    self.left_or_right = None
                    data = "NONE_LR"
                else:
                    return
            elif a0.key() == Qt.Key_Left:
                if self.holder == "TURN_LEFT_ON":
                    self.holder = None
                    return
                else:
                    return
            elif a0.key() == Qt.Key_Right:
                if self.holder == "TURN_RIGHT_ON":
                    self.holder = None
                    return
                else:
                    return
            else:
                return
            self.car_socket.write(data.encode('utf-8') + b'\n')
            self.car_socket.flush()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Control()
    a.show()
    sys.exit(app.exec_())
