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

# need to set socket options before connecting
if len(sys.argv) > 1:
    socket.setsockopt(zmq.CONFLATE, 1)
    for arg in sys.argv[1:]:
        socket.setsockopt_string(zmq.SUBSCRIBE, arg) # each argument defines a filter value
else:
    socket.setsockopt_string(zmq.SUBSCRIBE, "") # subscribe to all

# can use localhost here (DNS name), can't use '*'
socket.connect("tcp://localhost:5556")

while True:
    msg = socket.recv()
    print(msg)
    time.sleep(len(sys.argv)-1)