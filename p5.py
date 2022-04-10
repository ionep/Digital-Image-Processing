from cmath import pi
from math import floor, sqrt, exp
from scipy import fftpack
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def readImage(path):
    im=Image.open(path)
    
    # im.show()
    return im

def shiftXY(npArr):
  rows,cols=npArr.shape
  for i in range(rows):
      for j in range(cols):
            npArr[i][j]=npArr[i][j]*((-1)**(i+j)) #f(x,y) * (-1)^(x+y)
  return npArr

def frequency_image(image):
  npImage = np.array(image)
  fft = fftpack.fftshift(fftpack.fft2(npImage))
  magnitude_spectrum = 20*np.log(np.abs(fft))
  newImage = Image.fromarray(magnitude_spectrum.astype(np.uint8))  
  newImage.show()

def laplacian(image):
  npImage = np.array(image)
  npImage=shiftXY(npImage)
  fft = fftpack.fftshift(fftpack.fft2(npImage))
  rows, cols= fft.shape
  for i in range(rows):
      for j in range(cols):
            fft[i][j]=-((2*pi)**2) * (i*i+j*j) * fft[i][j]
  ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(fft)))
  ifft2 = np.maximum(0, np.minimum(ifft2, 255))
  magnitude_spectrum = 20*np.log(np.abs(ifft2))
  magnitude_spectrum=shiftXY(magnitude_spectrum)
  newImage = Image.fromarray(magnitude_spectrum.astype(np.uint8))  
  newImage.show()

def idealLPF(image):
  npImage = np.array(image)
  cutoff=float(input("Enter cutoff radius"))
  npImage=shiftXY(npImage)
  fft = fftpack.fftshift(fftpack.fft2(npImage))
  rows, cols= fft.shape
  for i in range(rows):
      for j in range(cols):
            # u=i-rows/2
            # v=j-cols/2
            duv=sqrt(i*i+j*j) #D(u,v)=sqrt(u^2+v^2)
            if(duv<=cutoff):
              lpf=1
            else:
              lpf=0
            fft[i][j]=lpf*fft[i][j]
  ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(fft)))
  ifft2 = np.maximum(0, np.minimum(ifft2, 255))
  magnitude_spectrum = 20*np.log(np.abs(ifft2))
  magnitude_spectrum=shiftXY(magnitude_spectrum)
  newImage = Image.fromarray(magnitude_spectrum.astype(np.uint8))  
  newImage.show()

def butterworthLPF(image):
  npImage = np.array(image)
  cutoff=float(input("Enter cutoff radius:"))
  n=int(input("Enter order of filter:"))
  npImage=shiftXY(npImage)
  fft = fftpack.fftshift(fftpack.fft2(npImage))
  rows, cols= fft.shape
  for i in range(rows):
      for j in range(cols):
            # u=i-rows/2
            # v=j-cols/2
            duv=sqrt(i*i+j*j) #D(u,v)=sqrt(u^2+v^2)
            lpf=1/(1+(duv/cutoff)**(2*n))
            fft[i][j]=lpf*fft[i][j]
  ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(fft)))
  ifft2 = np.maximum(0, np.minimum(ifft2, 255))
  magnitude_spectrum = 20*np.log(np.abs(ifft2))
  magnitude_spectrum=shiftXY(magnitude_spectrum)
  newImage = Image.fromarray(magnitude_spectrum.astype(np.uint8))  
  newImage.show()

def gaussianLPF(image):
  npImage = np.array(image)
  cutoff=float(input("Enter cutoff radius:"))
  npImage=shiftXY(npImage)
  fft = fftpack.fftshift(fftpack.fft2(npImage))
  rows, cols= fft.shape
  for i in range(rows):
      for j in range(cols):
            # u=i-rows/2
            # v=j-cols/2
            duv=sqrt(i*i+j*j) #D(u,v)=sqrt(u^2+v^2)
            lpf=exp(-(1/2)*((duv/cutoff)**2))
            fft[i][j]=lpf*fft[i][j]
  ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(fft)))
  ifft2 = np.maximum(0, np.minimum(ifft2, 255))
  magnitude_spectrum = 20*np.log(np.abs(ifft2))
  magnitude_spectrum=shiftXY(magnitude_spectrum)
  newImage = Image.fromarray(magnitude_spectrum.astype(np.uint8))  
  newImage.show()


def idealHPF(image):
  npImage = np.array(image)
  cutoff=float(input("Enter cutoff radius"))
  npImage=shiftXY(npImage)
  fft = fftpack.fftshift(fftpack.fft2(npImage))
  rows, cols= fft.shape
  for i in range(rows):
      for j in range(cols):
            # u=i-rows/2
            # v=j-cols/2
            duv=sqrt(i*i+j*j) #D(u,v)=sqrt(u^2+v^2)
            if(duv<=cutoff):
              hpf=0
            else:
              hpf=1
            fft[i][j]=hpf*fft[i][j]
  ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(fft)))
  ifft2 = np.maximum(0, np.minimum(ifft2, 255))
  magnitude_spectrum = 20*np.log(np.abs(ifft2))
  magnitude_spectrum=shiftXY(magnitude_spectrum)
  newImage = Image.fromarray(magnitude_spectrum.astype(np.uint8))  
  newImage.show()

def butterworthHPF(image):
  npImage = np.array(image)
  cutoff=float(input("Enter cutoff radius:"))
  n=int(input("Enter order of filter:"))
  npImage=shiftXY(npImage)
  fft = fftpack.fftshift(fftpack.fft2(npImage))
  rows, cols= fft.shape
  for i in range(rows):
      for j in range(cols):
            duv=sqrt(i*i+j*j) #D(u,v)=sqrt(u^2+v^2)
            if(duv==0):
              duv=0.0001
            hpf=1/(1+(cutoff/duv)**(2*n))
            fft[i][j]=hpf*fft[i][j]
  ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(fft)))
  ifft2 = np.maximum(0, np.minimum(ifft2, 255))
  magnitude_spectrum = 20*np.log(np.abs(ifft2))
  magnitude_spectrum=shiftXY(magnitude_spectrum)
  newImage = Image.fromarray(magnitude_spectrum.astype(np.uint8))  
  newImage.show()

def gaussianHPF(image):
  npImage = np.array(image)
  cutoff=float(input("Enter cutoff radius:"))
  npImage=shiftXY(npImage)
  fft = fftpack.fftshift(fftpack.fft2(npImage))
  rows, cols= fft.shape
  for i in range(rows):
      for j in range(cols):
            # u=i-rows/2
            # v=j-cols/2
            duv=sqrt(i*i+j*j) #D(u,v)=sqrt(u^2+v^2)
            hpf=1-exp(-(1/2)*((duv/cutoff)**2))
            fft[i][j]=hpf*fft[i][j]
  ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(fft)))
  ifft2 = np.maximum(0, np.minimum(ifft2, 255))
  magnitude_spectrum = 20*np.log(np.abs(ifft2))
  magnitude_spectrum=shiftXY(magnitude_spectrum)
  newImage = Image.fromarray(magnitude_spectrum.astype(np.uint8))  
  newImage.show()

inp=int(input("Enter your choice:\n \
    1. Fourier Image \n \
    2. Laplacian \n \
    Low Pass Filter \n \
    3. Ideal LPF \n \
    4. Butterworth LPF \n \
    5. Gaussian LPF \n \
    High Pass Filter \n \
    6. Ideal HPF \n \
    7. Butterworth HPF \n \
    8. Gaussian HPF \n \
    "))
im=readImage("einstein.jpg")
if(inp==1):
    frequency_image(im)
elif(inp==2):
    laplacian(im)
elif(inp==3):
    idealLPF(im)
elif(inp==4):
    butterworthLPF(im)
elif(inp==5):
    gaussianLPF(im)
elif(inp==6):
    idealHPF(im)
elif(inp==7):
    butterworthHPF(im)
elif(inp==8):
    gaussianHPF(im)