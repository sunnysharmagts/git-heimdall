#!/usr/bin/env python

import sys

def the_function_to_call():
    print("Hello from python script")
    print("---This is next value---")
    #return "This is successful"
    sys.exit(0)

if __name__ == "__main__":
    the_function_to_call()
