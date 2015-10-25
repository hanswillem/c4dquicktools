"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.032

Name-US:Tracer Build Mesh
Description-US:Builds a mesh from the tracer rig
"""

import c4d

def makeSweep():
    sweep = c4d.BaseObject(c4d.Osweep)
    sweep.InsertUnder(objs[0])
    tracer = [i for i in objs[0].GetChildren() if i.GetType() == 1018655][0]
    tracer.InsertUnder(sweep)
    rect = c4d.BaseObject(c4d.Osplinerectangle)
    rect[c4d.PRIM_RECTANGLE_WIDTH] = 15
    rect[c4d.PRIM_RECTANGLE_HEIGHT] = 15
    rect.InsertUnder(sweep)

def makeWrapDeformer():
    group = objs[0]
    mesh = objs[1]
    tracer = [i for i in group.GetChildren() if i.GetType() == 1018655][0]
    splineWrap = c4d.BaseObject(1019221)
    splineWrap[c4d.MGSPLINEWRAPDEFORMER_SPLINE] = tracer
    splineWrap[c4d.MGSPLINEWRAPDEFORMER_AXIS] = 2
    splineWrap[c4d.MGSPLINEWRAPDEFORMER_LENMODE] = 1
    splineWrap[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
    splineWrap[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1
    splineWrap.InsertUnder(mesh)
    

objs = doc.GetActiveObjects(2)
if len(objs) == 1:
    makeSweep()
if len(objs) == 2:
    makeWrapDeformer()

c4d.EventAdd()
