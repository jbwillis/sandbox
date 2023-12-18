# attempt at putting both a publisher and a subscriber in a single thread

import time
import zmq

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:5556")

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.setsockopt(zmq.CONFLATE, 1)
subscriber.setsockopt_string(zmq.SUBSCRIBE, "Hello")  # subscribe to everything
subscriber.setsockopt_string(zmq.SUBSCRIBE, "Goodbye")  # subscribe to everything
subscriber.connect("tcp://localhost:5556")

while True:
    now = time.strftime("%d-%b-%Y %H:%M:%S")

    publisher.send_string(f"Hello, it's {now}")
    try:
        msg = subscriber.recv_string(flags=zmq.NOBLOCK)
        print(msg)
    except zmq.ZMQError as e:
        if str(e) == "Resource temporarily unavailable":
            # no message
            pass
        else:
            raise e
