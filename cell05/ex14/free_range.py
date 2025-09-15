#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")

else:
    if sys.argv[1] == sys.argv[2]:   
        print("none")
    else:
        ls = [i for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1)]
        print(ls)