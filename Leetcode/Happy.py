a  = int (input())  

for i in range(a):
    y = input().split(" ")
    bus = int(y[0])
    position = int(y[1])
    
    passengerCount = 0
    openWindowCount = 0
    back = 0
    for i in range(bus):
        x = input().split(" ")
        passenger = int(x[0])
        Openwindow = int(x[1])
        
        if Openwindow + openWindowCount >= position:
            print(back)
            break
        else:
            openWindowCount += Openwindow
            back = passenger-Openwindow
    else:
        print(-1)