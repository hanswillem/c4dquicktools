"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.048

Name-US:Focus Camera
Description-US:Adds a new camera with a focus object
"""

import c4d

doc.StartUndo()


#cam
cam = c4d.BaseObject(5103)


#focus
focus = c4d.BaseObject(5140)
focus.SetName('Focus Object')
focus.InsertUnder(cam)
doc.AddUndo(c4d.UNDOTYPE_NEW, focus) #*****UNDO*****
focus[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = 2000
focus[c4d.NULLOBJECT_DISPLAY] = 1
focus[c4d.NULLOBJECT_RADIUS] = 50
focus[c4d.NULLOBJECT_ORIENTATION] = 1


#put focus in cam
cam[c4d.CAMERAOBJECT_TARGETOBJECT] = focus


#get editorcam
bd = doc.GetActiveBaseDraw()
editorCam = bd.GetEditorCamera()


#set cam to editorcam
cam[c4d.ID_BASEOBJECT_REL_POSITION] = editorCam[c4d.ID_BASEOBJECT_REL_POSITION]
cam[c4d.ID_BASEOBJECT_REL_ROTATION] = editorCam[c4d.ID_BASEOBJECT_REL_ROTATION]
doc.InsertObject(cam)
doc.AddUndo(c4d.UNDOTYPE_NEW, cam) #*****UNDO*****


c4d.EventAdd()

doc.EndUndo()