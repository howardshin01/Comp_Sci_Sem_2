num = [6,9,32,28,15,22,3,18]
sum1 = 0

for x in range(0, len(num)):
    sum1 = sum1 + num[x]
    
aver = sum1 / len(num)
maxi = num[0]
mini = num[0]

for x in num:
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x
print(aver)
print(maxi)
print(mini)