a = 1234
int1=0
while a>0 :
    print(a%10)
    int1=int1*10+a%10
    a = a//10
    
print(int1)