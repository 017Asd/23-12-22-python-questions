sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

a = ["name", "salary"]

for k in a:
    sample_dict.pop(k)
print(sample_dict)