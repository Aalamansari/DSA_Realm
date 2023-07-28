def sumofDigits(n):
    if n==0:
        return 0
    else:
        return int(n%10) + sumofDigits(n/10)

print(sumofDigits(112))