#!/usr/bin/env python3

def admin_login(username, password):
    if username == "ADMIN" or  username == "admin" and password == "12345":
        return ("Access granted")
    else:
        return ("Access denied")

admin_login("sudo", "12345")
admin_login("admin", "12345")
admin_login("ADMIN", "12345")

def hows_the_weather(temp):
    if temp <= 40:
        return("It's brisk out there!")
    elif 40 < temp <= 65:
        return("It's a little chilly out there!")
    elif 65 < temp <= 85:
        return("It's perfect out there!")
    elif temp > 85:
        return("It's too dang hot out there!")

hows_the_weather(33)
hows_the_weather(99)
hows_the_weather(75)

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return("FizzBuzz")
    elif number % 3 == 0:
        return ("Fizz")
    elif number % 5 == 0:
        return("Buzz")
    else: 
         return (number)

fizzbuzz(1)
fizzbuzz(2)
fizzbuzz(3)
fizzbuzz(4)
fizzbuzz(5)
fizzbuzz(15)


def calculator(operator, num1, num2):
    if operator == "+":
        return (num1+num2)
    elif operator == "-":
        return (num1-num2)
    elif operator == "*":
        return (num1*num2)
    elif operator == "/":
        return (num1/num2)
    else:
        print("Invalid operation!")
        return None

calculator("+", 1, 1)
calculator("-", 3, 1)
calculator("*", 3, 2)
calculator("/", 4, 2)
calculator("nope", 4, 2)
