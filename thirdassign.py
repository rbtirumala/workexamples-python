""" 

 """
# def caps(item):
#     print(item)
#     return item.upper()

# print(list(map(caps,my_pets)))

# my_strings = ['a', 'b', 'c', 'd', 'e']
#my_numbers = [5,4,3,2,1]

# my_numbers.sort()


# print(my_numbers)


# print(list(zip(my_strings,my_numbers)))


# scores = [73, 20, 65, 19, 76, 100, 88]
# my_numbers = [5,4,3,2,1]

# def over_50(item):
#     return item > 50

# print(list(filter(over_50,scores)))
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). 
# What is the total?

# scores = [73, 20, 65, 19, 76, 100, 88]
# my_numbers = [5,4,3,2,1]


# def accumulate (acc, item):
#     print(acc, item)
#     return acc + item

# first_sum=(reduce(accumulate,my_numbers,0))
# print(reduce(accumulate,scores,first_sum))

#square

# my_list = [5,4,3]
# print(list(map(lambda my_list:my_list*my_list,my_list)))




#list sorting

# a = [(0,2),(4,3),(9,9),(10,-1)]
# # def getKey(item):
# #     return item[1]
# l = sorted(a,key=lambda item:item[1])

# print(l)
""" some_list =['a','b','c','b','d','m','n','n']
duplicates ={item for item in some_list if some_list.count(item)>1}
print(duplicates)
 """
""" from time import time
def performance(fn):
    def wrapper (*args,**kawrgs):
        t1 = time()
        result = fn(*args,**kawrgs)
        t2 = time()
        print(f'it took {t2-t1} ms') 
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i*5

long_time() """

# user1={
#     'name':'Sorna',
#     'Valid': False,
# }

# def authenticated(fn):
#     def wrapper(*args,**kawrgs):
#         for item in args:
#             if item['Valid']:
#                 fn(args,**kawrgs)
#             else:
#                 print('invalid user')
#     return wrapper

# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)

# def fib(number):
#     for i in range (number):
#         yield i
# fibo=[]
# for item in fib(21):
       
#     print(next)




# def fibseq(num):
#     fib=[]
#     current = 0
#     previous = 0
#     for i in range(num):
#         if (i < 2):
#             next = current + previous
#             fib.append(next)
#             current +=1
#         else:
#             next = fib[i-1]+fib[i-2]
#             fib.append(next)
#             #print(fib)
#     return fib[num-1]   
# value = fibseq(20)
# print(value)
# def gen(num):
#     for i in range(num):
#         yield i

# for item in gen(100):
#     print(item)

""" current = 0
previous = 0
fib=[]

def fibseq(num):
    for i in range (num):
        
        yield i


for item in fibseq(100):
    
    
    if (item < 2):
        next = current + previous
        fib.append(next)
        current +=1
        
    else:
        next = fib[item-1]+fib[item-2]
        fib.append(next)
print(fib[99]) """
    

# my_first_name = "John"
        
        
