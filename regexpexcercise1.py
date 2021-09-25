import re


def checkpwd():
    string = input("password:")
    pattern = re.compile(r"(^[\w][\d][\w][\d][\w][\d][\w][@_!#$%^&*()<>?/\|}{~:])")
    
    a = pattern.search(string)
    
    if (len(string) < 8):
        print("Hello, please retry length is less than 8 characters!")
    
    else:
        print("Way to go!!")
    
    return a
    

b=checkpwd()
print(b)