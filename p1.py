import numpy as np
from PIL import Image

def readImage(path):
    im=Image.open(path)
    
    im.show()
    return im

# max in the image - image
def negative(im):
    #convert to numpy array
    npImage=np.array(im)
    max=npImage.max() #get the maximum
    newImage=Image.fromarray(max-npImage) #subtract from maximum and convert back to image
    newImage.show()

# thresholding at r
def threshold(im):
    th=int(input("Enter amount to threshold at: "))
    npImage=np.array(im)
    npImage=npImage>th
    npImage=npImage.astype(np.uint8)*255
    newImage=Image.fromarray(npImage)
    newImage.show()

def logTransform(im):
    c=float(input('Enter value of c:'))
    npImage=np.array(im)
    npImage=npImage/255
    npImage=c*np.log(1+npImage)*255
    newImage=Image.fromarray(npImage.astype(np.uint8))
    newImage.show()

def powerLaw(im):
    c=float(input('Enter value of c:'))
    g=float(input('Enter value of gamma:'))
    npImage=np.array(im)
    npImage=npImage/255
    npImage=c*np.power(npImage,g)*255
    newImage=Image.fromarray(npImage.astype(np.uint8))
    newImage.show()

def grayLevelSuppressedSlicing(im):
    boostValue=100
    minLevel=int(input('Enter minimum value:'))
    maxLevel=int(input('Enter maximum value:'))
    npImage=np.array(im)

    #fully suppress other levels
    npImage=np.where((npImage>minLevel) & (npImage<maxLevel), npImage+boostValue, 20)
    npImage=np.where(npImage>255, 255, npImage)
    newImage=Image.fromarray(npImage.astype(np.uint8))
    newImage.show()

def grayLevelMaintainSlicing(im):
    boostValue=100
    minLevel=int(input('Enter minimum value:'))
    maxLevel=int(input('Enter maximum value:'))
    npImage=np.array(im)

    #maintain other levels
    npImage=np.where((npImage>minLevel) & (npImage<maxLevel), npImage+boostValue, npImage)
    npImage=np.where(npImage>255, 255, npImage)
    newImage=Image.fromarray(npImage.astype(np.uint8))
    newImage.show()

def bitPlaneSlicing(im,bit):
    if(bit<1 or bit>8):
        print("Error in bit")
        return 0
    npImage=np.array(im)
    masks=[1,2,4,8,16,32,64,128]
    num_rows, num_cols = npImage.shape
    npMask=np.full((num_rows,num_cols),masks[bit-1])
    npImage=npImage & npMask
    newImage=Image.fromarray(npImage.astype(np.uint8))
    newImage.show()

inp=int(input("Enter your choice:\n \
    1. Negative of a image\n \
    2. Threshold of a image\n \
    3. Logarithmic transform \n \
    4. Power Law transform \n \
    5. Graylevel Slice(Suppress) \n \
    6. Graylevel Slice(Maintain) \n \
    7. Bitplane Slice: \n"))
im=readImage("einstein.jpg")
if(inp==1):
    negative(im)
elif(inp==2):
    threshold(im)
elif(inp==3):
    logTransform(im)
elif(inp==4):
    powerLaw(im)
elif(inp==5):
    grayLevelSuppressedSlicing(im)
elif(inp==6):
    grayLevelMaintainSlicing(im)
elif(inp==7):
    for i in range(1,9):
        bitPlaneSlicing(im,i)