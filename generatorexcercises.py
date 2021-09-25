"""class MyGen():
    current = 0
    def __init__(self,first,last):
        self.first = first
        self.last = last
        print(self.last,self.first)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if 100 <= self.last:
            num = MyGen.current
            MyGen.current +=1
            return num
        raise StopIteration

gen = MyGen(0,100)
print(list(gen))
for i in gen:
    print(i)"""

   