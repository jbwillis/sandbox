"""
Simple server demonstration, taken from
https://zeromq.org/languages/python/

Communicates with `zmq_simple_client.py`
"""

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    # process
    time.sleep(1)

    # reply
    socket.send(b"World")
