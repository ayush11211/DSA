#Hashing in Python 3 questions

#Que1  TC = O(n + m)  SC = O(1) using list
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# hash_list = [0] * 11
# for num in n:
#     hash_list[num] += 1
# for num in m:
#     if num < 1 or num > 10:
#         print("0")
#     else:
#         print(hash_list[num])

#Same Que using dictionary and .get method

# freq_map = dict()
# for nums in n:
#     freq_map[nums] = freq_map.get(nums,0)+1
# for nums in m:
#     if nums < 1 or nums > 10:
#         print("0")
#     else:
#         print(freq_map.get(nums,0))




#Que 2 Character Hashing Same above Que using list  TC = O(n + M) SC = O(1)
s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

# hash_list = [0] * 26
# for num in s:
#     ascii_val = ord(num)
#     index = ascii_val - 97
#     hash_list[index]+=1
# for num in q:
#     ascii_val = ord(num)
#     index = ascii_val - 97
#     print(hash_list[index])


# This can be solved using Dictionary also
freq_map = dict()
for num in s:
    freq_map[num] = freq_map.get(num,0)+1
for num in q:
    print(freq_map.get(num,0))