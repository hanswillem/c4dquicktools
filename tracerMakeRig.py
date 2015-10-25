import c4d

nulls = doc.GetActiveObjects(2)

#put nulls in order of viewportselection
for i in nulls:
    i.Remove()
for i in nulls:
    doc.InsertObject(i)
    

#create tracer
doc.SetSelection(nulls[0], c4d.SELECTION_NEW)
doc.SetSelection(nulls[1], c4d.SELECTION_ADD)
doc.SetSelection(nulls[2], c4d.SELECTION_ADD)
c4d.CallCommand(1018655, 1018655)
tracer = doc.GetActiveObject()
tracer[c4d.MGTRACEROBJECT_MODE] = 1
tracer[c4d.SPLINEOBJECT_TYPE] = 2
tracer[c4d.SPLINEOBJECT_INTERPOLATION] = 3
tracer[c4d.SPLINEOBJECT_ANGLE] = 0


#create hierarchy
gp0 = nulls[0].GetMg()
gp1 = nulls[1].GetMg()
gp2 = nulls[2].GetMg()

nulls[2].InsertUnder(nulls[1])
nulls[1].InsertUnder(nulls[0])

nulls[0].SetMg(gp0)
nulls[1].SetMg(gp1)
nulls[2].SetMg(gp2)

nulls[0].SetName('joint 01')
nulls[1].SetName('joint 02')
nulls[2].SetName('joint 03')

#make wrapper null
doc.SetSelection(nulls[0], c4d.SELECTION_NEW)
c4d.CallCommand(100004772) #group objects
wrapper = doc.GetActiveObject()
wrapper.SetName('group')
wrapper[c4d.NULLOBJECT_DISPLAY] = 2
wrapper[c4d.NULLOBJECT_RADIUS] = 50
wrapper[c4d.NULLOBJECT_ORIENTATION] = 3


#create ik tag
sel = doc.SetSelection(nulls[0], c4d.SELECTION_NEW)
sel = doc.SetSelection(nulls[2], c4d.SELECTION_ADD)

#create ik chain
c4d.CallCommand(1019884, 1019884)
goal = doc.GetActiveObject()
goal[c4d.NULLOBJECT_DISPLAY] = 11
goal[c4d.NULLOBJECT_ORIENTATION] = 1
goal[c4d.NULLOBJECT_RADIUS] = 25
goal.SetName('goal')

#put tracer in wrapper
tracer.InsertUnder(wrapper)


c4d.EventAdd()
