""" Almandub Alanazi """
""" this function to print the top 10 frequency words"""
def mostfrequentwords(words):
    myDictionary={}
    top10words =[]
    for word in words:
        if word in myDictionary:
            myDictionary[word] +=1
        else:
            myDictionary[word] =1
    for key in myDictionary:
        top10words.append([myDictionary[key], key])
    top10words.sort()
    top10words.reverse()
    if (len(top10words)<10):
        printnumber = len(top10words)
    else:
        printnumber = 10
    for i in range (0,printnumber):
        if i == 9 :
            print ( i+1,".  ", " ".join(str(x) for x in top10words[i]))
            
        else:
            print ("", i+1,".  ", " ".join(str(x) for x in top10words[i]))
def filestats_alanazi(my_file_name):
    """ definitions for my counters and lists"""
    words =[]
    mystringlist=[]
    wordscounter=0
    lines =0
    characters =0
    mychracteres = "abcdefghijklmnopqrstuvwxyz'-"
     

    """ read from a file and count the lines and the chracteres"""
    try:
        my_file = open(my_file_name, "r+")
        for line in my_file:
            lines += 1
            mystringlist += line.split()
            characters += len(line)
        my_file.close()
    except IOError:
        print ("Oops! There is a problem with opening the file ")

    """ to decide what string is a word  """
    for mystring in mystringlist:
        inmystring =""
        for char in mystring:
            lowerchar = char.lower()
            if lowerchar in mychracteres:
                inmystring = inmystring + lowerchar
        if inmystring != "" and inmystring != "--" and inmystring != "-" :
            if len (inmystring)==1:
                if inmystring == "a" or inmystring == "i":
                    words.append(inmystring)
                    wordscounter +=1
            else:
                words.append(inmystring)
                wordscounter +=1
    """ printing the results"""
    print ("The file '",my_file_name,"' has:")
    print ("    ",characters," characters")
    print ("    ",lines," lines")
    print ("    ",wordscounter," words")
    print ("")
    print ("The top 10 most frequent words are:")
    mostfrequentwords(words)   

