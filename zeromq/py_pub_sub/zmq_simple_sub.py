"""
Simple publish-subscribe demonstration, taken from
https://zguide.zeromq.org/docs/chapter1/

Communicates with `zmq_simple_pub.py`
"""

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")
socket.setsockopt_string(zmq.SUBSCRIBE, "")  # subscribe to everything

while True:
    msg = socket.recv_string()
    print(msg)
