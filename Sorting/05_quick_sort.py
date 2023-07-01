def swap(mylist,index1,index2):
    temp = mylist[index1]
    mylist[index1] = mylist[index2]
    mylist[index2] = temp


def pivot(mylist,pivot_index,end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1,end_index+1):
        if mylist[i] < mylist[pivot_index]:
            swap_index+=1
            swap(mylist,swap_index,i)
    swap(mylist,pivot_index,swap_index)
    return swap_index


def quick_sort(mylist,left,right):
    if left<right:
        pivot_index = pivot(mylist,left,right)
        quick_sort(mylist,left,pivot_index-1)
        quick_sort(mylist,pivot_index+1,right)
    return mylist

my_list = [4,6,1,7,5,3,2]

print(quick_sort(my_list,0,len(my_list)-1))