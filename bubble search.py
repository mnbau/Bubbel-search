def bubble(l):
    for i in range (len(l)):
        for j in range (0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
l = [2,5,4,8,9,98,3,1]
print (bubble(l))