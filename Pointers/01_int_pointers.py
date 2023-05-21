# Integers are immutable 

num1 = 1
num2 = num1

print('value of num1: ',num1)
print('value of num2: ',num2)

print('num1 pointing to address: ',id(num1))
print('num2 pointing to address: ',id(num2))

num2 = 2

print('value of num1: ',num1)
print('value of num2: ',num2)

print('num1 pointing to address: ',id(num1))
print('num2 pointing to address: ',id(num2))

