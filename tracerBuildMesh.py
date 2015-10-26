"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.032

Name-US:Tracer Build Mesh
Description-US:Builds a mesh from the tracer rig
"""

#The script needs a tracer rig's group null to be selected for it to work properly.
#It creates a sweep object based on the group null and a rectangle.

import c4d
doc.StartUndo()

obj = op
sweep = c4d.BaseObject(c4d.Osweep)
sweep.InsertUnder(obj)
doc.AddUndo(c4d.UNDOTYPE_NEW, sweep)#*****UNDO*****
tracer = [i for i in obj.GetChildren() if i.GetType() == 1018655][0]
doc.AddUndo(c4d.UNDOTYPE_CHANGE, tracer)#*****UNDO*****
tracer.InsertUnder(sweep)
rect = c4d.BaseObject(c4d.Osplinerectangle)
rect[c4d.PRIM_RECTANGLE_WIDTH] = 15
rect[c4d.PRIM_RECTANGLE_HEIGHT] = 15
rect.InsertUnder(sweep)
doc.AddUndo(c4d.UNDOTYPE_NEW, rect)#*****UNDO*****

c4d.EventAdd()
doc.EndUndo()
