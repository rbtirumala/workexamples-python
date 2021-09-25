import sys
import os
from PIL import Image, ImageFilter
from pathlib import Path

# grab 1 and 2 arguments
args= (sys.argv)

# check if new/ or another name exists, if not create it

if Path('args[2]').exists():
    print( 'new path exists :', args[2])
    print('from path exists: ', args[1])
else:
    f = open("args[2]",'x')

fromDirectory = args[1]
toDirectory = args[2]

c = 1
for filename in os.listdir(fromDirectory):
    if filename.endswith(".jpg"):
        args3= os.path.join(fromDirectory, filename)
        img = Image.open(args3,"r")
        name= 'img'+ str(c) +'.png'
        # print(name)
        # rgb_im = img.convert('RGB')
        args= os.path.join(toDirectory, name)
        img.save(args,'png')
        c +=1
        continue
    else:
        continue
print('Done')

