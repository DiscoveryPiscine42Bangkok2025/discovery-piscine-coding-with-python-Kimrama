#!/usr/bin/env python3
import sys
if len(sys.argv) == 1:
    print("none")
else:
    print("".join([c.lower() for c in sys.argv[1]]))