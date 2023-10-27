
# # #  #Math modules 
 
# # # import math

# # # a= int(input("Enter the number : "))

# # # result = math.sqrt(a)
# # # print(f" Square root of given number {a} is :  {result}")


# # # b = int(input("Enter the number  : "))
# # # c  = int(input("Enter the power : "))
# # # result = math.pow(b,c)

# # # print(f" power of given number {b} is {c} is  : {result}")

# # # Random number modules ok .....!!!!!!

# # import random
# # r = random.random()
# # print(r)

# # a = random.randint(1,100)
# # print(a)

# # s = random.randrange(1,100)
# # print(s)

# # l = ["Prathmesh","Sahil","Ganesh","Sai"]
# # ch = random.choice(l)  # It gives random value form given list ok you understand it 
# # print(ch)

# import datetime

# # a = datetime.datetime() -----------> not give any output ok 
# # print(a)

# s = datetime.datetime.now()
# print(s)

# Number gussing game in python   ok

while True:
    import random
    print('''
                Start Game.....!!!!!!
                
                1.  Play
                2.  Exict 
                
                    ''')
    ch = int(input("Choice : "))

    if ch ==1:
        Unum = int(input("Enter your number : "))
        Cnum = random.randint(1,10)
        print("Computer number is : ",Cnum)
        if Unum==Cnum:
            print("Congratulation..!!!, you gusses acqurate number ...")
        elif Cnum> Unum:
            print("Computer number is greater then your number ...")
        else:
            print("your number is greater then computer number ...")
            
            print("-----------------><-------------------")
    else:
            print("Game is over ....!!!")
            break