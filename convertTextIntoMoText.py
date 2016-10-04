import c4d

objs = doc.GetActiveObjects(1)

for i in objs:
    motext = c4d.BaseObject(1019268)
    motext.SetMg(i.GetMg())
    
    motext[c4d.PRIM_TEXT_TEXT] = i[c4d.PRIM_TEXT_TEXT]
    
    if i[c4d.PRIM_TEXT_FONT] is not None:
        motext[c4d.PRIM_TEXT_FONT] = i[c4d.PRIM_TEXT_FONT]

    motext[c4d.PRIM_TEXT_HEIGHT] = i[c4d.PRIM_TEXT_HEIGHT]

    parent = i.GetUp()
    if parent.GetType() == 5116:
        l = [parent[c4d.EXTRUDEOBJECT_MOVE][0], parent[c4d.EXTRUDEOBJECT_MOVE][1], parent[c4d.EXTRUDEOBJECT_MOVE][2]]
        extrudeDepth = max(l)
        motext[c4d.MGTEXTOBJECT_SPLINEMOVE] = extrudeDepth
    else:
        motext[c4d.MGTEXTOBJECT_SPLINEMOVE] = 1
    
    doc.InsertObject(motext)

c4d.EventAdd()