#Find the factorial of a number using recursion TC = O(n) SC = O(n)
n = 5
def func(n):
    if n == 0 or n == 1:
        return 1
    return n * func(n-1)

x = func(n)
print(x)