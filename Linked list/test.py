nums = [5,3,1,1,1,3,73,1]
result = []
k=1
hashmap = {}
for i in nums:
    if i not in hashmap:
        hashmap[i] = 1
    else:
        hashmap[i]+=1
    
for key,values in hashmap.items():
    if values>1 and len(result)!=k:
        result.append(key)

for key,values in hashmap.items():
    if values==1 and len(result)!=k:
        result.append(key)

print(result)
print(hashmap)
