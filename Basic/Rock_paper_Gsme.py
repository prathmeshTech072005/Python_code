# Rock_Paper_Game

import random

while True:
    print('''
          Game Start....!!!
          1. Play
          2. Excit
          ''')
    ch = int(input("Choice : "))
 
    for a in range(1,6):   
     if ch ==1:
             print('''
              1. Rock
              2. paper
              3.Scissor ''')
             User_input = int(input())
             if User_input ==1:
               Uinput= "Rock"
             elif User_input == 2:
                Uinput= "Paper"
             elif User_input ==3:
              Uinput= "Scissor" 
                
                
             ch = ["Rock","Paper","Scissors"]
             Ccoice = random.choice(ch) 
             print(f" Computer choise is : {Ccoice}")
                
             print(f"your  choice is : {Uinput}") 
                
                
             if Uinput == Ccoice:
                    print("Drow the game   ")
             elif (Uinput == "Rock" and Ccoice=="Scissor")or (Uinput == "Paper" and Ccoice=="Rock")or(Uinput == "Scissor" and Ccoice=="Paper"):
                    
              print("you win")
             else:
                    print("computer win the game ")   
        
              

    else:
        print("Game is over ")
   
