a = 5
b = [[1]]

for i in range(1,a):
    b.append([])
    for j in range (1,i+1):
        b[i][j] = a[i-1][j-1] + a[i-1][j]
