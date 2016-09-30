"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.048
Name-US:Create Card With Image
Description-US:Creates a card with the selected material as texture
"""


import c4d
from c4d import gui, bitmaps
import os


def getImageSize(mat): 
    pathToFile = mat[c4d.MATERIAL_COLOR_SHADER][c4d.BITMAPSHADER_FILENAME]
    bmp = bitmaps.BaseBitmap(pathToFile) 
    bmp.InitWith(pathToFile)   
    w, h = bmp.GetSize() 
    return [w, h]


def resizeCard(card, mat):
    w, h = getImageSize(mat)
    card[c4d.PRIM_PLANE_WIDTH] = w
    card[c4d.PRIM_PLANE_HEIGHT] = h


def createCard(mat):
    card = c4d.BaseObject(5168)
    card[c4d.PRIM_AXIS] = 5
    card[c4d.PRIM_PLANE_SUBW] = 1
    card[c4d.PRIM_PLANE_SUBH] = 1
    doc.InsertObject(card)
    texTag = c4d.BaseTag(5616)
    texTag[c4d.TEXTURETAG_MATERIAL] = mat
    texTag[c4d.TEXTURETAG_PROJECTION] = 6
    card.InsertTag(texTag)
    resizeCard(card, mat)
    

def createMultipleCards():
    for mat in doc.GetActiveMaterials():
        createCard(mat)


def main():
    createMultipleCards()
    c4d.EventAdd()
    

if __name__ == '__main__':
    main()
