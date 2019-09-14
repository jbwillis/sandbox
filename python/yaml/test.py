#! /usr/bin/env python3

import yaml

# create a dictionary to load
print("Test dictionary")
test_dict = {"Matthew": 5, "Mark": 17, "Luke": 33.33, "John": 123}
print(test_dict)

print("Dumping test dictionary")
print(yaml.dump(test_dict))
with open('test_dump1.yaml', 'w') as f:
    yaml.dump(test_dict, f)

print("testing numpy objects")
import numpy as np
a = np.zeros([13,1])
b = np.array([1,2,3,4,5,6])
c = {"a": a.tolist(), "b": b.tolist(), "e": np.e, "pi": np.pi}
print("dict of np arrays:")
print(c)
print("dumped")
print(yaml.dump(c))
with open('test_dump2.yaml', 'w') as f:
    yaml.dump_all(test_dict, f)
    yaml.dump_all(c, f)


