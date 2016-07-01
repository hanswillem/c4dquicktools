
"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.048
Name-US:Sweep Multiple Splines Square
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
            
            square = c4d.BaseObject(5186)
            square[c4d.SPLINEOBJECT_INTERPOLATION] = 1
            square[c4d.SPLINEOBJECT_SUB] = 3
            square[c4d.PRIM_RECTANGLE_WIDTH] = userInput
            square[c4d.PRIM_RECTANGLE_HEIGHT] = userInput
            square.InsertUnder(sweep)
            
            newTag = c4d.BaseTag(c4d.Tphong)
            sweep.InsertTag(newTag)
            doc.AddUndo(c4d.UNDOTYPE_NEW, newTag)


userInput = gui.RenameDialog('thickness')

if userInput != None:
    userInput = float(userInput)
    sweepSplines()
    c4d.EventAdd()
    doc.EndUndo() #undo