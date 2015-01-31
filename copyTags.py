"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R16.021

Name-US:Copy Tags
Description-US:Copies one ore more tags to other objects
"""

import c4d
doc.StartUndo()

def removeDoublesFromList(l):
    nl = []
    for i in l:
        if i not in nl:
            nl.append(i)
    return nl

objs = doc.GetActiveObjects(1)
tags = doc.GetActiveTags()
tags.reverse()
tagObjs = [i.GetObject() for i in tags]
tagObjs = removeDoublesFromList(tagObjs)
objs = [i for i in objs if i not in tagObjs]

for i in objs:
    for j in tags:
        c = j.GetClone()
        i.InsertTag(c)
        doc.AddUndo(c4d.UNDOTYPE_NEW, c)

c4d.EventAdd()
doc.EndUndo()
