#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
else:
    print("parameter:", len(sys.argv) - 1)
    for i in sys.argv[1:]:
        if i.strip() == "":
            print(f'"{i}": empty or only spaces')
        else:
            print(f"{i}: {len(i)}")
