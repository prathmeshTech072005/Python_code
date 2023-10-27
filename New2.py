# find uesd

a = "how are you my dear friend......!!!!!"
print(a)
print(a.find("f"))  # it give index position element 

print(a.index("a"))  # it gives error when input string is not given

s = "Sanika"
print(s.isalpha())  # it gives only true or false value ok 
# --------------------------
p = "sanika143"
print(p.isalpha())
# -------------------------
r= "143"   
print(r.isdigit())
# -------------------------------------

id = "prathmesh007"
print(id.isalnum())  # it gives TRUE  when you inPuter either ALPHABET OR NUMBER 

# improtant it is used for that you can d osome things 



# ---------------------><-----------------
# A = ""
# print(A.find())
# print(A.index())
# print(A.isalpha())
# print(A.isdigit())
# print(A.isalnum())



# Python char() and ord()   function ok 

# It convert numeric value into character ok 

# x = chr(97)
# print(x)

# y = chr(45)
# print(y)

# a = chr(100) # it convert number into its character 
# print(a)

# ------------------------------------------------------------------------------

# s = ord("A")   # all this charater have their own unique value ok 
# print(s)

# a= ord("%")
# print(a)

# b= ord("/")
# print(b)

# p= ord("&")
# print(p)

# ----------------------><----------------------


# Python String format method ok 

s = "Prathmesh sargar {} he is {} old ok ".format(" good boy ", 18)
print(s)

p = "this day is very {0}  for me {1} you are smart bro  ".format("important", " i known you are smart ")

print(p)


sp = "sanika {a} % love you prathmesh".format(a=99.99)
print(sp)
