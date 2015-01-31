"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R16.021

Name-US:Remove Tags
Description-US:Removes tags of selected type from selected objects
"""

import c4d
from c4d import gui

doc.StartUndo()

#function to get all objects
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

#get selected objects or all objects if none are selected
if len(doc.GetActiveObjects(1)) > 0:
    objs = doc.GetActiveObjects(1)
else:
    objs = getAllObjects()

#make lists
selectedTags = doc.GetActiveTags()
selectedTagsTypes = [i.GetType() for i in selectedTags]

#remove tags
for i in objs:
    for j in i.GetTags():
        if j.GetType() in selectedTagsTypes:
            doc.AddUndo(c4d.UNDOTYPE_DELETE, j)
            j.Remove()

c4d.EventAdd()
doc.EndUndo()
