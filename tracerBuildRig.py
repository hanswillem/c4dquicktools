import c4d

nulls = doc.GetActiveObjects(2)

#put nulls in order of viewportselection
for i in nulls:
    i.Remove()
for i in nulls:
    doc.InsertObject(i)
    
#create tracer
doc.SetSelection(nulls[0], c4d.SELECTION_NEW)

for i in range(1, len(nulls)):
    doc.SetSelection(nulls[i], c4d.SELECTION_ADD)
    
c4d.CallCommand(1018655, 1018655)
tracer = doc.GetActiveObject()
tracer[c4d.MGTRACEROBJECT_MODE] = 1
tracer[c4d.SPLINEOBJECT_TYPE] = 2
tracer[c4d.SPLINEOBJECT_INTERPOLATION] = 3
tracer[c4d.SPLINEOBJECT_ANGLE] = 0

#store global position of nulls
allgp = []
for i in nulls:
    allgp.append(i.GetMg())

#create hierarchy
nullNrs = range(1, len(nulls))
nullNrs.reverse()
for i in nullNrs:
    nulls[i].InsertUnder(nulls[i-1])

#restore global position of nulls
for i in range(len(nulls)):
    nulls[i].SetMg(allgp[i])


#rename joints
for i in range(len(nulls)):
    nulls[i].SetName('joint')

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
sel = doc.SetSelection(nulls[-1], c4d.SELECTION_ADD)

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
