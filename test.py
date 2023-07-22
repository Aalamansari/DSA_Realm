# num = [1,2,3,4,5]

# max_sum = 0
# for i in range(0,len(num)):
#     sum = 0
#     for j in range(i,len(num)):
#         sum = sum + num[j]
#         if sum>max_sum:
#             max_sum = sum

# print(max_sum)  

###############################################################

# num = [1,1,2,2,3,4]

# a = 0
# b = 1
# count = 0
# while b<len(num):
#     if num[a]!=num[b]:
#         a+=1
#         num[a]=num[b]
#         count+=1
#         b+=1
#     else:
#         b+=1

# print(num)  
# print(count+1)


# l1 = [1,1,2,2,3,4]
# mylen = 1
# a = 0
# b = 1
# while b < len(l1):
#     if l1[a] == l1[b]:
#         b +=1
#     else:
#         a +=1
#         l1[a] = l1[b]
#         mylen +=1


# print(l1)
# print(mylen)



# str1 = "1,2,3,4"

# str1 = str1.split(',')
# str1.pop(0)
# str1.pop(-1)
# str1 = ' '.join(str1)

# print(str1)

# nums = [10,4,8,3]
# right = []
# left = [0]
# ans = []

# for i in range(1,len(nums)):
#     right.append(sum(nums[i:]))
#     left.append(sum(nums[0:i]))

# right.append(0)


# for i in range(len(right)):
#     ans.append(abs(left[i]-right[i]))

# print(left)
# print(right)
# print((ans))



num = [0,1,2,2,3,0,4,2]
val = 2

a = 0
b = 0
count = 0
while a<len(num):
    if num[a]!=val:
        num[b]=num[a]
        count+=1
        b+=1
        a+=1
    else:
        a+=1

print(num)  
print(count)