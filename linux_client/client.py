# -*- coding: utf-8 -*-
import socket
import struct
import pickle
import zlib
import numpy as np
import cv2

test = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
test.bind(("127.0.0.1", 8889))
while 1:
    data, _ = test.recvfrom(65535)
    data = zlib.decompress(data)
    image = np.asarray(bytearray(data), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    cv2.imshow("test", image)
    cv2.waitKey(1)
