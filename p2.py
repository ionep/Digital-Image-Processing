import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def readImage(path):
    im=Image.open(path)
    
    # im.show()
    return im

def contrastStretching(im):
    #convert to numpy array
    npImage=np.array(im)
    orgImage=npImage
    min=npImage.min()
    max=npImage.max()
    range=max-min
    npImage=(npImage-min)/range * 255
    newImage=Image.fromarray(npImage.astype(np.uint8)) 
    newImage.show()
    fig = plt.figure()
    fig.add_subplot(2,1,1)
    plt.hist(orgImage.flatten(), bins=50)
    fig.add_subplot(2,1,2)
    plt.hist(npImage.flatten(), bins=50)
    plt.show()

def histogramEqualization(img):
    npImage=np.array(im)
    orgImage=npImage

    histogram = np.zeros(256)
    for pixel in npImage.flatten():
        histogram[pixel] += 1
    a = iter(histogram)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)

    cs = np.array(b)
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()
    cs = nj / N
    cs = cs.astype('uint8')
    npImage = cs[npImage.flatten()]
    npImage=np.reshape(npImage, orgImage.shape)
    newImage=Image.fromarray(npImage.astype(np.uint8)) 
    newImage.show()
    fig = plt.figure()
    fig.add_subplot(2,1,1)
    plt.hist(orgImage.flatten(), bins=50)
    fig.add_subplot(2,1,2)
    plt.hist(npImage.flatten(), bins=50)
    plt.show()

inp=int(input("Enter your choice:\n \
    1. Contrast Stretching\n \
    2. Histogram Equalization:\n"))
im=readImage("einstein.jpg")
if(inp==1):
    contrastStretching(im)
elif(inp==2):
    histogramEqualization(im)