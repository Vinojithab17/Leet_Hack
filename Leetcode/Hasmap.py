hashmap = {}

a = [22,44,66,33,55,33,23,56,77,56,97,33,46,99,75,99,66,45,13,90,567,123]

for i in a:
    key = i%len(a)
    try:
        x = hashmap[key]
        hashmap[key].append(i)
    except KeyError as e:
        hashmap[key] = [i]
        

print(hashmap)