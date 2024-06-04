a  = [1,2,3,4,4,5,6,7,1,2,4,4,12,5,6,22]
a = [2,2,3,1]
Largest = -100000000000000
SecondLargest  = -10000000000
ThirdLargest = -100000000
b = []
for i in a:
    if i in b:
        continue
    else:
        b.append(i)
        if i>Largest:
            ThirdLargest = SecondLargest
            SecondLargest = Largest
            Largest = i
        elif i>SecondLargest:
            ThirdLargest = SecondLargest
            SecondLargest = i
        elif i>ThirdLargest:
            ThirdLargest=i

if len(b) <= 2:
    ThirdLargest = Largest
print(Largest,SecondLargest,ThirdLargest)


print(ord('a'))