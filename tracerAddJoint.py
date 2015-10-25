"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.032

Name-US:Tracer Add Joint
Description-US:Adds a tracer joint
"""

import c4d

null = c4d.BaseObject(c4d.Onull)
null[c4d.NULLOBJECT_DISPLAY] = 13
null[c4d.NULLOBJECT_ORIENTATION] = 1
null.SetName('joint')
doc.InsertObject(null)
doc.SetSelection(null, c4d.SELECTION_NEW)

c4d.EventAdd()
