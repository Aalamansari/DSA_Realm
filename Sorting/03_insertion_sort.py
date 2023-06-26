def insertion_sort(mylist):
    for i in range(1,len(mylist)):
        temp = mylist[i]
        j = i-1
        while temp<mylist[j] and j>-1:
            mylist[j+1] = mylist[j]
            mylist[j] = temp
            j-=1
    return mylist


print(insertion_sort([4,2,1,6,7]))