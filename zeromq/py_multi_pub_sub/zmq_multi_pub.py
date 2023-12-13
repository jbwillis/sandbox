"""
Multipart, multicast publish-subscribe demonstration, taken from
https://zguide.zeromq.org/docs/chapter2/#Pub-Sub-Message-Envelopes

Communicates with `zmq_multi_sub.py`
"""

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

i = 0
while True:
    now = time.strftime("%d-%b-%Y %H:%M:%S")

    socket.send_multipart([b"AA", f"{i:20d}: Hello, it's {now}".encode('utf-8')])
    socket.send_multipart([b"BB", f"{i:20d}: {now} is the time".encode('utf-8')])
    socket.send_multipart([b"BA", f"{i:20d}: Not sure this is necessary".encode('utf-8')])
    i += 1
    # time.sleep(1)
