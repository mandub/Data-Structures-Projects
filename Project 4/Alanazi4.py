import sys
import os
import unittest
from turtle import *
import turtle
import random
global No_Gragh
No_Gragh=True
############################## FROM https://github.com/bnmnetp/pythonds #####################################
class PriorityQueue:
    def __init__(self):
        self.heapArray = [(0,0)]
        self.currentSize = 0

    def buildHeap(self,alist):
        self.currentSize = len(alist)
        self.heapArray = [(0,0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2            
        while (i > 0):
            self.percDown(i)
            i = i - 1
                        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc
                
    def minChild(self,i):
        if i*2 > self.currentSize:
            return -1
        else:
            if i*2 + 1 > self.currentSize:
                return i*2
            else:
                if self.heapArray[i*2][0] < self.heapArray[i*2+1][0]:
                    return i*2
                else:
                    return i*2+1

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i//2][0]:
               tmp = self.heapArray[i//2]
               self.heapArray[i//2] = self.heapArray[i]
               self.heapArray[i] = tmp
            i = i//2
 
    def add(self,k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return retval
        
    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def decreaseKey(self,val,amt):
        # this is a little wierd, but we need to find the heap thing to decrease by
        # looking at its value
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt,self.heapArray[myKey][1])
            self.percUp(myKey)
            
    def __contains__(self,vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False
                
class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id

############################## FROM THE BOOK #####################################
class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
    """  I ADD THIS LINES TO DELETE ALL VertexS """
    def deleteALL(self):
        self.vertices = {}
        self.numVertices = 0        
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())
""" -------------------dijkstra --------------- """
def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)
""" -------DFSGraph--------"""
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
################################## MY CODE  ################################################
""" This method to display Topological sort"""
def Topological_sort():
    NoGragh=True
    startpintcheck=True
    d={}
    if (d == g.vertices):
        print ("Empty Graph")
    else:
        NoGragh= False
    if(NoGragh):
        print ("No Graph has Added yat ..")
        return
    
    while (startpintcheck):
        startpoint= input("Enter the start vertex: ")
        if (isitthere(startpoint)):
            startpintcheck= False
        else:
            print ("Your input is not in the Graph .  Try again...")
    print ("")            
    print ("Topological sort from vertex ",startpoint," are:")
    print ("")
    print ("******************************************")
    print ("*\tReached\tVertexs  \t\t*")
    dfeGraph=DFSGraph()
    dfeGraph.deleteALL()
    for x in g:
        x.setColor('white')
        x.setPred(None)
        x.setDiscovery(0)
        x.setFinish(0)
    
    for j in g :
        dfeGraph.addVertex(j)
        if (j.getId()== startpoint):
            myVertex= j
    dfeGraph.dfs()
    dfeGraph.dfsvisit(myVertex)
    Visted_Vertexs=[]
    UNvisted_Vertexs=[]
    for v in g:
        if (v.getColor() == 'white'):
            UNvisted_Vertexs.append(v)
        else:
            Visted_Vertexs.append(v)
        
    Visted_Vertexs= bubbleSort(Visted_Vertexs)
    
    sys.stdout.write(str("*\t"))
    for i in Visted_Vertexs:
        sys.stdout.write(str(i.getId()))
    print ("\t\t\t\t*")
    print ("******************************************")
    print ("******************************************")
    print ("*\tUnreached\tVertexs\t\t*")
    sys.stdout.write(str("*\t"))
    for i in UNvisted_Vertexs:
        sys.stdout.write(str(i.getId()))
    print ("\t\t\t\t*")
    print ("******************************************")
""" this method performed algorithm bubble Sort in Vertex to ordered them in decreasing order"""
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i].getFinish() < alist[i+1].getFinish():
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

""" This method to display All pairs shortest path"""        
def All_pairs_shortest_path():
    NoGragh=True
    d={}
    if (d == g.vertices):
        print ("Empty Graph")
    else:
        NoGragh= False
    if(NoGragh):
        print ("No Graph has Added yat ..")
        return
    Vnumber=g.numVertices
    for r in g :
        r.setDistance(sys.maxsize)
    
    Matrix = [[0 for x in range(Vnumber)] for y in range(Vnumber)]
    row = 0
    colom = 0
    mylist=[]
    for j in g :
        myVertex= j
        dijkstra(g,myVertex)
        mylist.append(myVertex.getId())
        colom=0
        for v in g :
            Matrix[row][colom]=v.getDistance()
            colom=colom+1
        row=row+1
        for r in g :
            r.setDistance(sys.maxsize)
    
    for x in range (0,len (Matrix)):
        Matrix[x].insert(0,mylist[x])
    mylist.insert(0,0)
    Matrix.insert(0,mylist)
    
    print ("")
    print ("The shortest distances between all pairs of vertices in the graph : ")
    print ("")
    print ("**************************************************************************")
    for x in range (0,len (Matrix)):
        sys.stdout.write("*")
        for y in range (0,len (Matrix)):
            if (Matrix[x][y] == sys.maxsize):
                vlaue = "NO"
            else:
                vlaue =Matrix[x][y]
            sys.stdout.write("\t"+str(vlaue ))
        sys.stdout.write("\t*")
        print ("")
        print ("")
    print ("**************************************************************************")
""" This method to display Single source shortest path"""
def Single_source_shortest_path():
    NoGragh=True
    d={}
    if (d == g.vertices):
        print ("Empty Graph")
        NoGragh=True
    else:
        NoGragh= False
    if(NoGragh):
        print ("No Graph has Added yat ..")
        return
    for r in g :
        r.setDistance(sys.maxsize)
    startpintcheck=True
    
    while (startpintcheck):
        startpoint= input("Enter the start vertex: ")
        if (isitthere(startpoint)):
            startpintcheck= False
        else:
            print ("Your input is not in the Graph .  Try again...")
    print ("")            
    print ("The shortest paths from vertex ",startpoint," are:")
    print ("")
    print ("**************************")
    print ("*\tVertex\tDistance *")
    for j in g :
        if (j.getId()== startpoint):
            myVertex= j
    dijkstra(g,myVertex)
    for v in g :
        #if (v.getId() != myVertex.getId()):
        if (v.getDistance()== sys.maxsize):
            Distance="NO"
        else:
            Distance= v.getDistance()
        print ("*\t",v.getId(), "\t", Distance,"\t *")
    print ("**************************")
    print ("")
""" This method print weighted graph and return list of lists to draw the graph """
def Showweighted():
    newlist=[]
    alist=[]
    for v in g:
        for w in v.getConnections():
            var1= v.getId()+w.getId()
            var2= w.getId()+v.getId()
            if (var1 not in alist and var2 not in alist ):
                alist.append (var1)
                alist.append (var2)
                print(" %s - %s : " % (v.getId(), w.getId()),v.getWeight(w))
                newlist.append([v.getId(),w.getId(),v.getWeight(w)])
    return newlist
            
""" This method print directed graph and return list of lists to draw the graph"""    
def Showdirected():
    alist=[]
    for v in g:
        for w in v.getConnections():
            print (v.getId(),'>',w.getId(),':')
            alist.append([v.getId(),w.getId()])
    return alist
""" This method to determine is the graph directed graph or weighted graph"""
def isitdirected():
    for v in g:
        for w in v.getConnections():
            for x in w.getConnections():
                if (v.getId() == x.getId()):
                    return False
    return True
""" This method is started to display any graph """
def Viewgraph():
    NoGragh=True
    d={}
    if (d == g.vertices):
        print ("Empty Graph")
    else:
        NoGragh= False
    if(NoGragh):
        print ("No Graph has Added yat ..")
        return
    if (isitdirected()):
        alist=Showdirected()
        Drowdirected(alist)
    else:
        
        alist=Showweighted()
        Drowweighted(alist)
""" This method draw directed graph """
def Drowdirected(Matrix):
    mylist=[]
    for Level in Matrix:
        for index in range (0,len (Level)):
            if (Level[index] not in mylist):
                mylist.append(Level[index])  
    x=0
    y=0
    screen = Screen()
    turtle.clearscreen()
    Circle = "Circle.gif"
    screen.addshape(Circle)
    circle = Turtle()
    Arrow=Turtle()
    circle.shape(Circle)
    Arrow.shape()
    Arrow.penup()
    circle.penup()
  
    
    letterXYlist=[]
    XYlist=[]
    alist=mylist
    nlitters=len(alist)
    dgree= 360//nlitters
    for n in alist:
        circle.forward(280)
        circle.stamp()
        circle.write(n, True, align="center")
        String=str(circle.pos())
        String=String.replace("(","")
        String=String.replace(")","")
        XYlist=String.split(',')
        letterXYlist.append([n,XYlist[0],XYlist[1]])
        circle.forward(-280)
        circle.right(dgree)
    for line in Matrix:
        edge=line
        for L in letterXYlist:
            if (L[0]== edge[0]):
                Fx=float (L[1])
                Fy=float(L[2])
            if (L[0]== edge[1]):
                Sx=float(L[1])
                Sy=float(L[2])
        Arrow.setpos((Fx,Fy))
        Arrow.pendown()
        Arrow.setpos((Sx,Sy))
        Arrow.stamp()
        Arrow.penup()
    circle.hideturtle()
    return
""" This method draw weighted graph """
def Drowweighted(Matrix):
    mylist=[]
    for Level in Matrix:
        for index in range (0,len (Level)):
            if (Level[index] not in mylist):
                if (index == 1 or index == 0):
                    mylist.append(Level[index])               
    x=0
    y=0
    screen = Screen()
    turtle.clearscreen()
    Circle = "Circle.gif"
    screen.addshape(Circle)
    circle = Turtle()
    circle.shape(Circle)
    circle.penup()    
    letterXYlist=[]
    XYlist=[]
    alist=mylist
    nlitters=len(alist)
    dgree= 360//nlitters
    for n in alist:
        circle.forward(280)
        circle.stamp()
        circle.write(n, True, align="center")
        String=str(circle.pos())
        String=String.replace("(","")
        String=String.replace(")","")
        XYlist=String.split(',')
        letterXYlist.append([n,XYlist[0],XYlist[1]])
        circle.forward(-280)
        circle.right(dgree)
    #circle.hideturtle()
    for line in Matrix:
        edge=line
        for L in letterXYlist:
            if (L[0]== edge[0]):
                Fx=float (L[1])
                Fy=float(L[2])
            if (L[0]== edge[1]):
                Sx=float(L[1])
                Sy=float(L[2])
        circle.setpos((Fx,Fy))
        circle.pendown()
        circle.setpos((Sx,Sy))
        circle.penup()
        medx,medy=((Fx+Sx)/2),((Fy+Sy)/2)
        circle.setpos(medx,medy)
        circle.write(str (edge[2]), True, align="center")
    circle.hideturtle()
    return

""" Read graph from file"""
def fromafile(filename):
    g.deleteALL()
    addgraph=False
    readafile=False
    No_Gragh=True
    linelist=[]
    try:
        my_file = open(filename,'r')
        for line in my_file:
            linelist.append(line.replace('\n','' ))            
        readafile=True
        my_file.close()
    except IOError:
        print("Oops! (",filename,") the file  not found .  Try again...")

    if (readafile):
        for chosen in linelist:
            chosen=buledSentaxt(chosen)
            if(chosen == ""):
                Next=False
            elif (checkInput(chosen)):
                No_Gragh=False
                addgraph=True
                alist=[]
                letters= chosen.split(' ')
                weighte=eval(letters[1])
                for n in letters[0]:
                    alist.append(n)
                ##### chick for dircted graph here -----------
                if (isitthere(alist[0])):
                    YES=0
                else:
                    g.addVertex(alist[0])
                if (isitthere(alist[2])):
                    YES=0
                else:
                    g.addVertex(alist[2])
                g.addEdge(alist[0],alist[2],weighte)
                if (alist[1]== '-'):
                    g.addEdge(alist[2],alist[0],weighte)
                    
            
        
    return addgraph
""" This method to complete syntax example from A>B to A>B: 99"""
def buledSentaxt(VSstring):
    alist=[]
    try:
        letters= VSstring.split(' ')
        weighted=eval(letters[1])
        for n in letters[0]:
            alist.append(n)
        
        if (alist[0].isalpha() and alist[2].isalpha() and (alist[1]== '-' or alist[1]== '>') and alist[3]== ':'):
            return VSstring
        else:
            return VSstring
    
    except ValueError:
        VSstring=VSstring+":"+str(sys.maxsize)
        return VSstring
    except IndexError:
        VSstring=VSstring+": "+str(sys.maxsize)
        return VSstring
"""This method to check Input """    
def checkInput(VSstring):
    alist=[]
    try:
        letters= VSstring.split(' ')
        weighted=eval(letters[1])
        for n in letters[0]:
            alist.append(n)
        
        if (alist[0].isalpha() and alist[2].isalpha() and (alist[1]== '-' or alist[1]== '>') and alist[3]== ':'):
            return True
        else:
            print("Oops! (",VSstring,")  That was not valid Syntax 4.  Try again...")
            return False
    
    except ValueError:
        print("Oops! (",VSstring,")  That was not valid Syntax 5.  Try again...")
        return False
    except IndexError:
        print("Oops! (",VSstring,")  That was not valid Syntax 6.  Try again...")
        return False
""" This method to determine if vertex is in the graph or not"""        
def isitthere(VName):
    chick= False
    for i in g:
        if (i.getId() == VName):
            chick= True
    return chick
""" This method read graph from keyboard """    
def fromthekeyboard():
    g.deleteALL()
    No_Gragh=True
    Next=True
    while (Next):
        chosen = input("Enter an edge or return to quit: ")
        if(chosen == ""):
            Next=False
            if(No_Gragh):
                print ("No Gragh has added yat..")
            else:
                print("Graph created successfully")
        elif (checkInput(chosen)):
            No_Gragh=False
            alist=[]
            letters= chosen.split(' ')
            weighte=eval(letters[1])
            for n in letters[0]:
                alist.append(n)
            ##### chick for dircted graph here -----------
            if (isitthere(alist[0])):
                YES=0
            else:
                g.addVertex(alist[0])
            if (isitthere(alist[2])):
                YES=0
            else:
                g.addVertex(alist[2])
            g.addEdge(alist[0],alist[2],weighte)
            if (alist[1]== '-'):
                g.addEdge(alist[2],alist[0],weighte)
"""  This is the main method that create user interface and interact with users """
def Alanazi4():
    program = True
    while(program):
        print ("Main Menu")
        print (" 1 Input a graph from the keyboard")
        print (" 2 Input a graph from a file")
        print (" 3 View graph")
        print (" 4 Single-source shortest path")
        print (" 5 All-pairs shortest path")
        print (" 6 Topological sort")
        print (" 7 Exit the program")
        chose = input("Enter your selection[1-7]: ")
        print("")
        if (chose=="1"):
            fromthekeyboard()
        elif (chose=="2"):
            file = input("Enter a file name : ")
            if(fromafile(file)):
                print("Graph created successfully")
            else:
                print ("No Gragh has added yat..")
        elif (chose=="3"):
            Viewgraph()
        elif (chose=="4"):
            Single_source_shortest_path()
        elif (chose=="5"):
            All_pairs_shortest_path()
        elif (chose=="6"):
            Topological_sort()
        elif (chose=="7"):
            print("Good bye.")
            program = False
        else:
            print("Wrong choice")
        
        
""" Those are global variables one for a graph and second for check if there is a graph or not """    
No_Gragh= True
g = Graph()
Alanazi4()
