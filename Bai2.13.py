import math
print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
        print("x1 = ", (-(b) - math.sqrt(delta))/(2*a) )
