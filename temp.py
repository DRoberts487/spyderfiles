from matplotlib import pyplot as plt 
from matplotlib import image as mpimg

plt.title ('Dragon image')
plt.xlabel ('x panel scalling')
plt.ylabel ('y panel scalling')

image = mpimg.imread('dragon.jpg')
plt.imshow(image)
plt.show()
print (image.shape)

