print("------Sets and Dicts------")
fruits = {"apple", "banana", "mango"}
print(fruits)
fruits = {"apple", "banana", "mango"}
fruits.update(["orange", "Pineapple"])
print(fruits)
name={"Rana","Asad","Dawood"}
name.update(["Ali","Ahmed"])
print(name)
print("Ali" in name)
print(len(name))
name.remove("Ali")
print(name)
a = {1,2,3,4,5,6,7,7,8,9,9,10}
b = {11,12,13,14,15}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(b.intersection_update(a))
print(a)
print(b)

print("------Dicts------")
a = {"name":"Rana","age":17,"city":"Multan"}
print(a["city"])
print(a["name"])
print(a.keys())
print(a.values())
print(a.items())
a["city"]="Islamabad"
print(a)
print(a.pop("age"))
a={}
a["country"]="Pakistan"
print(a)


print("------Short hand if else statement------")
a = 7
b = 8
print(a, "is greater than B") if a > b else print(b, "is greater than A")