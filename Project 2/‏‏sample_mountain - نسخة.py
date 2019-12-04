from turtle import *
import turtle
from stack import Stack
import time 

def alanazi_hiker(My_file_name):
    mountain_list=[]
    my_file = open(My_file_name, "r+")
    for line in my_file:
        mountain_row=[]
        for char in line:
            if char != '\n':
                mountain_row.append(char)
        mountain_list.append(mountain_row)
    my_file.close()
    #Sfor i in mountain_list:
        #print(i)
    #print("____________")
    for i in range(len(mountain_list)):
        for j in range(len(mountain_list[0])):
            p=0
            #print("pos[",i,"][",j,"]:", mountain_list[i][j])
    
    #open_position = [i,j]
    #mystack.push(open_position)
    #newlist=mystack.pop()
    #print (newlist)
    drow(mountain_list)
def drow(mountain_list):
  screen = Screen()
  Walker = "g.gif"
  Tree = "Tree.gif"
  Mountain= "m.gif"
  Visited="v.gif"
  Parking="p.gif"
  Win="w.gif"
  Lose="L.gif"
  mystack = Stack()
  win = False
  
  x = int(- (len(mountain_list) /2) * 25)
  y = int((len(mountain_list[0]) /2) * 25)
  print (x , " >>>>>>>>", y,"len(mountain_list)",len(mountain_list) )
  screen.addshape(Walker)
  screen.addshape(Tree)
  screen.addshape(Mountain)
  screen.addshape(Visited)
  screen.addshape(Parking)
  screen.addshape(Win)
  screen.addshape(Lose)
  #turtle.shape(Walker)
  screen.bgcolor("lightblue")
  tree = Turtle()
  walker = Turtle()
  mountain = Turtle()
  visited = Turtle()
  parking= Turtle()
  winning =Turtle()
  lose=Turtle()
  #walker.setpos(0, 0)
  #tess.color("blue")
  tree.shape(Tree)
  tree.setpos(x, y)
  tree.up()
  
  
  #print (tree.position())
  #tree.forward(250)
  tree.clearstamps()
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
          
          #print (mountain_list[j][i])
  #print (mystack.pop())
  #print (mystack.pop())
  print (mystack.isEmpty())
  
  parking.shape(Parking)
  parking.up()
  parking.setpos(x + visited_position[1] *25, y - visited_position[0] * 25)
  parking.stamp()
  walker.clearstamps()
  walker.up()
  visited.shape(Visited)
  visited.up()
  while (not mystack.isEmpty() and not win ):
      newpositions = mystack.pop()
      walker.setpos((x + newpositions[1] *25, y - newpositions[0] * 25))
      #wait for one second
      time.sleep(1)
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
      
      
  if (win):
      winning.shape(Win)
      winning.up()
      winning.setpos(x + winning_position[1]*25, y - winning_position[0] * 25)
      winning.stamp()
  else:
      lose.shape(Lose)
      lose.up()
      lose.setpos(x + Lose_position[1]*25, y - Lose_position[0] * 25)
      lose.stamp()      
      

alanazi_hiker("mountain.txt")
