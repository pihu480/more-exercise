list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
a=[]
while i<len(list1):
    if (list2,list1[i]) not in (list2,list1):
        a.append(list1[i])
    i=i+1
print(a)