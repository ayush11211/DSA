# Reverse an array using recursion  TC = O(n) SC = O(n)
nums = [5,7,3,2,6,1,5,9]

def rev(n,left,right):
    if left >= right:
        return n
    n[left],n[right] = n[right],n[left]
    return rev(n,left+1,right-1)

revers = rev(nums,0,len(nums)-1)
print(revers)
