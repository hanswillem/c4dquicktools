import c4d

nulls = doc.GetActiveObjects(2)

#create tracer
doc.AddUndo(c4d.UNDOTYPE_CHANGE, nulls[0])
c4d.CallCommand(1018655, 1018655)
tracer = doc.GetActiveObject()
tracer[c4d.MGTRACEROBJECT_MODE] = 1

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

c4d.EventAdd()
