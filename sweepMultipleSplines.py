"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.048
Name-US:Sweep Multiple Splines
Description-US:Puts selected splines in sweep nurbs
"""

import c4d
from c4d import gui

def sweepSplines():
    splines = doc.GetActiveObjects(2)

    for i in splines:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, i) #undo
        sweep = c4d.BaseObject(5118)
        doc.AddUndo(c4d.UNDOTYPE_NEW, sweep) #undo
        doc.InsertObject(sweep)
        parent = i.GetUp()
        if parent != None:
            sweep.InsertUnder(parent)
        i.InsertUnder(sweep)
        circle = c4d.BaseObject(5181)
        circle[c4d.SPLINEOBJECT_INTERPOLATION] = 1
        circle[c4d.SPLINEOBJECT_SUB] = 3
        circle[c4d.PRIM_CIRCLE_RADIUS] = 1
        circle.InsertUnder(sweep)
        newTag = c4d.BaseTag(c4d.Tphong)
        sweep.InsertTag(newTag)
        doc.AddUndo(c4d.UNDOTYPE_NEW, newTag)

doc.StartUndo()#undo
sweepSplines()
doc.EndUndo() #undo
c4d.EventAdd()
