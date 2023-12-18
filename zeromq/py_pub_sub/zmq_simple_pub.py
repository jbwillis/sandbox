"""
Simple publish-subscribe demonstration, taken from
https://zguide.zeromq.org/docs/chapter1/

Communicates with `zmq_simple_sub.py`
"""

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
# can't use localhost for the interface, must be '*' or an IP address
socket.bind("tcp://*:5556")

while True:
    now = time.strftime("%d-%b-%Y %H:%M:%S")

    socket.send_string(f"Hello, it's {now}")
