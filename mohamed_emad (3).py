#quiz python(dictionary)_1
key = ['Ten', 'Twenty', 'Thirty']
value = [10, 20, 30]
res = {}

for i in range(len(key)):
    res[key[i]] = value[i]
print(res)

print("------------------------")
#quiz python(dictionary)_1

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
    
keys = ["name", "salary"]
    
ext={}
for i in keys:
     if i in sample_dict.keys():
         ext[i]=sample_dict[i]
print(ext)

print("------------------------")
#quiz python(dictionary)_1 in another way

extract={i:sample_dict[i] for i in keys if i in sample_dict.keys()}
print(extract)



