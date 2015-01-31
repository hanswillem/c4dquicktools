"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R16.021

Name-US:Duplicate Tags
Description-US:Duplicates selected tags
"""

import c4d

doc.StartUndo()

tags = doc.GetActiveTags()
for i in tags:
    obj = i.GetObject()
    c = i.GetClone()
    lastTag = obj.GetTags()[-1]
    obj.InsertTag(c, pred = lastTag)
    doc.AddUndo(c4d.UNDOTYPE_NEW, c)
    doc.SetSelection(i, c4d.SELECTION_SUB)

c4d.EventAdd()
doc.EndUndo()
