"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.032

Name-US:Tracer Add Joint
Description-US:Adds a tracer joint
"""

#The script adds a null to the scene and sets it's display type to sphere.'
#It is meant to work together with the "Tracer Build Rig script" and the "Tracer Build Mesh" script.

import c4d
doc.StartUndo()

joint = c4d.BaseObject(c4d.Onull)
joint[c4d.NULLOBJECT_DISPLAY] = 13
joint[c4d.NULLOBJECT_ORIENTATION] = 1
joint.SetName('joint')
doc.InsertObject(joint)
doc.SetSelection(joint, c4d.SELECTION_NEW)
doc.AddUndo(c4d.UNDOTYPE_NEW, joint) #*****UNDO*****

c4d.EventAdd()
doc.EndUndo()
