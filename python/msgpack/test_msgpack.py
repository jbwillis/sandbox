import msgpack

b = msgpack.packb((123, "abc", 99.876))
u = msgpack.unpackb(b)
print(f"u = {u}")