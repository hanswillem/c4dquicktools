
"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.048
Name-US:Sweep Multiple Splines Circle
Description-US:Puts selected splines in sweep nurbs
"""

import c4d
from c4d import gui
doc.StartUndo()#undo

def sweepSplines():
    splines = doc.GetActiveObjects(1)
    
    for i in splines:
        if (i.GetType() == 5101) or (i.GetType() == 5186) or (i.GetType() == 5181):
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
            circle[c4d.PRIM_CIRCLE_RADIUS] = userInput 
            circle.InsertUnder(sweep)
            
            newTag = c4d.BaseTag(c4d.Tphong)
            sweep.InsertTag(newTag)
            doc.AddUndo(c4d.UNDOTYPE_NEW, newTag)


userInput = gui.RenameDialog('thickness')

if userInput != None:
    userInput = float(userInput)
    sweepSplines()
    c4d.EventAdd()
    doc.EndUndo() #undo