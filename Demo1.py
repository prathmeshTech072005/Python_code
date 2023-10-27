# print("Hello public 23")
# print("Hello public 23")
# print(23+12+  "  prathmesh sargar")
# print('23 +12')
# print(23+23)
#print(12<14)

# variable name cant start with number of their is no space between variable name ok 
# you can used _ in variable name 

#  # a is variable here ok 
# a =12
# print(a)

# print(type(a))   Here print type of variable a is integer ok 


# #  Arithmatic operator 

# a = 12
# b = 23
# print(a+b)
# print(a-b)
# print(a*b)     # multiplication 
# print(a/b)    # Division 
# print(a%b)    # MOdulus 
# print(5**2)    # Exponents 
# print(5**3)    125 this is answer of this statement ok 
# print(5**4) 
# print(10/3)   #3.333333
# print(10//3)   # 3  // it is used for floor division   it gives only integer value ok 
# -------------------------------------------------------
# Assigment operator 
# = , += , =+ 

# x = 5 
# print(x)  # 5
# x = x+5
# print(x)  # 10 
# x+= 5
# print(x)  #15 

# x = x-5   
# print(x)  #10

# x -=5
# print(x)  #5
# ---------------------------------------------------------------------
#  Comparision operator 

# x = 12
# y =23
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x<=y)
# -----------------------------------------------------------------------------------
# Logical operator 

# and   ------------- both condition ares true  then true ok 
# , or  ------------  if any one condition is true then it is true ok 
# , not ------------- it reverse the condtion 

# x = 10
# y = 20

# print(x==10 and y==20)
# print(x==10 and y==20 and x==y)
# print(x==y or x<y)  

# ------------------------------------------------------------------
# Membership operator 


# h = "Hello"
# print(h)

# string1 = "Prathmesh"
# print('h' in string1)  # True   it can be used as contain() method 
# print('p' in string1)  # False    it check given is present or nor ok 


# l = [12,34,23,45,23]
# print(23 in l)  # find solusation 
# print(50 not in l)  # true false check ok 
# ------------------------------------------------------------------------

#  Identity operator ----------is and not is 

# x =10
# y =10
# print(x==y)   compare two values ok 
# print(x is y)   compare x is equals to y ok 
# print(x is not y) 


# Bitwise operator  -------- &  ,  |  ,  ^      Convert into binary form 

# x = 10 
# y = 8
# print(bin(x))  # with bin()  can claculate binary number 
# print(bin(y))

# print(x , bin(x))
# print(y , bin(y))

# a =8
# print(bin(a))   #  Binary number of 8 is 1000 

# ------------------------------------------
# Data type in python 

# # int
# a = 12
# print(type(a))     

# # float 
# n = 2.54
# print(type(n))

# # complex ?
# p = 2+5j
# print(type(p))

# s = "String"
# print(type(s))


# # String and their type 

#   we can write string in ''  , "  "  ,  '''    '''
# st = 'string1'
# print(type(st))

# st1 = "String2"
# print(type(st1))

# st3 = '''
#          Prathmesh
#             Sargar 
#                DYP student ok 
#         '''
# print(st3)      

# a = '10'
# print(a)
# print(type(a))

# # List    it is imutable in python ok 
# # data type in python 

# list1 = [12,23,45,67,89]

# print(list1)
# print(type(list1))
# list1[0]= "Prathmesh sargar"
# print(list1)

# l = [12,5.6 ,'you' , "String"]
# print(l, type(l))

# l[2] = 10
# print(l, type(l))
# -----------------------------------?

# #  Directory  in python 
#  in this -----value   and key is used ofr that ot get output form then user ok 

# 1.  value 
# 2.  key 



# d= {'name': 'prathmesh',
    
#     'Girlfrined ':' Sanika',
    
#      'age ' : 18
#     }
# print(d)
# print(type(d))
# print(d['name'])
# print(d['Girlfrined '])
# print(d['age'])

# ----------------------------------------

# Set
#   In set we can't repeate value or duplicate value 

# s= {12,43,1,12}  #ccant print doplicate element ok 
# print(s)
# print(type(s))

# st = {12,'prathmesh', 18, 'sanika', 'Ganesh'}
# print(st)
# print(type(st))

#   
# list2 = [12,'sanika', 12.534,'Ganesh',80.10, 'sonali']
# print(list2)

# set1 = {'name': 'prathemsh', 
#         'age': '18' ,
#         'result ': '100%' ,
#         'girlfriend ' : 'sanika'
        
#       }

# list3 = [12,'string',12.43 , 'prathmesh', 12.2]
# print(list3)


# a = 12
# print(a)

# l = [12,23,45,67,89,'result' , 'prathmesh007@gmail.com ', 12.34]
# print(l)

# set12 = {12, 'result', 12.23, 'prathmesh_Sargar ', 12.21, 'Sanika'}
# print(set12)


# User input    int , float , eval is play very important roll in this ok 
# -------------------

# a= input("Enter thecfirst value :-")
# b= input("Enter second value :-")

# print(a+b)   # This concatinate value ok 


# n1 = int(input("Enter first value :"))
# n2 = int(input("Enter second value : "))
# print(n1+n2)

# n1 = eval(input("Enter first value :"))
# n2 = eval(input("Enter second value : "))
# print(n1+n2)

# -----------------------------------------------------------------------------------------------

# a= eval(input("Enter the value :-"))
# if a%2==0:
#     print(a, "Even number ")
# else:
#     print(a, "Odd number ")    

# ----------------------------------------------------------------

# input marks 

# marks = eval(input("Enter your marks :-"))
# if marks >=90:
#     print("First division ")
# elif marks >=80:
#     print("Second Division ")
# elif marks <=80 and marks >=50:  
#     print("Thrid Division ")
# else:
#     print("you are fail ")          

money = int(input("Enter how much amount of money you have :"))
if money >=1000:
    print("onmarine line spend holiday ok ")
elif money <=1000 and money >=500:
    print(" on Moll spend holiday") 
elif money <=200 and money>=100:
    print("Side road party ok ")     
elif money<=50  and money>=20:
    print("vada pav on home party ")    
else:
    print("Earn money and then eat food ok ")       






        


















