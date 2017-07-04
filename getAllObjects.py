import c4d


#recursively get all objects in the scene
def getAllObjects():
    
    def itterateHierarchy(obj):
        objects.append(obj)
        if obj.GetDown() != None:
            itterateHierarchy(obj.GetDown())
        if obj.GetNext() != None:
            itterateHierarchy(obj.GetNext())

    objects = []
    itterateHierarchy(doc.GetFirstObject())
    return objects


allObjs = getAllObjects()
