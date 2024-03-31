

a = "101111"
b = "10"
# Output: "10101"

s = ""
carry = 0

x = len(a)-1
y = len(b)-1

while x >= 0 or y >= 0:
    sum = carry
    if x >= 0:
        sum += int(a[x])
    if y >= 0:
        sum += int(b[y])
    s = str(sum%2) + s
    carry = sum//2
    x-=1
    y-=1
    
if carry:
    s = "1" + s
print(s)
    

