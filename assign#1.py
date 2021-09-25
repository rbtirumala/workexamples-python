#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def catage (self):
        #print(f'catx is {self.age}')
        return self.age

    


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Amy',3)
cat2 = Cat('Sweety',4)
cat3 = Cat('Cuty',2)
agearray=[]
agearray= (cat1.catage(),cat2.catage(),cat3.catage())

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
#print(f'The oldest cat is', oldest(), 'years old')

print(f'The oldest cat is', max(agearray),'years old')