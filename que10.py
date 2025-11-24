#Check if the String is Palindrome or not


#this is using recursion  TC = O(n) SC = O(n)
name = "nitin"

# def pali(str,left,right):
#     if left>=right:
#         return True
#     if str[left] != str[right]:
#         return False
#     return pali(str,left+1,right-1)

# x = pali(name,0,len(name)-1)
# print(x)


#this is using loop  TC= O(n) SC = O(1)
# def pali():
#     n = len(name)
#     left = 0
#     right = n-1
#     while left<right:
#         if name[left] != name[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# x= pali()
# print(x)