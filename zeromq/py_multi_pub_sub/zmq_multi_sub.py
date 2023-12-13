"""
Multipart, multicast publish-subscribe demonstration, taken from
https://zguide.zeromq.org/docs/chapter2/#Pub-Sub-Message-Envelopes

Communicates with `zmq_multi_pub.py`
"""

import time
import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        socket.setsockopt_string(zmq.SUBSCRIBE, arg) # each argument defines a filter value
else:
    socket.setsockopt_string(zmq.SUBSCRIBE, "") # subscribe to all

while True:
    msg = socket.recv_multipart()
    print(f"{msg[0]}: {msg[1]}")
    time.sleep(len(sys.argv)-1)