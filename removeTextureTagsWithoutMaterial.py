"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R16.021

Name-US:Remove Empty Texture Tags
Description-US:Removes texture tags that have no material
"""

import c4d
doc.StartUndo()

#GetAllObjects
def getAllObjects():
    allObjs = []
    def itterate(obj):
        while obj:
            allObjs.append(obj)
            itterate(obj.GetDown())
            obj = obj.GetNext()
        return allObjs    
    obj = doc.GetFirstObject()
    itterate(obj)
    return allObjs

objs = getAllObjects()

#remove tags
for i in objs:
    for j in i.GetTags():
        if j.GetType() == 5616:
            if j[c4d.TEXTURETAG_MATERIAL] == None:
                doc.AddUndo(c4d.UNDOTYPE_DELETE, j)
                j.Remove()

c4d.EventAdd()
doc.EndUndo()
