# Dictionaries are mutable

dict1 = {'value':11}
dict2 = dict1

print('value of dict1: ',dict1['value'])
print('value of dict2: ',dict2['value'])

print('dict1 pointing to address: ',id(dict1))
print('dict2 pointing to address: ',id(dict2))

dict2['value'] = 12

print('value of dict1: ',dict1['value'])
print('value of dict2: ',dict2['value'])

print('dict1 pointing to address: ',id(dict1))
print('dict2 pointing to address: ',id(dict2))