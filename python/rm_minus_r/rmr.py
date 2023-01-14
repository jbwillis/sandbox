import os

DIRECTORY_STAT = 16384  # the stat value for a directory


def is_dir(path):
    """returns True if item at `path` is a directory, otherwise returns False"""
    stat = os.stat(path)
    if stat[0] == DIRECTORY_STAT:
        return True
    else:
        return False


def joinpath(path1, path2):
    """join path1 and path2 with the os specific separator"""
    return f"{path1}{os.sep}{path2}"


def rmrecursive(path, verbose=False):
    """
    Simple rm -r implementation.
    Recursively deletes everything at path and below
    """
    if is_dir(path):
        for item in os.listdir(path):
            item_path = joinpath(path, item)
            rmrecursive(item_path, verbose=verbose)
        os.rmdir(path)
    else:
        os.remove(path)

    if verbose:
        print(f"Removed {path}")
