import numpy as np
from imageio import imread, imwrite

def decode(im, im2):
    res = np.copy(im)
    for ix in range(w):
        for iy in range(h):
            if (im[iy][ix][0] != im2[iy][ix][0]) or (im[iy][ix][1] != im2[iy][ix][1]) or (im[iy][ix][2] != im2[iy][ix][2]):
                res[iy][ix] = (255, 255, 255)
            else:
                res[iy][ix] = (0, 0, 0)
           
    imwrite('decode.jpg', res, format='jpg')

#input = sys.argv[1]
#output = sys.argv[2]
#input = "cat.jpg"
#sign = "cat_night.jpg"
input, sign, out = input("file name: ").split()
im = imread(input)
#sign = str(input("mark name: "))
#im = imread(input) # Открываем изображение
im_s = imread(sign) #подпись
(h, w, d) = im.shape

imwrite(out, im, format='jpg') # пересохраняем исходное изображение

im_mode = np.copy(im)

for ix in range(w):
   for iy in range(h):
        #im2[iy][w-ix-1]=im[iy][ix]
        #im2[iy][ix] = (0, 0, 0)
        if (im_s[iy][ix][0] == 255 and im_s[iy][ix][1] == 255) and im_s[iy][ix][2] == 255:
            im_mode[iy][ix] = (im[iy][ix][0]+1, im[iy][ix][1]+1, im[iy][ix][2]+1)
        #print(im[iy][ix], im2[iy][ix])
    
imwrite(out, im_mode, format='jpg') # сохраняем транспонированное изображение
decode(im, im_mode)
