import c4d

c4d.CallCommand(100004766) # Select All
objs = doc.GetActiveObjects(1)
c4d.CallCommand(100004767) # Deselect All
l = []
n = []

for i in objs:
    for j in i.GetTags():
        if j.GetType() == 5637:
            if j[c4d.COMPOSITINGTAG_ENABLECHN0] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD)
                if j[c4d.COMPOSITINGTAG_IDCHN0] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN0])
                if i.GetName() not in n:
                    n.append(i.GetName())
                    
            if j[c4d.COMPOSITINGTAG_ENABLECHN1] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN1] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN1])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN2] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN2] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN2])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN3] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN3] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN3])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN4] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN4] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN4])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN5] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN5] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN5])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN6] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN6] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN6])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN7] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN7] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN7])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN8] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN8] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN8])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN9] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN9] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN9])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN10] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN10] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN10])
                if i.GetName() not in n:
                    n.append(i.GetName())

            if j[c4d.COMPOSITINGTAG_ENABLECHN11] == 1:
                doc.SetSelection(i, c4d.SELECTION_ADD)
                doc.SetSelection(j, c4d.SELECTION_ADD) 
                if j[c4d.COMPOSITINGTAG_IDCHN11] not in l:
                    l.append(j[c4d.COMPOSITINGTAG_IDCHN11])
                if i.GetName() not in n:
                    n.append(i.GetName())

print 'objects: ' + str(n)
print 'buffers: ' + str(l)
c4d.EventAdd()