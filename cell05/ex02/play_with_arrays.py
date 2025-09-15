#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [i + 2 for i in original_array if i + 2 > 5]

print(original_array)
print(new_array)