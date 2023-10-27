# # Write a Python program that prints "Hello, World!" to the console
# print("Hello words ")

# # Create a program that adds, subtracts, multiplies, and divides two numbers entered by the user.
# a=12
# b= 13
# print( "Sum of two numbers is :-" ,a+b)

# a= eval(input("Enter first value  :- "))
# b = eval(input("Enter second value :-"))
# sum = a+b
# print("Sum of two numbers is :-",sum)

# # Write a program that checks if a given integer is even or odd.
# num = eval(input("Enter any number :-"))
# if  num%2==0:
#     print("Given number is even number ")
# else:
#     print("Odd number ")   
    
# length = eval(input("Enter length od rectangle :")) 
# breadth = eval(input("Enter breadth of rectangle :"))
# area = length * breadth
# print("Area of Recatangle having length is ",length ," and breadth is ",breadth , " then area is  : ",area )   
    
    
#  Develop a program that calculates the factorial of a given positive integer.    #    
# num1 = int(input("Enter any number :"))12





# Generate and display the multiplication table for a specified integer (e.g., the table for 7: 7x1, 7x2, ..., 7x10).

# a= int(input("Enter the number :"))

# for s in range(11):
#     print(a," X ",s," = " ,s*a)
   
#  Create a program that determines if a given year is a leap year or not.  

year = int(input("Enter any year :"))
if year%100!=0 and year%4==0 or year%400 ==0  and year%4==0:
    print(f"{year} is leap year ")
else:
    print(f"{year} is  Not a leap year ")       
     


s = "Prathmesh"
a = s[-1::1]
print(a)
    
    