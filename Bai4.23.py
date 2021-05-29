s = input("Nhap cau cua ban: ")
d={"DIGITS":0, "LETTERS":0}
for c in s:
   if c.isdigit():
       d["DIGITS"]+=1
   elif c.isalpha():
       d["LETTERS"]+=1
   else:
         pass
print ("So chu cai la:", d["LETTERS"])
print ("So chu cai la:", d["DIGITS"])
