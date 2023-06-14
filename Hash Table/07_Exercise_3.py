# Find the first non-repeating character from the given string
def find_unique(str):
    dict1 = {}
    l1 =[]
    for i in str:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] = dict1[i] + 1
    
    for key, values in dict1.items():
        if values == 1:
            l1.append(key)
            break
    if len(l1)==0:
        return None
    return l1


str = 'aabbcc'
str1 = list(str)
print(find_unique(str1))