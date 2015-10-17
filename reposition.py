"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R16.021

Name-US:Reposition Object
Description-US:Repositions the first selected object to the second selected object (position and rotation)
"""

import c4d
from c4d import gui

if len(doc.GetActiveObjects(2)) != 2:
    gui.MessageDialog('Select 2 Objects!')
else:
    doc.StartUndo()
    objA = doc.GetActiveObjects(2)[0]
    objB = doc.GetActiveObjects(2)[1]
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, objA)
    objA[c4d.ID_BASEOBJECT_REL_POSITION] = objB[c4d.ID_BASEOBJECT_REL_POSITION]
    objA[c4d.ID_BASEOBJECT_REL_ROTATION] = objB[c4d.ID_BASEOBJECT_REL_ROTATION]
    c4d.EventAdd()
    doc.EndUndo()
