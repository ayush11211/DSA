#Print all the Factors on Given Number
from math import sqrt
#Aproach1 Brute force solution
#cheching that the number is divisible with number till n then all those are the factors  
# TC = O(n)  SC = O(k) whew k is the number of factors

# n = 20
# result = []
# for i in range(1,n+1):
#     if n % i == 0:
#         result.append(i)
# print(result)

#Aproach 2 better solution
# in this aproach we check till n/2 only because we found the after 
# that no number is divisible with the input number except the number it self TC = O(n)   SC = O(k)

# n = 20
# result = []
# for i in range(1, n//2 + 1):
#     if n % i == 0:
#         result.append(i)
# result.append(n)
# print(result)

#Aproach 3 Optimal Solution
# in this we use square root of the number to make it more optimal ((((n/i) hint)))

n = 20
result = []
for i in range(1, int(sqrt(n))+ 1):
    if n % i == 0:
        result.append(i)
        if n//i != i:
            result.append(n//i)
result.sort()
print(result)




