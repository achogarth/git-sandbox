#!/usr/bin/env python
def hello(s):
    print ("Hello", s)

def hellocall():
    print("Hello from module")

if __name__ == "__main__":
    print("Hello Main")
    hello("World")
    hellocall()