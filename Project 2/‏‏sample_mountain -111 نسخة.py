from turtle import *
import turtle

def mymain():
    mountain_list=[]
    my_file = open("characters.txt", "r+")
    for line in my_file:
        mountain_row=[]
        for char in line:
            if char != '\n':
                mountain_row.append(char)
        mountain_list.append(mountain_row)
    my_file.close()
    for i in mountain_list:
        print(i)
    print("____________")
    for i in range(len(mountain_list)):
        for j in range(len(mountain_list[0])):
            p=0
            #print("pos[",i,"][",j,"]:", mountain_list[i][j])
    drow(mountain_list)
def drow(mountain_list):
  screen = Screen()
  Walker = "g.gif"
  Tree = "Tree.gif"
  Mountain= "m.gif"
  x = - (len(mountain_list) /2) * 25
  y = (len(mountain_list[0]) /2) * 25
  print (x , " >>>>>>>>", y,"len(mountain_list)",len(mountain_list) )
  screen.addshape(Walker)
  screen.addshape(Tree)
  screen.addshape(Mountain)
  #turtle.shape(Walker)
  screen.bgcolor("lightblue")
  tree = Turtle()
  walker = Turtle()
  mountain = Turtle()
  mountain.shape(Mountain)
  walker.shape(Walker)
  #walker.setpos(0, 0)
  #tess.color("blue")
  tree.shape(Tree)
  tree.setpos(x, y)
  tree.up()
  walker.up()
  mountain.up()
  print (tree.position())
  #tree.forward(250)
  tree.clearstamps()
  for j in range (0,len(mountain_list) ):
      for i in range (0,len(mountain_list[0])):
          
          
          if (mountain_list[j][i] == "^"):
              tree.setpos(x + i *25, y - j * 25)
              tree.stamp()
          if (mountain_list[j][i] == "p"):
              walker.setpos(x + i *25, y - j * 25)
              walker.stamp()
          if (mountain_list[j][i] == "t"):
              mountain.setpos(x + i *25, y - j * 25)
              mountain.stamp()              
          
          #print (mountain_list[j][i])
      
  """tree.backward(300)
  tree.stamp()
  tree.left(90)
  tree.stamp()
  tree.forward(250)
  #tess.stamp()
  tree.right(90)#start here
  print (tree.position())"""
  """for j in range (0,10):
      for i in range(0,10):
          tess.stamp()
          tess.forward(50)
      tess.backward(500)
      tess.right(90)
      tess.forward(50)
      #tess.stamp()
      tess.left(90)"""
  #tess.clearstamps()
  


mymain()
