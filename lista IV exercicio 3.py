import random
l1 = []
l2 = []
l3 = []
for i in range(20):
    l1.append(random.randint(1,100))
    l3.append(l1[i])
    l2.append(random.randint(1,100))
    l3.append(l2[i])

print (l1)
print (l2)
print (l3)
