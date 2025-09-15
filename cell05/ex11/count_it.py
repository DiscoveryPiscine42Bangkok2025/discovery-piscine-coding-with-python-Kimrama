#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print("none")
else:
    print("parameter:", len(sys.argv) - 1)
    for i in sys.argv[1:]:
        print(f"{i}: {len(i)}")