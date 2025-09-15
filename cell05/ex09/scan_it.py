#!/usr/bin/env python3
import sys

if len(sys.argv) <= 2:
    print("none")

else:
    count = 0
    key = sys.argv[1]

    string_ls = sys.argv[2].split()
    for word in string_ls:
        if key in word:
            count += 1
    print(count if count > 0 else "none")
