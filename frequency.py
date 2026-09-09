dictionary = {"codingal":2, "is":3, "fun":1, "and":2, "great":1}

print("The original dictionary is:", str(dictionary))

k = 2

res=0
for key in dictionary:
    if dictionary[key] == k:
        res += 1

print("The frequency of", k, "in the dictionary is:", res)