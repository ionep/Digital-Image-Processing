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
    # newArray=np.where(newArray<0,0,newArray)
    # newArray=np.where(newArray>255,255,newArray)
    return newArray

def laplacian(img):
    npImage=np.array(img)
    filter_array=np.array([[0,1,0],
                    [1,-4,1],
                    [0,1,0]])
    newArray=applyFilter(npImage,filter_array)
    newImage=Image.fromarray(newArray.astype(np.uint8)) 
    newImage.show()
    finalArr=npImage-newArray
    finalImage=Image.fromarray(finalArr.astype(np.uint8)) 
    finalImage.show()

def prewitt(img):
    npImage=np.array(img)
    filter_array_row=np.array([[-1,-1,-1],
                    [0,0,0],
                    [1,1,1]])
    filter_array_col=np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])
    newArray_row=applyFilter(npImage,filter_array_row)
    newImage=Image.fromarray(newArray_row.astype(np.uint8)) 
    newImage.show()
    newArray_col=applyFilter(npImage,filter_array_col)
    newImage=Image.fromarray(newArray_col.astype(np.uint8)) 
    newImage.show()
    newArray=newArray_row+newArray_col
    newImage=Image.fromarray(newArray.astype(np.uint8)) 
    newImage.show()

def sobel(img):
    npImage=np.array(img)
    filter_array_row=np.array([[-1,-2,-1],
                    [0,0,0],
                    [1,2,1]])
    filter_array_col=np.array([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]])
    newArray_row=applyFilter(npImage,filter_array_row)
    newImage=Image.fromarray(newArray_row.astype(np.uint8)) 
    newImage.show()
    newArray_col=applyFilter(npImage,filter_array_col)
    newImage=Image.fromarray(newArray_col.astype(np.uint8)) 
    newImage.show()
    newArray=newArray_row+newArray_col
    newImage=Image.fromarray(newArray.astype(np.uint8)) 
    newImage.show()

inp=int(input("Enter your choice:\n \
    1. Laplacian\n \
    2. Prewitt \n \
    3. Sobel \n \
    "))
im=readImage("einstein.jpg")
if(inp==1):
    laplacian(im)
elif(inp==2):
    prewitt(im)
elif(inp==3):
    sobel(im)