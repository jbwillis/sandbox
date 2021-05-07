#! /usr/bin/env python3

# works with PyQt5==5.14.1, fails with PyQt5==5.15.2

import cv2
import numpy as np
import pyqtgraph as pg

img = np.random.random((100, 100, 3))
cv2.imshow("Test", img)
cv2.waitKey(10)

pg.image(img)
cv2.waitKey(1000)
