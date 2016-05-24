"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.048
Name-US:Extrude Multiple Splines
Description-US:Extrudes selected spline objects
"""

import c4d
from c4d import gui

doc.StartUndo()#undo

def extrudeSplines():
    global strength
    global extrudeOffset
    count = 0
    extr = 0
    splines = doc.GetActiveObjects(2)
    splines = splines[::-1]

    for i in splines:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, i) #undo
        i[c4d.SPLINEOBJECT_CLOSED] = 1
        parent = i.GetUp()
        extrude = c4d.BaseObject(5116)  
             
        doc.AddUndo(c4d.UNDOTYPE_NEW, extrude) #undo
        doc.InsertObject(extrude)
        
        newTag = c4d.BaseTag(c4d.Tphong)
        extrude.InsertTag(newTag)
        doc.AddUndo(c4d.UNDOTYPE_NEW, newTag)
        
        extrude[c4d.ID_BASELIST_NAME] = 'splineExtrude ' + str(count)
        extrude[c4d.EXTRUDEOBJECT_MOVE] = c4d.Vector(0, 0, strength)    
        extrude[c4d.ID_BASEOBJECT_REL_POSITION] = i[c4d.ID_BASEOBJECT_REL_POSITION]
        extrude[c4d.ID_BASEOBJECT_REL_SCALE] = i[c4d.ID_BASEOBJECT_REL_SCALE]
        extrude[c4d.ID_BASEOBJECT_REL_ROTATION] = i[c4d.ID_BASEOBJECT_REL_ROTATION]
        if parent != None:
            extrude.InsertUnder(parent)
        i.InsertUnder(extrude)
        i[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(0, 0, 0)
        i[c4d.ID_BASEOBJECT_REL_SCALE] = c4d.Vector(1, 1, 1)
        i[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(0, 0, 0)
        count = count + 1


userInput = gui.InputDialog('strength', '5')
strength = float(userInput)



extrudeSplines()

doc.EndUndo() #undo

c4d.EventAdd()

