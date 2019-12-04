""" This function (chracterencode) to encode the chracters in the phrase """
def chracterencode(phrase,key_value):
    mychracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    mydigits ="0123456789"
    Encodephrase =""
    mychractereslist = list(mychracteres)
    Encodechar=""
     
    for i in phrase:
        if i in mychracteres:
            for index in range(0,len(mychractereslist)):
                if (i == mychractereslist[index]):
                    Encodeindexchar = index + key_value
                    if (Encodeindexchar < len(mychractereslist) ):
                        Encodephrase = Encodephrase + mychractereslist[Encodeindexchar ]
                    else:
                        Encodeindexchar = Encodeindexchar -  len(mychractereslist)
                        Encodephrase = Encodephrase + mychractereslist[Encodeindexchar ]
        elif i in mydigits:
            Encodephrase = Encodephrase +digitencode(i)
    return Encodephrase

""" This function (digitencode) to encode the Digits"""
def digitencode(mydigit):
    myDigitDictionary={}
    my_file = open("digitencode.txt", "r+")
    for line in my_file:
        k, v = line.strip().split(' ')
        myDigitDictionary[k.strip()] = v.strip()
    my_file.close()
    return myDigitDictionary[mydigit]

""" This function (chracterDecode) to Decode the chracters in the phrase """
def chracterDecode(phrase,key_value):
    mychracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    mydigits ="$(%{-:!@=^"
    Decodephrase =""
    mychractereslist = list(mychracteres)
    
     
    for i in phrase:
        if i in mychracteres:
            for index in range(0,len(mychractereslist)):
                if (i == mychractereslist[index]):
                    Decodeindexchar = index - key_value
                    if (Decodeindexchar >= 0 ):
                        Decodephrase = Decodephrase + mychractereslist[Decodeindexchar ]
                    else:
                        Decodeindexchar = Decodeindexchar +  len(mychractereslist)
                        Decodephrase = Decodephrase + mychractereslist[Decodeindexchar ]
        else:
            Decodephrase = Decodephrase +digitDecode(i)
    return Decodephrase

""" This function (digitDecode) to decode the Symbols to digit"""
def digitDecode(mydigit):
    myDigitDictionary={}
    my_file = open("digitencode.txt", "r+")
    for line in my_file:
        k, v = line.strip().split(' ')
        myDigitDictionary[v.strip()] = k.strip()
    my_file.close()
    return myDigitDictionary[mydigit]
    
""" This function  (ISacceptable) to check if the phrase is is acceptable or not """
def ISacceptable(words_list):
    for i in words_list:
        if ( i.isnumeric() or i.isalpha()):
            myboolean = True
        else:
            return False
    return myboolean
""" First we need to check the user input if it is valid or not """
while True:
        phrase = input ("Enter a phrase: ")
        if (phrase != ""):
            break
        else:
            print ("Oops!  That was not a valid phrase.  Try again...")            
        
while True:
    try:
        key_value =int( input ("Enter the key value: "))
        break
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")
while True:
    try:
        EncodeOrDecode= int (input("Type 0 if you would like to Encode,or 1 if you would like to Decode : "))
        if (EncodeOrDecode == 1 or EncodeOrDecode == 0):
            break
        else:
            print ("Oops!  That was not 0 or 1 .  Try again...")
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")

words_list= phrase.split (' ')

if (EncodeOrDecode == 0):
    if ISacceptable(words_list):
        print ("\nYour encoded message is:")
        print (chracterencode(phrase,key_value))
    else:
        print ( " Your phrase is NOT acceptable")
else:
    print ("\nYour decoded message is:")
    print (chracterDecode(phrase,key_value))

    
