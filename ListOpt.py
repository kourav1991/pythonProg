
Alist = []

#append
Alist.append(10)
Alist.append(20)
Alist.append(30)

#entend
Alist.extend([90,20,45,32,645,32,90,65,23])

#unique list
UniqList = list(set(Alist))

#Remove last element
#UniqList.pop()

#Sort
UniqList.sort(reverse=True)
print ('List of sorted element ' , UniqList)

#Conversion List to tuple
atuple = tuple(UniqList)

print ('List to tuple ' ,UniqList)
