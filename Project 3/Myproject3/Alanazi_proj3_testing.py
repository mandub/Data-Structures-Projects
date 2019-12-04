from BinaryTree import BinaryTree
from queue import Queue
import sys
####################################################################################################
def Print_out_tree(T):
    thislevel = [T]
    print ( "Root : ",T.getRootVal())
    while thislevel:
        nextlevel = list()
        for n in thislevel:
            if (n.getLeftChild() != None ):
                nextlevel.append(n.getLeftChild())
                sys.stdout.write(" this is left :" + str(n.getLeftChild().getRootVal())+ " of " + str(n.getRootVal()))
            if (n.getRightChild() != None ):
                nextlevel.append(n.getRightChild())
                sys.stdout.write(" this is Right :" + str(n.getRightChild().getRootVal())+ " of " + str(n.getRootVal()))    
        print ("")
        thislevel = nextlevel
    print (" - - - - - - - - - - - - - - - - - - - - ")
        
def Print_out_each_tree(T):
    thislevel = [T]
    spaces=[]
    leve =1
    a = '                                                                '
    while thislevel:
        nextlevel = list()
        a = a[: int ((len(a)/2))]
        for n in thislevel:
            if (len(spaces) > 0 ):
                b = spaces.pop(0)
                sys.stdout.write(b)
            sys.stdout.write(a+str(n.getRootVal()) +a)
            if (n.getLeftChild() != None ):
                nextlevel.append(n.getLeftChild())
            if (n.getRightChild() != None ):
                nextlevel.append(n.getRightChild())
                if (n.getLeftChild() == None ):
                    spaces.append(a)
                    
               
        print ("")
        thislevel = nextlevel
        leve= leve+1


###################################################################################################
def Decode_by_Tree(T,codeString):
    space='$'
    temp = BinaryTree(space)
    temp = T
    print (codeString)
    phraseString=""
    check=True
    Decode_phrase_list=[]
    Decode_phrase_list.append(phraseString)
    Decode_phrase_list.append(check)
    codeStringlist=[]
    for n in codeString:
        codeStringlist.append(n)
    foundchar= False
    while (check and (len (codeStringlist) > 0)):
        digit = codeStringlist.pop(0)
        if (digit == '0'):
            print("Go Left")
            if (temp.getLeftChild() != None ):
                if (temp.getLeftChild().getRootVal()== space):
                    temp = temp.getLeftChild()
                    if ((len (codeStringlist) == 0)):
                        check = False
                        print (" Erorr _________________Left_______(len (codeStringlist) == 0)________________",temp.getRootVal())
                        
                        
                else:
                    print (temp.getLeftChild().getRootVal())
                    phraseString = phraseString + temp.getLeftChild().getRootVal()
                    print (phraseString)
                    temp = T
            else:
                check = False
                print (" Erorr _________________Left_______________________",temp.getRootVal())
        else:
            if(digit == '1'):
                print("Go Right")
                if (temp.getRightChild() != None ):
                    if (temp.getRightChild().getRootVal()== space):
                        temp = temp.getRightChild()
                        if ((len (codeStringlist) == 0)):
                            check = False
                            print (" Erorr _________________Right_______(len (codeStringlist) == 0)________________",temp.getRootVal())
                    else:
                        print (temp.getRightChild().getRootVal())
                        phraseString = phraseString + temp.getRightChild().getRootVal()
                        print (phraseString)
                        temp = T
                else:
                    check = False
                    print (" Erorr ___________________Right_____________________",temp.getRootVal())
                    
    Decode_phrase_list[0]= phraseString
    Decode_phrase_list[1]= check
    return Decode_phrase_list
def Encode_by_Tree(charcodelist):
    space='$'
    myTree_check_list=[]
    mytree = BinaryTree(space)
    check=True
    myTree_check_list.append(mytree)
    myTree_check_list.append(check)
    print (myTree_check_list)
    for i in range (0,len (charcodelist)-1):
        print ("#####################################")
        if (not check):
            break
        line = charcodelist[i]
        mychar = line[0]
        mycode = line[1]
        mycode=mycode+mychar
        temp = BinaryTree(space)
        temp = mytree
        for digit in range (0,len (mycode)-1):
            if (digit == (len (mycode) -2)):
                digit=digit+1
                
            print ("-----------------------------------")
            if (mycode[digit] == '0'):
                print ("Go left")
                if (temp.getLeftChild()== None):
                    print("Add Left")
                    temp.insertLeft(space)
                    temp = temp.getLeftChild()
                else:
                    if(temp.getLeftChild().getRootVal()== space):
                        print ("just go left ")
                        temp = temp.getLeftChild()
                    else:
                        check= False
                        print (" Erorr ______on going left________________________________________",mycode[len (mycode)-1])
                        break
                        
            else :
                if (mycode[digit] == '1'):
                    print ("Go Right")
                    if (temp.getRightChild()== None):
                        print("Add Right")
                        temp.insertRight(space)
                        temp = temp.getRightChild()
                    else:
                        if (temp.getRightChild().getRootVal()== space):
                            print ("just go Right")
                            temp = temp.getRightChild()
                        else:
                            check= False
                            print (" Erorr ______on going Right________________________________________",mycode[len (mycode)-1])
                            break
                            
                else:
                    if  (mycode[len(mycode)-2] == '0'):
                        try:
                            if (temp.getLeftChild().getRootVal() != None):
                                check= False
                                print (" Erorr ______on Adding Left ________________________________________",mycode[len (mycode)-1])
                                break
                        except AttributeError:
                                temp.insertLeft(mycode[digit])
                                print ("Adding to the left of the tree ",mycode[digit])
                    if  (mycode[len(mycode)-2] == '1'):
                        try:
                            if (temp.getRightChild().getRootVal() != None):
                                check= False
                                print (" Erorr ______on Adding Right ________________________________________",mycode[len (mycode)-1])
                                break
                        except AttributeError:
                            temp.insertRight(mycode[digit])
                            print ("Adding to the Right of the tree ",mycode[digit])

        print (charcodelist[i])
    myTree_check_list[0] = mytree
    myTree_check_list[1] = check
    return myTree_check_list
""" This function to read File and return list of listes that have characters code and decoding of the message"""
def readfile(file):
    linelist=[]
    charcodelist=[]
    charcode=[]
    index=0
    try:
        my_file = open(file, "r+")
        for line in my_file:
            linelist.append(line)
        my_file.close()
    except IOError:
        print ("Oops! There is a problem with opening the file ")
    for n in range (0,len(linelist)-2 ):
        charcodelist=linelist[n].split()
        charcode.append(charcodelist)
    charcodelist=linelist[len(linelist)-1].split()
    charcode.append(charcodelist)
    return charcode
def Alanazi_proj3_testing(file):
    myTree_check_list=[]
    mytree = BinaryTree(" ")
    Decode_phrase_list=[]
    check=True
    myTree_check_list.append(mytree)
    myTree_check_list.append(check)
    Decode_phrase_list.append("")
    Decode_phrase_list.append(check)
    charcodelist=readfile(file)
    myTree_check_list = Encode_by_Tree(charcodelist)
    if (myTree_check_list[1]):
        print (myTree_check_list)
        Decode_phrase_list = Decode_by_Tree(myTree_check_list[0],charcodelist[len(charcodelist)-1][0])
        if (Decode_phrase_list[1]):
            print (Decode_phrase_list)
            Print_out_each_tree(myTree_check_list[0])
            print ("Success : ",Decode_phrase_list[0])
            print ("Number of bits = ",len(charcodelist[len(charcodelist)-1][0])  )
            print ("Number of characters = ",len(Decode_phrase_list[0]))
            #print ("Compression ratio = ",((len(charcodelist[len(charcodelist)-1][0] ) )/ (len(Decode_phrase_list[0])*8)) * 100, "%")
        else:
            print ("Error : cannot decode message")
    else :
        print ("Error : not a valid code")
    
    

    
Alanazi_proj3_testing("test1.txt")# to check for (project case 1)
Alanazi_proj3_testing("test2.txt")# to check for (project case 2)
#Alanazi_proj3_testing("test3.txt")# to check for (project case 3)
#Alanazi_proj3_testing("test4.txt")# to check for (project case 4)
#Alanazi_proj3_testing("test5.txt")# to check for (Success : )
#Alanazi_proj3_testing("test6.txt")# to check for (Error : cannot decode message)
#Alanazi_proj3_testing("test7.txt")# to check for (Error : not a valid code)
#Alanazi_proj3_testing("test8.txt")# to check for (Error : not a valid code) 2 Letters have the same code
Alanazi_proj3_testing("test9.txt")# to check for (Error : not a valid code) encoded code less than Letters code

#GenerateTest.GenerateTest("<Letters>","<Phrase>")




