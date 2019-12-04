
DirectedFile = open("DirectedEx.txt","r")
for line in DirectedFile:
    print(line,sep='',end='')
DirectedFile.close()
print("---------------------------------------")
UndirectedFile = open("UndirectedEx.txt","r")
for line in UndirectedFile:
    print(line,sep='',end='')
UndirectedFile.close()

