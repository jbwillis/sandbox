"""
Multipart, multicast publish-subscribe demonstration, taken from
https://zguide.zeromq.org/docs/chapter2/#Pub-Sub-Message-Envelopes

Communicates with `zmq_multi_sub.py`
"""

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
# can't use localhost for the interface, must be '*' or an IP address
socket.bind(f"tcp://*:{5556}")

i = 0
while True:
    now = time.strftime("%d-%b-%Y %H:%M:%S")

    # to allow the subscriber to skip messages with the CONFLATE option, we can't use send_multipart
    socket.send(b"AA"+f"{i:20d}: Hello, it's {now}".encode('utf-8'))
    socket.send(b"BB"+f"{i:20d}: {now} is the time".encode('utf-8'))
    socket.send(b"BA"+f"{i:20d}: Not sure this is necessary".encode('utf-8'))
    i += 1
