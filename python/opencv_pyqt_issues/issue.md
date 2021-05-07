Well, I've found a solution, if I install PyQt5==5.14.1 instead of PyQt5==5.15.2 I don't get the problem I'm seeing here. Here's the full description if you're interested in recreating this. (I'd be interested if someone could try it).

I'm using Python 3.8.5 on Ubuntu 20.04

* Create a fresh virtual environment
```
mkvirtualenv cvqt_test
```

* Install latest versions of necessary packages
```
pip install numpy pyqtgraph PyQt5 opencv-contrib-python
```

* The versions of these are
```
numpy==1.20.1
pyqtgraph==0.11.1
PyQt5==5.15.2
opencv-contrib-python==4.5.1.48
```

* Run test program
```
import cv2
import numpy as np
import pyqtgraph as pg

img = np.random.random((100, 100, 3))
cv2.imshow("Test", img)
cv2.waitKey(10)

pg.image(img)
cv2.waitKey(1000)
```

* Fails with error message:
```
QObject::moveToThread: Current thread (0x1150a70) is not the object's thread (0xedd4d0).
Cannot move to target thread (0x1150a70)

qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/home/jbwillis/.virtualenvs/cvqt_test/lib/python3.8/site-packages/cv2/qt/plugins" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb, eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl.
```

* Install earlier version of PyQt5
```
pip install PyQt5==5.14.1
```

* Run test progam: Runs without issue, displaying both an OpenCV image and a pyqtgraph image for 1 second





