# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def append(self,value):
#         new_node = Node(value)
#         if self.length==0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length+=1
#         return True

#     def print(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
    
    
#     def insert(self,index,value):
#         if index<0 or index>self.length:
#             return False
#         if index==0:
#             return self.prepend(value)
#         if index==self.length:
#             return self.append(value)
#         new_node = Node(value)
#         temp = self.get(index-1)
#         new_node.next = temp.next
#         temp.next = new_node
#         self.length=+1
#         return True

#     def remove(self,index):
#         if index<0 or index>=self.length:
#             return None
#         if index==0:
#             return self.popfirst()
#         if index==self.length-1:
#             return self.pop()
#         prev = self.get(index-1)
#         temp = prev.next
#         prev.next = temp.next
#         temp.next=None
#         self.length-=1
#         return temp
 
#     def reverse(self):
#         if self.length == 0:
#             return False
#         else:
#             temp = self.head
#             self.head = self.tail
#             self.tail = temp
            
#             before = None
#             for _ in range(self.length):
#                 after = temp.next
#                 temp.next = before
#                 temp.prev = after
#                 before = temp
#                 temp = after
#         return True
    
#     def reverse_between(self,m,n):
#         if self.length==0 or self.length==1:
#             return None
#         before  = self.head
#         p1 = self.head
#         for _ in range(m):
#             before = before.next
        

#         temp = before.next

#         for _ in range(m-1):
#             p1 = p1.next

#         p2 = self.head
#         for _ in range(m):
#             p2 = p2.next

#         p3 = self.head
#         for _ in range(n+1):
#             p3 = p3.next


#         for _ in range(n-m):  
#             if temp!=None:
#                 after = temp.next
#                 temp.next = before
#                 before = temp
#                 temp = after

        
#         p1.next = before  
        
#         if p3==None:
#             p2.next = None
#         else:
#             p2.next = p3
            

        



# myList = LinkedList(1)
# myList.append(2)
# myList.append(3)
# myList.append(4)
# myList.append(5)
# myList.append(6)
# myList.append(7)
# myList.append(8)
# myList.append(9)
# myList.reverse_between(2,4)
# myList.print()

###########################################################

# mylist = []
# for i in range(5):
#     mylist.append(i)

# print(mylist)


# print([i for i in range(5)])

##########################################################

# for i in range(5):
#     if i%2==0:
#         mylist.append(i)

# print(mylist)

# print([i for i in range(5) if i%2==0])

#########################################################


# for i in range(5):
#     if i%2==0:
#         mylist.append('Even')
#     else:
#         mylist.append('Odd')

# print(mylist)


# print([f'Even:{i}' if i%2==0 else f'odd:{i}' for i in range(5)])

########################################################

# s = "MCMXCIV"
# mydict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# sum = 0
# i=0 
# while i<len(s):
#     if s[i]=='I' or s[i]=='X' or s[i]=='C':
#         if i!=len(s)-1 and s[i]+s[i+1] in mydict:
#             sum+=mydict[s[i]+s[i+1]]
#             i+=2
#         else:
#             sum+=mydict[s[i]]
#             i+=1
#     else:
#         sum+=mydict[s[i]]
#         i+=1

# print(sum)




# mydict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

# s = "RLRRLLRLRL"
# test_count = 0
# real_count = 0
# i=0

# while i<len(s):
#     if s[i] =='R':
#         test_count+=1
#     else:
#         test_count-=1
#     i+=1    
#     if test_count==0:
#         real_count+=1 
    
# print(real_count)
    

###############################################################

nums = [1,15,6,3]
# new_nums = []
# dig_sum = 0

# for i in nums:
#     new_nums.append(i)

# for i in range(len(nums)):
#     if nums[i]>=10:
#         new_str= str(nums[i])
#         new_str = list(new_str)               
#         nums+=new_str

# for i in nums:
#     if int(i)<10:
#         dig_sum+=int(i)

# print(sum(new_nums)-dig_sum)

# dig_sum =0
# for i in nums:
#     if i >9:
#         while i!=0:
#             last = i%10
#             dig_sum += last
#             i = i//10
#     else:
#         dig_sum += i

# print(dig_sum)


def print2(n):
    if n<1:
        return print('The value of n is 0')
    else:
        return print2(n-1)
        print2(n)

print2(4)