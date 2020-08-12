import sys
board=["-", "-" ,"-",
       "-", "-" ,"-",
       "-", "-" ,"-"]
p = [0,1,2,3,4,5,6,7,8]
iX = [0,0,0,0,0,0,0,0,0]
iO = [0,0,0,0,0,0,0,0,0]

def display_board():
    print("|" + board[0]+ "|"+ board[1]+ "|" + board[2]+ "|")
    print("|" + board[3]+ "|"+ board[4]+ "|" + board[5]+ "|")
    print( "|" + board[6]+ "|"+ board[7]+ "|" + board[8]+ "|")

def horx():
  i = 0
  while i<9:
    if iX[i]+iX[i+1]+iX[i+2] == 3:
     print("player1 won")
     sys.exit()
    i+=3


def verx():
  v=0
  while v<3:
    if iX[v]+iX[v+3]+iX[v+6] == 3:
     print("player1 won")
     sys.exit()
   
    v+=1

def horo():
  i = 0
  while i<9:
    if iO[i]+iO[i+1]+iO[i+2] == 3:
     print("player2 won")
     sys.exit() 
    i+=3


def vero():
  v=0
  while v<3:
    if iO[v]+iO[v+3]+iO[v+6] == 3:
     print("player2 won")
     sys.exit()
   
    v+=1

def diago():
   if iO[0]+iO[4]+iO[8] == 3:
     print("player2 won")
     sys.exit()
   elif(iO[2]+iO[4]+iO[6] == 3) :
      print("player2 won")
      sys.exit()


  

def diagx():
   if iX[0]+iX[4]+iX[8] == 3:
     print("player1 won")
     sys.exit()
   elif iX[2]+iX[4]+iX[6] == 3:
      print("player1 won")
      sys.exit()
      
     
    
   

  


'''def win_check():
 
    if board[0] == "X" and board[3]=="X" and board[6]=="X":
       print("player 1 won!")
       sys.exit("Game Ended")
    elif board[0]=="O" and board[3]=="O" and board[6]=="O":
      print("player2 won!")
      sys.exit("Game Ended")
    elif board[0]=="X" and board[1]=="X" and board[2]=="X":
         print("player1 won!")
         sys.exit("Game Ended")
    elif board[0]=="O" and board[1]=="O" and board[2]=="O":
         print("player2 won!")
         sys.exit("Game Ended")
    elif board[3]=="X" and board[4]=="X" and board[5]=="X":
         print("player1 won!")
         sys.exit("Game Ended")
    elif board[3]=="O" and board[4]=="O" and board[5]=="O":
         print("player2 won!")
         sys.exit("Game Ended")
    elif board[6]=="X" and board[7]=="X" and board[8]=="X":
        print("player1 won!")
        sys.exit("Game Ended")
    elif board[6]=="O" and board[7]=="O" and board[8]=="O":
         print("player2 won")
         sys.exit("Game Ended")
    elif board[1]=="X" and board[4]=="X" and board[7]=="x":
         print("player1 won!")
         sys.exit("Game Ended")
    elif board[1]=="O" and board[4]=="O" and board[7]=="O":
         print("player1 won!")
         sys.exit("Game Ended")
    elif board[2]=="O" and board[5]=="O" and board[8]=="O":
         print("player2 won!")
         sys.exit("Game Ended")
    elif board[2]=="X" and board[5]=="X" and board[8]=="X":
         print("player1 won!")
         sys.exit("Game Ended")
    elif board[0]=="X" and board[4]=="X" and board[8]=="X":
        print("player1 won!")
        sys.exit("Game Ended")
    elif board[2]=="O" and board[4]=="O" and board[6]=="O":
         print("player2 won")
         sys.exit("Game Ended")
    elif board[2]=="X" and board[4]=="X" and board[6]=="X":
         print("player1 won")
         sys.exit("Game Ended")
    elif board[0]=="X" and board[4]=="X" and board[8]=="X":
        print("player1 won!")
        sys.exit("Game Ended")
    elif board[0]=="O" and board[4]=="O" and board[8]=="O":
         print("player2 won")
         sys.exit("Game Ended")   
'''


def player1():
  position = input("Please p1 insert a position from 1-9:")
  position = int(position) - 1
  if position in p :  

   board[position] = "X"
   
   display_board()
   p.remove(position)
   iX[position] = 1 
   horx()  
   verx()
   diagx()
   
  else: 
      print("this position is already taken")
      return player1()
  #win_check()
  
 
  player2()

def player2():
  position = input("Please p2 insert a position from 1-9:")
  position = int(position) - 1
  if position in p :  

   board[position] = "O"

   display_board()
   p.remove(position)
   iO[position]=1
   horo()
   vero()
   diago()
  else :
    print("this position is already taken")
    return player2()
  #win_check()


  player1()


def play_game():
  display_board()
  player1()

play_game()
  



  

       
   
 