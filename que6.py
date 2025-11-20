#Store frequency in dictionary

nums = [5,6,7,7,1,9,111,1,1,5,1,1]
x = 1
#Method 1 TC = O(n)  SC = O(n) Frequency map used
# freq_map = dict()
# for i in range(0,len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]]+=1
#     else:
#         freq_map[nums[i]]=1
# print(freq_map[x])

#method 2 Hash map used
hash_map = dict()
n = len(nums)
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1  #.get method is it checks if the key is present om the dictionary or not and if it is not
                                                   #present then it by default returns 0 and if it exists then it will return its value
print(hash_map[x])
