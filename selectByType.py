"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R16.021

Name-US:Select By Type
Description-US:Extends the current selection of objects by their type
"""

#selects all objects in the object hierarchy that have the same type as the selected object(s)

import c4d
from c4d import gui

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

#make list of selected types
types = []
selectedObjs = doc.GetActiveObjects(1)
for i in selectedObjs:
    if i.GetType() not in types:
        types.append(i.GetType())

#extend selection
objs = getAllObjects()
for i in objs:
    for j in types:
        if j == i.GetType():            
            doc.SetSelection(i, c4d.SELECTION_ADD)

c4d.EventAdd()
