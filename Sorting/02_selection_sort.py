def selection_sort(mylist):
    for i in range(len(mylist)-1):
        min_index = i
        for j in range(i+1,len(mylist)):
            if mylist[min_index]>mylist[j]:
                min_index = j
        if i!=min_index:
            temp = mylist[i]
            mylist[i] = mylist[min_index]
            mylist[min_index] = temp
    return mylist
        
print(selection_sort([4,2,1,7,6]))
            