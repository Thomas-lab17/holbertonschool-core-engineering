#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)

if number < 0:
    digit = -(-number % 10)
if number > 0:
    digit = number % 10
    
if digit > 5:
    print("Last digit of ",number ,"is", digit ," and is greater than 5")
    
if digit == 0:
    print("Last digit of ",number ,"is", digit ," and is 0")

if digit < 6 and digit != 0:
    print("Last digit of",number ,"is", digit ,"and is less than 6 and not 0")
