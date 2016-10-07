import c4d


def main():
    objs = doc.GetActiveObjects(1)
    for i in objs:
        metaBall = c4d.BaseObject(5125)
        metaBall[c4d.METABALLOBJECT_THRESHOLD] = 3.5
        metaBall[c4d.METABALLOBJECT_SUBEDITOR] = 15
        metaBall[c4d.METABALLOBJECT_SUBRAY] = 1
        
        phongTag = c4d.BaseTag(c4d.Tphong)
        metaBall.InsertTag(phongTag)
    
        moSpline = c4d.BaseObject(440000054)
        moSpline[c4d.MGMOSPLINEOBJECT_MODE] = 1
        moSpline[c4d.MGMOSPLINEOBJECT_SOURCE_SPLINE] = i
        
        doc.InsertObject(metaBall)
        moSpline.InsertUnder(metaBall)
        
        c4d.EventAdd()

if __name__ == '__main__':
    main()