
alist = ["google.com","unix.com","facebook.com","google.com","linkedin.com"]
lenlist = []
print ("Unique element of list : ", list(set(alist)))
alist = list(set(alist))
for val in alist :
    #print (len(val))
    lenlist.append(len(val))


print(lenlist)

