import math
n = int(input("Nhap so nguyen duong n = "));
print ("Tat ca cac so nho hon", n,'co tong uoc lon hon no');
i = 1;
a = 0;
while (i < (n/2)):
   if n % 1 == 0:
       a = a + i;
       i = i + 1;
       if a > n:
          print(n)
