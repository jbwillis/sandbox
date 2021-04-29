try:
    import asgdf
except ImportError:
    print("Import Error on asgdf")

try:
    import numpy
    print("No import error on numpy")
except ImportError:
    print("Import Error on numpy")
