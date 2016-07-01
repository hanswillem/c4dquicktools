"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.048

Name-US:NOM Setup Ropes
Description-US:Turns selected splines into meshes
"""


import c4d
from c4d import gui

doc.StartUndo() #undo

def setupPointCache(n):
    objs = doc.GetActiveObjects(1)
    for i in objs:
        
        #setup cylinder
        parent = i.GetUp()
        cyl = c4d.BaseObject(5170)
        cyl[c4d.PRIM_CYLINDER_RADIUS] = n
        cyl[c4d.PRIM_CYLINDER_HSUB] = 50        
        if parent != None:
            cyl.InsertUnder(parent)
        else:
            doc.InsertObject(cyl)
        doc.AddUndo(c4d.UNDOTYPE_NEW, cyl) #undo
        
        #setup phong tag
        phongTag = c4d.BaseTag(5612)
        cyl.InsertTag(phongTag)

        #setup point cache tag
        cacheTag = c4d.BaseTag(1021302)
        cyl.InsertTag(cacheTag)

        #setup spline wrap
        splWrap = c4d.BaseObject(1019221)
        splWrap[c4d.MGSPLINEWRAPDEFORMER_SPLINE] = i
        splWrap[c4d.MGSPLINEWRAPDEFORMER_AXIS] = 2
        splWrap.InsertUnder(cyl)

    c4d.EventAdd()
    doc.EndUndo() #undo


userInput = gui.RenameDialog('thickness')
if userInput != None:
    userInput = float(userInput)
    setupPointCache(userInput)