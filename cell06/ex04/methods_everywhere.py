#!/usr/bin/env python3
import sys

def shrink(s: str) -> str:
     print(s[:8])

def enlarge(s: str) -> str:
    while len(s) < 8:
        s+= 'Z'
    print(s)

if len(sys.argv) == 1:
    print("none")
else:
    for word in sys.argv[1:]:
        if len(word) > 8:
            shrink(word)
        else:
            enlarge(word)