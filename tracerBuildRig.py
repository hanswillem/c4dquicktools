"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.032

Name-US:Tracer Build Rig
Description-US:Builds a tracer rig from the selected tracer joints
"""

#The script needs three or more nulls to be selected to work properly. 
#It builds a rig with controls from the selected nulls using a tracer object.
#The order in which the nulls are selected before running the script determine the start and end of the hierarchy of the rig

import c4d
doc.StartUndo()

nulls = doc.GetActiveObjects(2)
    
#create tracer object
tracer = c4d.BaseObject(1018655)
doc.InsertObject(tracer)
doc.AddUndo(c4d.UNDOTYPE_NEW, tracer) #*****UNDO*****
tracerList = tracer[c4d.MGTRACEROBJECT_OBJECTLIST]
for i in nulls:  
    tracerList.InsertObject(i, 0)
tracer[c4d.MGTRACEROBJECT_OBJECTLIST] = tracerList
tracer[c4d.MGTRACEROBJECT_MODE] = 1
tracer[c4d.SPLINEOBJECT_TYPE] = 2
tracer[c4d.SPLINEOBJECT_INTERPOLATION] = 3
tracer[c4d.SPLINEOBJECT_ANGLE] = 0

#store global position of nulls
allgp = []
for i in nulls:
    allgp.append(i.GetMg())

#create hierarchy of nulls
nullNrs = range(1, len(nulls))
nullNrs.reverse()
for i in nullNrs:
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, nulls[i]) #*****UNDO*****
    nulls[i].InsertUnder(nulls[i-1])

#restore global position of nulls
for i in range(len(nulls)):
    nulls[i].SetMg(allgp[i])

#rename nulls
for i in range(len(nulls)):
    nulls[i].SetName('joint')

#make group null
group = c4d.BaseObject(5140)
group.SetMg(allgp[0])
doc.AddUndo(c4d.UNDOTYPE_CHANGE, nulls[0]) #*****UNDO*****
nulls[0].InsertUnder(group)
nulls[0].SetMg(allgp[0])
group.SetName('group')
group[c4d.NULLOBJECT_DISPLAY] = 2
group[c4d.NULLOBJECT_RADIUS] = 50
group[c4d.NULLOBJECT_ORIENTATION] = 3
doc.InsertObject(group)
doc.AddUndo(c4d.UNDOTYPE_NEW, group) #*****UNDO*****

#put tracer in group
tracer.InsertUnder(group)

#create ik chain
iktag = c4d.BaseTag(1019561)
iktag[c4d.ID_CA_IK_TAG_TIP] = nulls[-1]
nulls[0].InsertTag(iktag)
doc.AddUndo(c4d.UNDOTYPE_NEW, iktag) #*****UNDO*****
#create goal
goal = c4d.BaseObject(5140)
goal.SetMg(allgp[-1])
goal[c4d.NULLOBJECT_DISPLAY] = 11
goal[c4d.NULLOBJECT_ORIENTATION] = 1
goal[c4d.NULLOBJECT_RADIUS] = 25
goal.SetName('goal')
doc.InsertObject(goal)
doc.AddUndo(c4d.UNDOTYPE_NEW, goal) #*****UNDO*****
iktag[c4d.ID_CA_IK_TAG_TARGET] = goal

c4d.EventAdd()
doc.EndUndo()
