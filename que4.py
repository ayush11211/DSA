# Armstrong Number

# An Armstrong number is a number which says that, if every digit of a number has a power of number of digits presend in the number and then 
# we add those numbers and it gets equal to the actual number then that number is said to be armstrong number

n = 8208
nod = len(str(n))
digit = n
arm_Num = 0
while digit > 0:
    last_Digit = digit % 10
    arm_Num = arm_Num + last_Digit ** (nod)
    digit = digit // 10
if arm_Num == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
# TC = O(log10(N))  SC = O(1)
