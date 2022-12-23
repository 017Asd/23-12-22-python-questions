sample_list=[11, 45, 8, 11, 23, 45, 23, 45, 89]
# for i in sample_list:
#     a=sample_list.count(i)
#     print("Printing count of each item  ",i ,a)

from collections import Counter
x=Counter(sample_list)
print("Printing count of each item  ",x)