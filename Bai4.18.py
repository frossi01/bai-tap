import math
def fibonacci(n):
    if (n < 0):
        return -1;
    elif (n==0 or n==1):
        return n;
    else:
        return fibonacci(n - 1)+ fibonacci(n - 2);
n = int(input("Nhập số nguyên dương n = "));
print ("Tất cả các số fibonacci nhỏ hơn", n);
i = 0;
fin = fibonacci(i);
while(fin < n):
    fin = fibonacci(i);
    print(fin)
    i = i + 1;
