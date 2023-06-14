#how to find duplicates in a given list using a dictionary

def find_duplicates(nums):
    dict1 = {}
    l1 =[]
    for i in nums:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] = dict1[i] + 1
    
    for key, values in dict1.items():
        if values > 1:
            l1.append(key)
    return l1


print(find_duplicates([1,1,2,2,3]))