import c4d
from c4d import gui

txtInput = gui.RenameDialog('0-75')
keyFrameRangeStart = int(txtInput.split('-')[0])
keyFrameRangeEnd = int(txtInput.split('-')[1])

allObjs = doc.GetActiveObjects(1)
headObj = allObjs[0]
childObjs = allObjs[1:]

for i in range(keyFrameRangeStart, keyFrameRangeEnd):
    #set playhead
    doc.SetTime(c4d.BaseTime(i, doc.GetFps()))
    
    #get head tracks
    hxTrack = headObj.FindCTrack(c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0)))
    hyTrack = headObj.FindCTrack(c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 1), c4d.DescLevel(c4d.VECTOR_Y, c4d.DTYPE_REAL, 0)))

    #get head curves
    hxCurve = hxTrack.GetCurve()
    hyCurve = hyTrack.GetCurve()

    #get head start x,y
    hsx = hxCurve.GetValue(c4d.BaseTime(0, doc.GetFps()), doc.GetFps())
    hsy = hyCurve.GetValue(c4d.BaseTime(0, doc.GetFps()), doc.GetFps())
    ##get head current x,y
    hx = hxCurve.GetValue(c4d.BaseTime(i, doc.GetFps()), doc.GetFps())
    hy = hyCurve.GetValue(c4d.BaseTime(i, doc.GetFps()), doc.GetFps())

    headVector = c4d.Vector(hx, hy, 0)

    for j in childObjs:
        #get tracks
        xTrack = j.FindCTrack(c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0)))
        yTrack = j.FindCTrack(c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 1), c4d.DescLevel(c4d.VECTOR_Y, c4d.DTYPE_REAL, 0)))

        #get curves
        xCurve = xTrack.GetCurve()
        yCurve = yTrack.GetCurve()

        #get x,y
        x = xCurve.GetValue(c4d.BaseTime(i, doc.GetFps()), doc.GetFps())
        y = yCurve.GetValue(c4d.BaseTime(i, doc.GetFps()), doc.GetFps())
        childVector = c4d.Vector(x, y, 0)

        newPos = childVector - headVector

        #set x
        nx = newPos[0]
        xKeydict = xCurve.AddKey(c4d.BaseTime(i, doc.GetFps()))
        xKey = xKeydict["key"]
        xKey.SetValue(xCurve, nx)
        
        #set y
        ny = newPos[1]
        yKeydict = yCurve.AddKey(c4d.BaseTime(i, doc.GetFps()))
        yKey = yKeydict["key"]
        yKey.SetValue(yCurve, ny)

        j.InsertUnder(headObj)
