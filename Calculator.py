
# Basic calculator in python 

# a = eval(input("Enter first value :"))
# b= eval(input("Enter second value :"))
# opr = input("Enter your opration   (+  , -  , X  , /)")
# if opr == "+":
#     print( " Sum of two number is  : " ,a+b)
# elif opr=="-":
#     print(" Substraction of two number is  : " ,a-b)
# elif opr =="X":
#     print(" Multiplication of two number is  : " ,a*b)
# elif opr =="/":
#     print(" Division of two number is  : " ,a/b)
# else:
#     print("Invalid operation ")    

# basic calculator in python 

a = eval(input("Enter first value :  "))
b = eval(input("Enter second value :  "))
opr = input("Seclect the oprator  + , - ,X , /   ::   " )

if opr == "+":
    add = a+b
    print("Addtion of two number is  : ", add)
elif opr == "-":
    sub = a-b
    print("Substraction of two numbers is : ", sub)
elif opr =="X":
    multi = a*b
    print("MUltiplication of two numbers  : " , multi )
elif opr == "/":
    div = a/b
    print("Division of two numbers : " , div )
elif opr == "%":
    module = a&b
    print("MOdule of two numbers is  : ",  module ) 
               
   
    
    
    
