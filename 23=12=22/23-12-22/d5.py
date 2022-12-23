sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}


x = ["name", "salary"]

y = dict()

for k in x:
    
    y.update({k: sample_dict[k]})
print(y)