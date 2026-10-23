import cv2
import sys
from PIL import Image
def show_img(words):
  
  #words=MyText.split(" ")
  #for i in words:
   # print(i)
    #ss=str(i)
    #nn=split(ss)
    #print(nn)
                
    #nn.clear()
  
  images = [Image.open("alpha/"+x+".png") for x in words]
  widths, heights = zip(*(i.size for i in images))

  total_width = sum(widths)
  max_height = max(heights)

  new_im = Image.new('RGB', (total_width, max_height))

  x_offset = 0
  for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

  new_im.save('test.jpg')
  
