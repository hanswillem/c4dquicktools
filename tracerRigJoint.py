import c4d

null = c4d.BaseObject(c4d.Onull)
null[c4d.NULLOBJECT_DISPLAY] = 13
null[c4d.NULLOBJECT_ORIENTATION] = 1
null.SetName('joint')
doc.InsertObject(null)
doc.SetSelection(null, c4d.SELECTION_NEW)

c4d.EventAdd()
