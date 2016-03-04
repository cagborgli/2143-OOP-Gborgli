#Christopher Gborgli
# Abdullah Alathel
import cat
import os
import time
from PIL import Image
import sys

class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image
        self.img = None         # Pillow var to hold image


    """
    @Description:
    - Uses random cat to go get an amazing image from the internet
    - Names the image
    - Saves the image to some location
    @Returns:
    """
    def getImage(self, name = None):
        if name == None :
            self.name = self.getTimeStamp()
            cat.getCat(directory=self.path, filename=self.name, format=self.format)
        else:
            self.name = name
        
        self.img = Image.open(self.name+'.'+self.format)

        self.width, self.heigth = self.img.size

    """
    Saves the image to the local file system given:
    - Names
    - Path
    """
    def saveImage(self):
        pass
      
    """
    """
    def nameImage(self):
        pass

    """
    Gets time stamp from local system
    """
    def getTimeStamp(self):
        seconds,milli = str(time.time()).split('.')
        return seconds


"""
The ascii character set we use to replace pixels.
The grayscale pixel values are 0-255.
0 - 25 = '#' (darkest character)
250-255 = '.' (lightest character)
"""


class asciiShop(RandomCat):

    def __init__(self,new_width="not_set"):
        super(asciiShop, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0

        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.imageAsAscii = []
        self.matrix = None
        self.all_pixels = None
        


    """
    Your comments here
    """

    def convertToAscii(self):

        if self.newWidth == "not_set":
            self.newWidth = self.width

        self.newHeight = int((self.heigth * self.newWidth) / self.width)

        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height
            
        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        self.all_pixels = list(self.newImage.getdata())

        
        self.matrix = listToMatrix(self.all_pixels,self.newWidth)
        for pixel_value in self.all_pixels:
            index = pixel_value // 25
            self.imageAsAscii.append(self.asciiChars[int(index)])
    """
    Print the image to the screen
    """
    def printImage(self):
        self.imageAsAscii = ''.join(ch for ch in self.imageAsAscii)
        for c in range(0, len(self.imageAsAscii), self.newWidth):
            print (self.imageAsAscii[c:c+self.newWidth])
            
    """
    @Name: flip
    @Description:
    This method will flip an image horizontally, or vertically. 
    Vertically means all pixels in row 0 => row N, row 1 => row N-1, ... row N/2 => row N/2+1
    Horizontally means all pixels in col 0 => col N, col 1 => col N-1, ... col N/2 => col N/2+1
    @Params: direction (string) - [horizontal,vertical] The direction to flip the cat.
    @Returns: (string) - Flipped ascii image.
    """


    def flip(self,direction =None):
        Horizontal = []
        Vertical = []
        l_to_print = []
        if direction == "Horizontal" or direction =="horizontal":
            temp = []
            for l in self.matrix:
                temp.append(list(reversed(l)))
            for lists in temp:
                for value in lists:
                    Horizontal.append(int(value))
            for pix_val in Horizontal:
                ind = pix_val // 25
                l_to_print.append(self.asciiChars[int(ind)])
            printImage(l_to_print,self.newWidth)
        elif direction == "Vertical" or direction == "vertical":
            tem = []
            for i in range (len(self.matrix)-1,-1,-1):
                tem.append(self.matrix[i])
            for l in tem:
                for val in l:
                    Vertical.append(int(val))
            for p_val in Vertical:
                inde = p_val // 25
                l_to_print.append(self.asciiChars[int(inde)])
            printImage(l_to_print,self.newWidth)
        else:
                print("Come on dude you need to know your Directions ! ")
    """
    @Name: invert 
    @Description:
    This method will take all the lightest pixels and make them the darkest, next lightest => next darkest, etc..
    @Params: None
    @Returns: (string) - Inverted ascii image.
    """
    def invert(self):
        rchars = list(reversed(self.asciiChars))
        invert = []
        for pixel_value in self.all_pixels:
            index = pixel_value // 25
            invert.append(rchars[int(index)])
        printImage(invert,self.newWidth)
    """
    Convert to 2D list of lists to help with manipulating the ascii image.
    Example:
    """
def listToMatrix(l, n):
    return[l[i:i+n] for i in range(0, len(l), n)]
def printImage(array,wid):
    array = ''.join(ch for ch in array)
    for c in range(0, len(array), wid):
        print (array[c:c+wid])

if __name__=='__main__':
    awesomeCat = asciiShop(150)
    awesomeCat.getImage()

    awesomeCat.convertToAscii()
    awesomeCat.printImage()
    awesomeCat.invert()
    #awesomeCat.flip("vertical")
