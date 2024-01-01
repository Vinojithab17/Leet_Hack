lrgers = -1231153453562456
secondLargert = -1231153453562456

c = [1,2,3,4,5,5,6,7,8,9,4,4,6,32,6,7]

for i in range(0, len(c)):
    if c[i] > lrgers:
        secondLargert = lrgers
        lrgers = c[i]
        
print(lrgers, secondLargert)