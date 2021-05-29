class Hinhchunhat(object):
    def __init__(self, l, w):
       self.dai = l
       self.rong = w
    def area(self):
        return self.dai*self.rong

aHinhchunhat = Hinhchunhat(10,2)
print (aHinhchunhat.area())
