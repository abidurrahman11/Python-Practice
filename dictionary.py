person1 = {"name" : "john", "age": 23 , "address" : "NYC", "phone" : 121212}
print(person1)

name = person1["name"]
print(name)

person1["email"] = "xyz@gmail.com"
print(person1)

person1["phone"] = 323333
print(person1)

del person1["email"]
print(person1)


#Another way to declare dictionary
person2 = dict(name = "Mark", age = 21, address = "MI", email = "ycc@hotmail.com")
print(person2)

#updating a dictionary by another one
person1.update(person2)
print(person1)



person1.pop("address")
print(person1)

person1.popitem()
print(person1)

for key in person1:
    print(key)

for value in person1.values():
    print(value)

for key, value in person1.items():
    print(key, value)

