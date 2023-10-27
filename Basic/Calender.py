
# # # # # # # # # # # a = "Prathmesh Sargar"
# # # # # # # # # # # print(a)

# # # # # # # # # # # age = 19
# # # # # # # # # # # print(age)

# # # # # # # # # # # city = "Kolhapur"
# # # # # # # # # # # print(city)

# # # # # # # # # # marks = eval(input("Enter your CET Score :"))
# # # # # # # # # # if marks >=90 :
# # # # # # # # # #     print("Best score Excellent  ")    
# # # # # # # # # # elif marks <90 and marks >=80:
# # # # # # # # # #     print("Better Score") 
# # # # # # # # # # elif marks <80 and marks >=70 :
# # # # # # # # # #     print("Good Score")
# # # # # # # # # # elif marks <70 and marks >=50 :
# # # # # # # # # #     print("Average Score ")
# # # # # # # # # # else:
# # # # # # # # # #     print("Work hard in college ")               
    
# # # # # # # # # a = 12
# # # # # # # # # # Nested if statement ok ...!!!!
# # # # # # # # # if a>4:
# # # # # # # # #     if a<19:
# # # # # # # # #         print("a is greater then 4 and less then 19 ok ")    


# # # # # # # # a = input("Enter your name ")
# # # # # # # # age = 12
# # # # # # # # # Concatnnte number we are using com " , "
# # # # # # # # print("My name is "+a+ " ages is ",age)


# # # # # # # # One of the Example of Membership operator is : -

# # # # # # # # list1 = [12,34,45,"Sahil","Ganesh"]
# # # # # # # # a = "Ganesh" in list1    # it chack given element is one of the part of given list or nor ok 
# # # # # # # # print(a)   # "Ganesh "  this is not member ok 

# # # # # # # n1 = eval(input("Enter first number :"))
# # # # # # # n2 = eval(input("Enter Second number :"))
# # # # # # # ch = input("Enter the correct opertor : ")

              # switch case concept is used here ok .......!!!!
              
# # # # # # # if ch == '+':
# # # # # # #     res = n1+n2
# # # # # # #     print(f"Addition of {n1}  + {n1 } is : {res}")
# # # # # # # elif ch =='-':
# # # # # # #     res = n1-n2
# # # # # # #     print(f"Substraction of two number {n1} - {n2} is : {res}")    
    
# # # # # # # elif ch =='X':
# # # # # # #     res = n1*n2
# # # # # # #     print(f"multiplcation of two number {n1} X {n2} is : {res}") 
# # # # # # # elif ch =='/':
# # # # # # #     res = n1/n2
# # # # # # #     print(f"Division  of two number {n1} / {n2} is : {res}") 
# # # # # # # elif ch =='power':
# # # # # # #     res = n1**n2
# # # # # # #     print(f"poer  of number {n1}  power {n2} is : {res}")    
# # # # # # # elif ch=='%':
# # # # # # #     res = n1%n2
# # # # # # #     print(f" Module of two number {n1} % {n2} is : {res}")
# # # # # # # else :
# # # # # # #     print("Please inter Correct opertot ok .....!!!!")    
            
# # # # # # num = eval(input("Enter the number: "))
# # # # # # if num%2==0:
# # # # # #     print("Even number ")
# # # # # # else :
# # # # # #     print("odd number ")    


# # # # # st = input('Enter the String :')


# # # # # Factorial of given number ...!!!

# # # # # Wrong program in python
# # # # # --------------><----------------------
# # # # # n = int(input("Enter the number : "))
# # # # # s = 1
# # # # # for a in range(1,n):
# # # # #     print( a , " ", a

# # # # for a in range(1,6):
# # # #      print(a)
# # # # number = list(range(1,6))   #  list()  <---->  Convert into list ok....!!   first number is inclusive and last number is Exclusive 
# # # # print(number)     

# # # # # While loop in python
# # # # count = 1  # Initilization
# # # # while count<=10:  # Condition 
# # # #      print(count)  # Print statement 
# # # #      count +=1  # Incre / Decre

# # # # String Slicing in python 

# # # str1 = input("Enter your any String ")
# # # l = len(str1)
# # # st = str1[-1::-1]  # this is concept of reverse String ok 
# # # # print(st)

# # # if str1 == st:
# # #      print("Palandrome String ")
# # # else :
# # #      print("Not a Palandrome String ok ")     


# # # num = input("Enter the any value number :")
# # # print(f"Before reversing {num} ")
# # # num1 = num[-1::-1]
# # # print(f" After reversing : {num1}")


# # # reverse the given String 
# # # with using index position ok .....!!!

# # # str1 = input("ENter the String :")
# # # print(str1)
# # # st = str1[-1::-1]  # this is trick to reverse any type of input value ok 
# # # print(st)

# # # str1[ initialize : condition exicute at the end th value : Incre /Decre ]



# # # String itration in python 

# # # str1 = "Coding"
# # # for st in str1:  # for loop is used for itration ok 
# # #      print(st)
     
# # a = "String"
# # b = len(a) # find length of String 
# # print(b)

# # c = a[-1::-1]  # reverse String concept in python ok ....!!
# # print(c)


# # a = "prathmesh"
# # a= a.upper()
# # print(a)

# # b = "SARGAR"
# # z = b.lower()
# # print(b)
# # print(z)

# # z = z.capitalize()  #Capitalize mean  first letter is capital ok not all 
# # print(z)
# # a = a.capitalize()
# # print(a)
     
# # sript

# a = "    python   "
# print(len(a))  # 13 length
# b = a.strip()
# print(b)
# print(len(b))  # 6 length 


# text = "rem and sham" 
# trs = text.find("rem")   # it show the index option in givnen String ok ...!!
# print(trs)  
# trs1 = text.find("sham")
# print(trs1)
  
# st = "Relationship  is Good for life  "
# print(st)
# str = st.replace("Good", "Bad") # it is casesensitive 
# print(str)  

# str = "ram sham 213 dfksj" # where he see space he gives where " , " ok ....!!!
# s = str.split()
# print(s) 

# str = ['12','prathmesh','sargar','sonali']  # same datatype is requried ok 
# print(str)
# # print(s)
# s = ",".join(str)  # join function is used for that ok ...!!
# print(s)


# fruits = ['apple', 'banana', 'cherry']
# text = ",".join(fruits)  # "apple,banana,cherry"  
# print(text)

# str = 'prathmesh sargar'
# s = str.startwith('prathmesh')
# print(s)

# text = "Hello, World!"
# starts_with_hello = text.startswith("Hello")  # True
# print(starts_with_hello)

# text1 = "start, wrold"
# str = text1.endswith("wrold")  # it is case sensitive ok 
# print(str)

# num = 12
# str = str(num)  # Convert number into String  
# print(str)
# print(type(str))  


# charvalue = ord('P')  # ord() convert charactor value into integer ok 
# print(charvalue)

# charvalue = ord('S')  # ord() convert charactor value into integer ok 
# print(charvalue)
 
#  ord() ==>  convert charactor into integer ok 
#  chr() ==>  convert integer into charctor ok 
 
# value = chr(100)
# print(value)


# value1 = ord('A')  65
# print(value1)

# valu2 = chr(101)   e
# print(valu2)

# value3 = ord('D')    68
# print(value3)

# Formated String program in python ok .....!!

# name = "prathmesh"
# age = 19

# bio = "my name is {} and i am {} years old ...".format(name,age)
# bio1 = "my name is {0} and i am {1} years old ...".format(name,age)
# print(bio)
# print(bio1)

# name1 = "sahil"
# gfname = "Sanika"
# # In this value is assigement ok ....!!!
# bio = "my friend name is {a} and his Girlfrined name is {b}".format(a = name1,b = gfname)
# print(bio)


# list1 = ['prathmesh', 'Sahil','Ganesh','Savrabh', 'sanika','Monika','Sonali']
# print(list1)

# list1[0]= "Ajit"
# print(list1)

# list1.append("sakshi")    # By using  append()  function  We can add element in it ok....!!! 

# print(list1)

# list1.remove("sakshi")    # this is used for remove element ok ....!!!!
# print(list1)
 
# list1.pop()    # It remove last element ok...!!!
# print(list1) 
 
 
# n = [12,23,45,56,78,89,90,10]
# # print(n)

# n.sort()  # sorting given 
# print(n)


# a = [12,34,72,82,754,23,12,12]
# print(a)   # Print value of a 
# a.reverse()
# print(a)  # print reverse value of a 

# a.sort()
# print(a)

# a.append(12) # append()  method add value in given String ok 
# print(a)   

# a.remove(12)  # it remove first element ok 
# print(a)

# a.insert(12,23)  # insert() method add first position element it requried two aggrument ok 
# print(a)

# a.pop()   # it remove last element of given list ok 
# print(a)

# c=a.index(23)   # It gives index position of given array of element ok 
# print(c)
    
# a.extend(12)     This is getting me wrong ok , are you with me ......!!!!
# print(a)

# a.clear()   # It remove all element in given array , Clear all element in this array ok 
# print(a)

# n = a.count(12)  # It show how many times 12 in repite in given array ok 
# print(n)

# a.clear()
# print(a)

# a.append(12)
# print(a)

# a.append(23)
# print(a)
# a.append(154)
# print(a)

# a.pop()  # pop()  method remove last element ok .....!!!!
# print(a)

# a.insert(0,24)  
# print(a)

# a.insert(0,100)   # insert function take place is that ok   insert(  IndexValue  ,  Value  )
# print(a)


# b=a.copy()        # It is used for copy element form one list to anothor list ok 
# print( "Print list of b element ok : ",b)

# c=a.count(23)  # it gives index position of given array element ok 
# print(c)

# a.clear()
# print(a)

# a.append(100)
# print(a)
# a.append(200)
# print(a)
# a.append(300)
# print(a)
# a.append(400)
# print(a)
# a.append(500)
# print(a)

# a.pop() # Remove last Element ok 
# print(a)

# b= a.copy()
# print(b)

# b.append(180)  # Their are lots of things which we are try to things about that ok ...
# print(b)   

# a.append(10000)
# print(a)


# Nested list in python ok....!!

# list1 =[[1,2,3],[4,5,6],[7,8,9]] 
# for a in list1:                   # for loop is used for itration ok ......!!!!
#     print(a)
# print(len(list1))

# print(list1[0])  # It first element ok 
# print(list1[0][0])  # = 1 answer ok   

#  String slicing in python ok ....!

# list1 = [12,34,56,89,34,70,23,40,]
# subset = list1[0:]   #  String  Sclicing in python ok are you understading me my dear ok....!
# print(subset)

# subset1 = list1[-1::-1]   # List Sclicing in python ok [ inital : last exicution condi  :  incre / decre ]
# print(subset1)

# list1  =["fruit" ,"Apple" , "Banana","Cherry"]
# list2  =["Color","Red", "Yello", "Red"]
# for a,b in zip(list1,list2):   #  with using zip()  function you can ittrate both list value at same time ok 
#     print(a, "  ",b)

# <----- zip() -------->  function is used for ittrating two list of item at same time ok 
# name =["   name", "Prathmesh","Sahil","Ganesh","Sarthak", "Soham"]
# age  = ["   Age",19,19,20,17,18 ]
# print(name , age)  it print  Combine list of all things ok ...!!!

# for a,b in zip(name, age):
#     print(a, " : ", b)


# split() splits the string on spaces.


# str = "Sargar"   #  Conversation of String into list ok 
# st = list(str)
# print(st)

# str1 = "apple Banana Mango Cherry"  # Split split on space ok " , "
# sp = str1.split()
# print(sp)

# str2 = "ram,sham,rakesh,radha,sopan"
# sp = str2.split(",")      # Split given string in  " , "  sperate ok ....!!!
# print(sp)

# Conversation of String into List ok 

# split()  function is used 

# str2 = "I LOve you my dear frined ok "   #  list()  Convert String into list ok 
# print(list(str2))

# str = "ram shap ddfa"  # ['ram' , 'shap' , 'ddfa' ]
# st = str.split() #  split at space ok 
# print(st)

#   stack and Queue in python ok 

# stack = []
# stack.append(12)
# stack.append(13)
# stack.append(15)
# stack.append(17)
# stack.append(20)
# print(stack)

# stack.pop()  # pop() function remove last element ok 
# print(stack)

# stack =[]
# stack.append(100)
# stack.append(15)
# stack.append(45)
# stack.append(12)
# print(stack)
# stack.sort()  # Sorting  stack element ok ....!!!
# print(stack)

# queue = []

# queue.append(100)
# print(queue)
# queue.append(120)
# queue.append(190)
# queue.append(140)
# print(queue)

# queue.popleft()
# print(queue)

# Dictornary in python ok .....!!!

person ={
    'name':'prathmesh',
    'age':19,
    'city':'Kolhapur'
}
# print(person)
# for a in person:  ------------>   it print only key of dic 
    # print(a)
    
# st = person.keys()   -------------->        keys()  
# print(st)

# val = person.values() ---------->           values()
# print(val)

# item = person.items()  ---------------->    items()  
# print(item)

# person['name'] = "Sahil"  # Update name to sahil form prathmesh ok....!!

# print(person.items())


# Square root generator program in python

# sqrt1 = {x:x**2 for x in range(1,10)}
# # print(sqrt1)
# for a in sqrt1:
#     print(a," : ", a*a)


# dic = {
#     'Bio':{
#         'name':'prathmesh',
#         'age':19,
#         'city':'Kolhapur'
#     },
#     'info':{
#         'e-mail':'sargarprathmesh007@gmail.com',
#         'phone_number':8010618424,    
#     }   
# }
   
# print(dic)

# print(dic['Bio'])
# print(dic['info'])


# dic.clear()  # clear()  function clear all element in given dic 
# print(dic)
    
#   Set in python -------------->

# set1 = {12,34,67,80,90}  # set in unorder ok  given random output 
# set2 ={100,200,300,400}
# print(set1)

# set1.add(100)
# print(set1)

# set1.pop()
# print(set1)

# set1.remove(100) # remove() function is used for removing perticular value ok 
# print(set1)

# set1.update(set2)  # It add set1  as well as set2 element each other ok...!!!
# print(set1)


# set1  ={12,34,45,12,12,56}   # we cant repite element 
# print(set1)

# set1.clear()
# print(set1) # when we used clear() function gives output set() 

# set1.add(1000)
# print(set1)

# set1.add(200)
# print(set1)

# set1.add("ram")
# print(set1)

# set2 = {"Prathmesh", "Sargar" , }
# print(set2)

# set1.update(set2)
# print(set1)

# set1.remove("Sargar")  #  It remove "Sargar"  ok 
# print(set1)

# list1 = [1,2,3,4,5,6,7]
# list1.append(15)
# print(list1)

# print(set(list1)) # set()  function convert list into set ok ....!!!

# for a in list1:
#     print(a ,":",a*a)
    
# set1 = {12,34,56,78}
# set2 = {90,89,78,67,12}
# print(set1.union(set2))   # union()  function add two sets each other ok 

# set1 ={12,23,45,57,12,12}
# print(list(set1))
# print(set1)

# list1 =[12,12,123,4456,12]  # list in which you can do somethings ok , you understand it my dear ok ....!!
# print(list1)
# print(set(list1)) 

# Functions in python ok ....!!!

# def good():  #  here i am creating a function using def keyword ok 

#     print("Your name is prathmesh ok ...")
    
    
    #  Simple functions 
# good()    Here i am calling the give good() function 
# because when you call the function then that time function code is run ok 

# agrumented functions ok 
# def great(a,b):
#     print(a+b)
    
# great(12,12)      # here i am calling the given function ok 12,12  is a parameter ok (a,b)
# great(100,100) # great(a, b ) a and b is a parameter ok you understand it 

# Return type function in python ok 

# def grow(a,b):
#     return a+b    # when we return something then you should 
# # must store this value in another variable as well ok 


# sum = grow(12,12)
# print("Addition of two number is : ",sum)

# def Love(n):
#     c = "Prathmesh love you as ",n," ok my dear "
#     return c

# def love():
#     print("Prathmesh sargar love you to much ok ")

# love()  

# def add(a,b):
#     c = a+b
#     print(c)
    
# add(12,90)   # Here i am calling this function ok you understand it 


# def ratio(a,b):
#     return a*b 

# ratio(12,12)   # Here we only calling function function but we are return this function that's wise is most important 
#  store this value of function in anoter function ok 
# and print this variable where we store value of this variable ok , you understand it
# multiplication = ratio(12,12)  # we store value of function in multiplication name variable ok 
# print(multiplication)  # Here i am printing this variable ok                 


# def square(a):   # here i am define functrion ok 
#     return a*a  # here return the function ok 
# a = int(input("Enter the number : "))   #  user input in this  ok 
# square = square(a)   # store value in variable square ok  
# print( "Square of give number",a, " is  : " ,square)    # Here print the value of variable ok 


# Lymbda function 

square = lambda x :x**2
result = square(2)
print(result)



cube = lambda a :a**3     # this are known as lymbda function ko 
result = cube(5)
print(result)



