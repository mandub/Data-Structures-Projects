""" First I need to import  turtle,stack,time"""
from turtle import *
import turtle
from stack import Stack
import time 
""" the main method will be alanazi_hiker """
""" this function will read the file and call anther function called (draw) to draw the maze """
def Alanazi_hiker(My_file_name):
    mountain_list=[]
    my_file = open(My_file_name, "r+")
    """ read ecah line and append it to a list of lists"""
    for line in my_file:
        mountain_row=[]
        for char in line:
            if char != '\n':
                mountain_row.append(char)
        mountain_list.append(mountain_row)
    my_file.close()    

    draw(mountain_list)
""" this function will receive the list and draw the maze and will control the walker move to the end """    
def draw(mountain_list):
  screen = Screen()
  Walker = "g.gif"
  Tree = "Tree.gif"
  Mountain= "m.gif"
  Visited="v.gif"
  Parking="p.gif"
  Win="w.gif"
  WinText="wtxt.gif"
  Lose="L.gif"
  Losetext="ltxt.gif"
  mystack = Stack()
  win = False
  """ here I will calculate the position of X and Y which will the start point for the maze"""
  x = int(- (len(mountain_list) /2) * 25)
  y = int((len(mountain_list[0]) /2) * 25)
  screen.addshape(Walker)
  screen.addshape(Tree)
  screen.addshape(Mountain)
  screen.addshape(Visited)
  screen.addshape(Parking)
  screen.addshape(Win)
  screen.addshape(WinText)
  screen.addshape(Lose)
  screen.addshape(Losetext)
  screen.bgcolor("lightblue")
  tree = Turtle()
  walker = Turtle()
  mountain = Turtle()
  visited = Turtle()
  parking= Turtle()
  winning =Turtle()
  winningtext =Turtle()
  lose=Turtle()
  losetext=Turtle()
  
  tree.shape(Tree)
  tree.setpos(x, y)
  tree.up()
  
  """ here start to draw the maze and also determined where the walker can start"""
  for j in range (0,len(mountain_list) ):
      for i in range (0,len(mountain_list[0])):
          
          
          if (mountain_list[j][i] == "^"):
              tree.setpos(x + i *25, y - j * 25)
              tree.stamp()
          if (mountain_list[j][i] == "P"):
              walker.shape(Walker)
              walker.up()
              walker.setpos(x + i *25, y - j * 25)
              walker.stamp()
              visited_position=[j,i]
              Lose_position=[j,i]
              if (i+1 <  len(mountain_list[0])):
                  if (mountain_list[j][i +1]== " "):
                      open_position = [j,i+1]
                      mystack.push(open_position)
              if (j+1 < len(mountain_list)):
                  if (mountain_list[j+1][i]== " "):
                      open_position = [j+1,i]
                      mystack.push(open_position)
              if ( i-1 >= 0):
                  if (mountain_list[j][i-1]== " "):
                      open_position=[j,i-1]
                      mystack.push(open_position)
              if (j-1 >=0):
                  if (mountain_list[j-1][i]== " "):
                      open_position=[j-1,i]
                      mystack.push(open_position)
                                
          if (mountain_list[j][i] == "T"):
              mountain.shape(Mountain)
              mountain.up()
              mountain.setpos(x + i *25, y - j * 25)
              mountain.stamp()              
          
  
  parking.shape(Parking)
  parking.up()
  parking.setpos(x + visited_position[1] *25, y - visited_position[0] * 25)
  parking.stamp()
  walker.clearstamps()
  walker.up()
  visited.shape(Visited)
  visited.up()
  """this while loop will find the open spaces and put them to the sack then it will make walker move to new spot until she found the top of the mountain or the stack is empty"""
  while (not mystack.isEmpty() and not win ):
      newpositions = mystack.pop()
      walker.setpos((x + newpositions[1] *25, y - newpositions[0] * 25))
      #wait for one second
      #time.sleep(1)
      i=newpositions[1]
      j=newpositions[0]

      if (i+1 <  len(mountain_list[0])):
          if (mountain_list[j][i +1]== " " or mountain_list[j][i +1]== "T"):
              open_position = [j,i+1]
              mystack.push(open_position)
              if (mountain_list[j][i +1]== "T"):
                  win = True
                  winning_position=[j,i+1]
      if (j+1 < len(mountain_list)):
          if (mountain_list[j+1][i]== " " or  mountain_list[j+1][i]== "T"):
              open_position = [j+1,i]
              mystack.push(open_position )
              if (mountain_list[j+1][i]== "T"):
                  win = True
                  winning_position=[j+1,i]
      if ( i-1 >= 0):
          if (mountain_list[j][i-1]== " " or mountain_list[j][i-1]== "T"):
              open_position=[j,i-1]
              mystack.push(open_position)
              if (mountain_list[j][i-1]== "T"):
                  win = True
                  winning_position=[j,i-1]
      if (j-1 >=0):
          if (mountain_list[j-1][i]== " " or mountain_list[j-1][i]== "T"):
              open_position=[j-1,i]
              mystack.push(open_position)
              if (mountain_list[j-1][i]== "T"):
                  win = True
                  winning_position=[j-1,i]
                  
                  
              

      visited_position = newpositions
      visited.setpos(x + visited_position[1] *25, y - visited_position[0] * 25)
      visited.stamp()
      mountain_list[visited_position[0]][visited_position[1]] = "V"
      
  """ if she found the top she will win"""
  """ else she will lose"""
  if (win):
      winning.shape(Win)
      winningtext.shape(WinText)
      winning.up()
      winningtext.up()
      winning.setpos(x + winning_position[1]*25, y - winning_position[0] * 25)
      winningtext.setpos(x /2  , y + 50)
      winning.stamp()
      winningtext.stamp()
  else:
      lose.shape(Lose)
      losetext.shape(Losetext)
      lose.up()
      losetext.up()
      lose.setpos(x + Lose_position[1]*25, y - Lose_position[0] * 25)
      losetext.setpos(x /2  , y + 50)
      lose.stamp()
      losetext.stamp()
      

Alanazi_hiker("mountain.txt")
