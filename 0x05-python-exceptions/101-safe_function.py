#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as i:
        sys.stdrr.write("Exception: {}\n".format(i))
        result = None
    return (result)
