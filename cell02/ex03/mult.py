#!/usr/bin/env python3

first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))
result = first * second
print(f"{first} * {second} = {result}")

if result == 0 :
    print("The result is positive and negative.")
if result > 0 :
    print("The result is positive.")
if result < 0 :
    print("The result is negative.")