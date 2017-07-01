import c4d
from c4d import gui

joints = []


#Get all joints (recursively!) and store there global matrices
def getAllJoints(obj):
    for i in obj.GetChildren():
        joints.append([i, i.GetMg()])
        getAllJoints(i)


#unparent the joints
def unparent():
    root = doc.GetActiveObject()
    getAllJoints(root)
 
    for i in joints:
        i[0].InsertUnder(root)
        i[0].SetMg(i[1])
         
        c4d.EventAdd()


#reparent the joits
def reparent():    
    root = doc.GetActiveObject()
    getAllJoints(root)
    
    for i in range(len(joints)):
        if i == 0:
            joints[i][0].InsertUnder(root)
            joints[i][0].SetMg(joints[i][1])
        else:
            joints[i][0].InsertUnder(joints[i - 1][0])
            joints[i][0].SetMg(joints[i][1])

        c4d.EventAdd()



#unparent()
reparent()
