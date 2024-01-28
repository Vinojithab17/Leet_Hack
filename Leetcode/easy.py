import math

def solution(V, theta, alpha, g=9.8):
    theta_rad = theta*(3.14/180)
    alpha_rad = alpha*(3.14/180)
    
    
    total_rad = (theta+alpha)*(3.14/180)


    T = (2*V*math.sin(theta_rad))/(g*math.cos(alpha_rad))
    R = V*math.cos(total_rad)*T/math.cos(alpha_rad)

    return "{:.2f}".format(T) ,"{:.2f}".format(R)



theta = float(input())
V = float(input())
alpha = float(input())

result = solution(V, theta, alpha)

if result:
    T, R = result
    print(T,R)
