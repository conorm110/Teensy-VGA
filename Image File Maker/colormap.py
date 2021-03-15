
from PIL import Image

image = Image.open('image_original.jpg')
new_image = image.resize((640, 480))
new_image.save('image_lowres.jpg')

x = 0
y = 0
im = Image.open('image_lowres.jpg')

pix = im.load()
xsize = int((((str(im.size)[1:]).split(","))[0]))
ysize = int(((((str(im.size)[1:]).split(","))[1])[1:]).replace(')', ''))

i = 0
j = 0
col = {0, 0, 0}
dataListRaw = {}
while (i<480):
    j = 0
    while (j<640):
        col = (((str(str(pix[j,i]).replace('(', '')).replace(')', ""))).replace(' ', '').split(','))
        k = 0
        while k < 3:
            if (int(col[k]) > 120):
                col[k] = '1'
            else:
                col[k] = '0'
            k = k+1
        
        if(int(col[0]) == 0):
            if(int(col[1]) == 0):
                if(int(col[2]) == 0):
                    col[0] = 0
                elif(int(col[2]) == 1):
                    col[0] = 1
            elif(int(col[1]) == 1):
                if(int(col[2]) == 0):
                    col[0] = 2
                elif(int(col[2]) == 1):
                    col[0] = 3
        elif(int(col[0]) == 1):
            if(int(col[1]) == 0):
                if(int(col[2]) == 0):
                    col[0] = 4
                elif(int(col[2]) == 1):
                    col[0] = 5
            elif(int(col[1]) == 1):
                if(int(col[2]) == 0):
                    col[0] = 6
                elif(int(col[2]) == 1):
                    col[0] = 7
        dataListRaw[(i*640)+j] = str(col[0]) +","
        j = j + 1
    i = i+ 1
  
f = open("bitmap.txt", "w")

i = 0
j = 0

while (i<480):
    j = 0
    while (j<640):
        f.write(str(dataListRaw[(i*640)+j]))
        j = j + 1

    i = i+ 1
f.close()
