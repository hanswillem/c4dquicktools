"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R16.021

Name-US:Extrude Multiple Splines
Description-US:Extrudes selected spline objects
"""

import c4d
from c4d import gui

count = 0
splines = doc.GetActiveObjects(1)
print splines

for i in splines:
    parent = i.GetUp()
    c4d.CallCommand(5116) #insert extrude object
    extrude = doc.GetActiveObjects(1)[0]
    extrude[c4d.ID_BASELIST_NAME] = 'splineExtrude ' + str(count)
    extrude[c4d.EXTRUDEOBJECT_MOVE] = c4d.Vector(0, 0, 20)    
    
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
    
c4d.EventAdd()
