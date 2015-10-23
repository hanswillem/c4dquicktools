import c4d

tag = c4d.BaseTag(c4d.Tpython)
op.InsertTag(tag)

tagCode = open('/Users/gewoonsander/Library/Preferences/MAXON/CINEMA 4D R17_89538A46/library/scripts/renderme.py', 'r')
tag[c4d.TPYTHON_CODE] = tagCode.read()

c4d.EventAdd()
