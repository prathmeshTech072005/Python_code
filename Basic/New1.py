
# import New   # Here we import file New.py ok you understand it my dear friend ok...!!
# # we can write above statement as 

# # import New as math   ok 

# result = New.sum(12,12)
# print(result)
# # -----------------------------------
# result1 = New.sub(12,10)
# print(result1)


# import New as math   # you can write this as well ok 

# result = math.sum(12,90)
# print(result)

# result = math.sub(12,12)
# print("Substation of two number is : ",result)

# # form New import sum 

# result = sum(12,12)
# print(result)

# import datetime   # It gives time date all this at present instance ok 

# current_time = datetime.datetime.now()
# print(current_time)


# Basic Arithmetic Functions:

# math.sqrt(x): Returns the square root of x.
# math.pow(x, y): Returns x raised to the power of y.
# math.exp(x): Returns the exponential of x.
# math.log(x): Returns the natural logarithm of x.
# math.log10(x): Returns the base-10 logarithm of x.

# Trigonometric Functions:

# math.sin(x): Returns the sine of x (in radians).
# math.cos(x): Returns the cosine of x (in radians).
# math.tan(x): Returns the tangent of x (in radians).
# math.asin(x): Returns the arcsine of x (in radians).
# math.acos(x): Returns the arccosine of x (in radians).
# math.atan(x): Returns the arctangent of x (in radians).

# Constants:

# math.pi: Represents the mathematical constant π (pi).
# math.e: Represents the mathematical constant e (Euler's number).

# Additional Functions:

# math.ceil(x): Rounds x to the smallest integer greater than or equal to x.
# math.floor(x): Rounds x to the largest integer less than or equal to x.
# math.factorial(x): Returns the factorial of x.
# math.gcd(a, b): Returns the greatest common divisor of a and b.


# import math
# a = 16
# square = math.sqrt(a)
# print(square)

# print(f"square root of {a} is : {square}")

# It gives value of pi ok 
# pi = math.pi
# print(f"The value pf pi is  : {pi}")

import random 

# random.random()
# random.randint()
# random.randrange()
# random.choice()


# # rand1 = random.random()   # It give random number from 0 to 1 in the term of floating point ok 
# # print(rand1)

# # r = random.randint(1,11)   # It gives random number 1 to 10 not add 11 in this range ok 
# # print(r)

# r = random.randrange(1,100)
# # print(r)

# print("your lover ",r,"%  love you ok ")

# # Random choise in python ok 

# # Ranodm choise in list create ok 

# l = ["Prathmeh","Sahil","Ganesh","Harshad"]  # random.choise()  gives random choise in this ok understand it very well ok 
# print(random.choice(l))


# list1 = [1,2,3,4,5,6,7,8,9,10]     # It gives random numbers form 1  to 10  ok 
# print(random.choice(list1))

# import random

# numbers = [1, 2, 3, 4, 5]
# print(random.shuffle(numbers))


# import math

# r = math.ceil(10.9)  # it gives bigger integer number ok 
# print(r)

# s = math.floor(10.45)  # It gives integer value ok 
# print(s)

# a = math.log(10) # It gives log value of number ok 
# print(a)

# z = math.exp(1)  # 
# print(z)

# c = math.sqrt(23)  # It gives square root of function ok 
# print(c)


# v = math.pow(2,4)  # It gives power of given number ok ....!!!!
# print(v)


# m = math.cbrt(2)   # 
# print(m)

# import datetime

# date1 = datetime.date(2023,9,22)  # Date showing 
# print(date1)

# time1 = datetime.time(9,32,12)  # Time showing
# print(time1)

# a = datetime.datetime.now()
# print(a)

import datetime

now = datetime.datetime.now()
print(now)
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
parsed_date = datetime.datetime.strptime("2023-09-01 14:30:00", "%Y-%m-%d %H:%M:%S")
print(parsed_date)

