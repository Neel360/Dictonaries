person = {"Name": "John Doe", "Age": 25, "Job": "Doctor", "Phone-number": "+44 1234 567890"}
print(person["Age"])
print(person.get("Job"))

person["Age"] = 26
print(person["Age"])
person["Email"] = "abc@xyz.com"

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(squares.pop(4))

print("The length of the dictionary is:", len(squares))

for i in squares:
    print(i, squares[i])
squares.clear()