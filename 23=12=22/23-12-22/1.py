l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd_i = []
even_i = []
for i in range(0, len(l1)):
    if i % 2!=0:
        odd_i.append(l1[i])
print("Element at odd-index positions from list one",odd_i)
for i in range(0,len(l2)):
    if i % 2==0:
        even_i.append(l2[i])  
print("Element at even-index positions from list two",even_i)     
l3 = odd_i + even_i

print("Printing Final third list",l3)
