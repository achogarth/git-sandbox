#!/usr/bin/env python
def hello(s):
    print ("Hello ", s)

def hellocall():
    print("Hello from module")

if __name__ == "__main__":
    import sys
    hello(sys.argv[1])