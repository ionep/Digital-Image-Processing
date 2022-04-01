import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def readImage(path):
    im=Image.open(path)
    
    # im.show()
    return im

def applyFilter(npImage,filter_array,type="weight"):
    filter_size, _=filter_array.shape
    num_rows, num_cols = npImage.shape
    padded=np.pad(npImage,
        ((int((filter_size-1)/2),int((filter_size-1)/2)),(int((filter_size-1)/2),int((filter_size-1)/2)))
        ,'constant')
    lst=[]
    for i in range(num_rows):
        for j in range(num_cols):
            window = padded[i:(filter_size+i),j:(filter_size+j)]
            
            r=0
            #applying filter
            if(type=="weight"):
                r = np.sum(np.multiply(filter_array,window))
            elif(type=="median"):
                r=np.median(window)
            
            lst.append(r)
    newArray = np.resize(lst,(num_rows,num_cols))
    # Normalised [0,255] for negative
    # newArray = 255*((newArray - np.min(newArray))/np.ptp(newArray))
    return newArray

def averageFilter(img):
    npImage=np.array(img)
    filter_size=int(input("Enter filter size:"))
    filter_array=np.full((filter_size,filter_size), 1/(filter_size*filter_size))
    newArray=applyFilter(npImage,filter_array)
    newImage=Image.fromarray(newArray.astype(np.uint8)) 
    newImage.show()

def weightedFilter(img):
    npImage=np.array(img)
    filter_size=int(input("Enter filter size:"))
    filter_array=[]
    for i in range(filter_size):
        for j in range(filter_size):
            weight=float(input("Enter weight[{}][{}]:".format(i,j)))
            filter_array.append(weight)
    filter_array=np.resize(filter_array,(filter_size,filter_size))
    newArray=applyFilter(npImage,filter_array)
    newImage=Image.fromarray(newArray.astype(np.uint8)) 
    newImage.show()

def medianFilter(img):
    npImage=np.array(img)
    filter_size=int(input("Enter filter size:"))
    filter_array=np.full((filter_size,filter_size), 0) #dummy to send filter size
    newArray=applyFilter(npImage,filter_array,"median")
    newImage=Image.fromarray(newArray.astype(np.uint8)) 
    newImage.show()

def highBoost(img):
    npImage=np.array(img)
    filter_size=int(input("Enter filter size:"))
    filter_array=[]
    for i in range(filter_size):
        for j in range(filter_size):
            weight=float(input("Enter weight[{}][{}]:".format(i,j)))
            filter_array.append(weight)
    A=float(input("Enter amplification factor:"))
    filter_array=np.resize(filter_array,(filter_size,filter_size))
    newArray=applyFilter(npImage,filter_array)
    newArray=(A-1) * npImage + newArray
    newImage=Image.fromarray(newArray.astype(np.uint8)) 
    newImage.show()

inp=int(input("Enter your choice:\n \
    Smoothing: \n \
    1. Average Filter\n \
    2. Weighted Smoothing Filter\n \
    3. Median Filter \n \
    Sharpening: \n \
    4. Weighted Sharpening Filter \n \
    5. High Boost: \n \
    "))
im=readImage("empty.jpg")
if(inp==1):
    averageFilter(im)
elif(inp==2 or inp==4):
    weightedFilter(im)
elif(inp==3):
    medianFilter(im)
elif(inp==5):
    highBoost(im)