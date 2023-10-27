# print("Prathmesh Sargar")

# Making game with using computer ok its very important for me to doing such things ok 

import random
while True: 
    Ucount =0
    Ccount = 0
    # import random
    print( '''
      Game Start .......!!!!!
      1. Play
      2. Exict 
      
      ''')
    choice= int(input("Choice : "))
    if choice ==1:
        
        
        for a in range(1,6):
            
            
            Unum = int(input("Enter your number : "))
            Cnum = random.randrange(1,10)
            
            print("Computer number : ",Cnum)
        
            if Unum == Cnum:
                    print(" Congratulation ...!!! ,you guess same number")
                    Ucount = Ucount +1
                    Ccount = Ccount +1
                    break
            elif Unum >Cnum:
                    print("Your number is greater then Computer number ")
                    Ucount = Ucount+1
            else:
                    print("Computer number is greater then your number ")  
                    Ccount = Ccount+1       
            print("-------------------><-------------------")   
            
        print("Your Score : ",Ucount)
        print("Computer Score : ",Ccount)  
        if Ucount == Ccount:
                        print("Drow game ")
        elif Ucount> Ccount :
                        print("you win the match")  
        else :
                        print("Computer win the gaame ")              
    else :
     print("Game is over , Good Bye ")

          