"""
Simple client demonstration, taken from
https://zeromq.org/languages/python/

Communicates with `zmq_simple_server.py`
"""

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
port = 5555
print(f"Connecting to server on port {port}")
socket.connect(f"tcp://localhost:{port}")

# Do 10 requests, waiting for a response each time
for request in range(10):
    print(f"Sending request {request} ...")
    socket.send(b"Hello")

    # get the reply
    message = socket.recv()
    print(f"[{request}] Received reply {message}")
