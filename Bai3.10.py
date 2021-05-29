import math
def Tinh(R):
    if R>0:
        s=math.pi*R**2
        c=2*math.pi*R
        print("chu vi hinh tron la", c)
        print("dien tich hinh tron la", s)
    else:
        print("ban kinh ko hop le")
R=int(input("nhap ban kinh hinh tron : " ))
Tinh(R)
