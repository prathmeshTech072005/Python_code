# # # # # # Used case of   list , dictionary  , set 


# # # # # # list1  = [12,34,67,8990,67]

# # # # # # print(list1)
# # # # # # Iterate element
# # # # # # for a in list1:
# # # # # #     print(a)

# # # # # # for itrating value we are using for loop 

# # # # # # for n in range(0,5):
# # # # # #     # print(n) 
# # # # # #     print(list1[n])   

# # # # # list1 = [[12,45],[34,89],[78,9],45,7845]
# # # # # print(list1)
# # # # # a = len(list1)
# # # # # print(a)

# # # # # for n in list1:   # this is for each loop in python ok .......!!!
# # # # #     print(n)



    
# # # # # # --------------------------------------------------------------------------
# # # # # # Dictionary 
# # # # # dic = {'name':'prathtmesh',
# # # # #        'age':19,
# # # # #        'city':'kolhapur'}
# # # # # print(type(dic))
# # # # # print(dic)
# # # # # for a in dic:
# # # # #     print(a,':' ,dic[a])
    


  

# # # # #     # -------------------------------------------
# # # # #   #tuple   
# # # # # set1 =(12,23,45,67)  
# # # # # print(type(set1))  

# # # # # stt2 = (12)
# # # # # print(type(stt2))   # this in int not tuple 

# # # # # # -----------------------------------------

# # # # # a = 12
# # # # # print(a)
# # # # # variable_name = 'String'
# # # # # print(variable_name)
# # # # # print(type(variable_name))
# # # # # print(type(a))


# # # # # Data type in python 

# # # # a = 12
# # # # b= 12.12
# # # # c= "String ...!!!"
# # # # d= True
# # # # list1 = [12,45,6789,78]
# # # # set1 = (12,3,12,3445,)  # it is collection of unique elements ok  # can repite set value in output...!!!
# # # # print(set1)
# # # # dic1 = { "name":" prathmesh",  # key: value pair store ok 
# # # #         "Age": 19,
# # # #         "city": "Mumbai"}

# # # # tupe1 = (12,34,567)
# # # # print(tupe1)

# # # # Concatination in python

# # # str1 = " Prathmesh Sargar"
# # # str2 = "Sargar"
# # # age = 19
# # # print(str1+ " "+str2)  # this is used for concatination ok 
# # # print(str1,str2)  # This also used for concatination ok 
# # # # this is also used for concatination ok 
# # # # print(f " " )  this is used ok 
# # # print(f" my name is {str1} and  i am   {age} years old ")

# # # a = 12
# # # b =12
# # # c = a+b
# # # print(' Addition of two numbers is :' ,c)

# # # a = 12
# # # b= 12
# # # c = a-b
# # # print("Substraction of two numbers :",c)

# # # a = 14 
# # # b = 6
# # # c = a//b  # this is // it is integer Divisior ok 

# # # a = 2
# # # print(a**2)  # It gives square
# # # print(a**3)  # It gives cube root 
# # # print(a**4)  # It gives 4th value og given value ok 

# # # a = 2
# # # a = pow(a,2)  # this is used for given situation ok 
# # # print(a)

# # # a = 2
# # # a *=3
# # # print(a)  #   2*3 = 6 ,,,,,    >>>--- Prathmesh Sargar ---<<< ....!!! 

# # #   &&  =====>  and 
# # #   ||  =====>  or 
# # #   !  ======> not 

# # a = 12
# # b =12
# # c = a==b
# # print(c)

# # a = 12
# # b = 13
# # c = a<= b
# # print(c)

# # a = 12
# # v = 23
# # c = a!=v
# # print(c)

# # a = True
# # b = True
# # c = False
# # print(a and c)
# # print(a or b)


# # a = [12,23,45,34,564,90]
# # print(12 in a)   #  It check it contain or not ok 
  
#   # in   and   not in   this are membership operator ok....!!
   
# # b = [122,567,87,454,2342,234,]
# # print(111 in b)
# # print(11 not in b)


# # python input oprations 

# # a = input("Enter your name : ")
# # print( "Hello " +a+ " , how are you my dear ")
# # cet_per= eval(input("Enter your cet % :"))
# # print(cet_per)


# # Type casting in python 

# # a = 12
# # b = str(a)
# # print(b)
# # print(type(b))

# # type casting python ok 
# a = 12.34
# print(a)
# print(type(a))
# b = int(a)
# print(b)
# print(type(b))

# a =100
# b = float(a)
# print(b)
# print(type(b))



  
  # a = input("Enter the number ")
#   print(a)
# except ValueError :
#   print("Please inter integer value ok ")  
  
# print("you are done")  

Income = eval(input("Enter your monthly income : "))
try :
  if Income >=12000000:
    print(Income) 
except ValueError:
  print("PLease inter number of income ok ")    
  if Income>=980000:
   print(" i can maried with you ")
else :
  print("not maried with ok ")  





    
       