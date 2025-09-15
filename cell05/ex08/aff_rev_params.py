#!/usr/bin/env python3
import sys

if len(sys.argv) <= 2:
    print("none")
else:
    print("\n".join(reversed(sys.argv[1:])))