from BinaryTree import BinaryTree
from queue import Queue
import sys
""" this function to build the tree for decoding """
def Decode_by_Tree(T,codeString):
    space=' '
    temp = BinaryTree(space)
    temp = T
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
            if (temp.getLeftChild() != None ):
                if (temp.getLeftChild().getRootVal()== space):
                    temp = temp.getLeftChild()
                    if ((len (codeStringlist) == 0)):
                        check = False                        
                        
                else:
                    phraseString = phraseString + temp.getLeftChild().getRootVal()
                    temp = T
            else:
                check = False
        else:
            if(digit == '1'):
                if (temp.getRightChild() != None ):
                    if (temp.getRightChild().getRootVal()== space):
                        temp = temp.getRightChild()
                        if ((len (codeStringlist) == 0)):
                            check = False
                    else:
                        phraseString = phraseString + temp.getRightChild().getRootVal()
                        temp = T
                else:
                    check = False
                    
    Decode_phrase_list[0]= phraseString
    Decode_phrase_list[1]= check
    return Decode_phrase_list
""" this function to build the tree for encoding """
def Encode_by_Tree(charcodelist):
    space=' '
    myTree_check_list=[]
    mytree = BinaryTree(space)
    check=True
    myTree_check_list.append(mytree)
    myTree_check_list.append(check)
    for i in range (0,len (charcodelist)-1):
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
                
            if (mycode[digit] == '0'):
                if (temp.getLeftChild()== None):
                    temp.insertLeft(space)
                    temp = temp.getLeftChild()
                else:
                    if(temp.getLeftChild().getRootVal()== space):
                        temp = temp.getLeftChild()
                    else:
                        check= False
                        break
                        
            else :
                if (mycode[digit] == '1'):
                    if (temp.getRightChild()== None):
                        temp.insertRight(space)
                        temp = temp.getRightChild()
                    else:
                        if (temp.getRightChild().getRootVal()== space):
                            temp = temp.getRightChild()
                        else:
                            check= False
                            break
                            
                else:
                    if  (mycode[len(mycode)-2] == '0'):
                        try:
                            if (temp.getLeftChild().getRootVal() != None):
                                check= False
                                break
                        except AttributeError:
                                temp.insertLeft(mycode[digit])
                    if  (mycode[len(mycode)-2] == '1'):
                        try:
                            if (temp.getRightChild().getRootVal() != None):
                                check= False
                                break
                        except AttributeError:
                            temp.insertRight(mycode[digit])

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
""" this is the main function"""
def Alanazi_BnCode(file):
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
        Decode_phrase_list = Decode_by_Tree(myTree_check_list[0],charcodelist[len(charcodelist)-1][0])
        if (Decode_phrase_list[1]):
            print ("Success : ",Decode_phrase_list[0])
            print ("Number of bits = ",len(charcodelist[len(charcodelist)-1][0])  )
            print ("Number of characters = ",len(Decode_phrase_list[0]))
            #print ("Compression ratio = ",((len(charcodelist[len(charcodelist)-1][0] ) )/ (len(Decode_phrase_list[0])*8)) * 100, "%")
        else:
            print ("Error : cannot decode message")
    else :
        print ("Error : not a valid code")
    
    

    
#Alanazi_BnCode("test1.txt")# to check for (project case 1)
#Alanazi_BnCode("test2.txt")# to check for (project case 2)
#Alanazi_BnCode("test3.txt")# to check for (project case 3)
#Alanazi_BnCode("test4.txt")# to check for (project case 4)
#Alanazi_BnCode("test5.txt")# to check for (Success : )
#Alanazi_BnCode("test6.txt")# to check for (Error : cannot decode message)
#Alanazi_BnCode("test7.txt")# to check for (Error : not a valid code)
#Alanazi_BnCode("test8.txt")# to check for (Error : not a valid code) 2 Letters have the same code
#Alanazi_BnCode("test9.txt")# to check for (Error : not a valid code) encoded code less than Letters code





