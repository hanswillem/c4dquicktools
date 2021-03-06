"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.032
Name-US:Glitch Obj
Description-US:Glitches the current scene by exporting it as .obj and randomising the data.
"""

import c4d
import random

#set paths, stating the obvious but change these paths to match your machine
exportedFile = '/Users/gewoonsander/Documents/glitchobj/modelExport.obj'
glitchedFile = '/Users/gewoonsander/Documents/glitchobj/modelGlitched.obj'

#save doc as obj
c4d.documents.SaveDocument(doc, exportedFile ,c4d.SAVEDOCUMENTFLAGS_0, 1030178)

#remove all objects from scene
c4d.CallCommand(100004766) #select all objects
for i in doc.GetActiveObjects(1):
    i.Remove()

#change numbers in obj file
count = 0
f = open(exportedFile)
fn = open(glitchedFile, 'w')
for l in f:
    if count % 10 == 0:
        rn1 = random.choice(range(10))
        rn2 = random.choice(range(10))
        l = [rn1 if i == str(rn2) else i for i in l] #pick random numbers and change them in other random numbers
        #l = [0 if i == 'f' else i for i in l] #remove faces
        l = [str(i) for i in l]
    fn.write(''.join(l))
    count = count + 1

#save file and reopen in c4d (merge with current doc)
f.close()
fn.close()
c4d.documents.MergeDocument(doc, glitchedFile, c4d.SCENEFILTER_OBJECTS, None)

#clean up scene
c4d.CallCommand(12168) #remove unused materials
c4d.CallCommand(100004766) #select all objects
for i in doc.GetActiveObjects(1):
    for j in i.GetTags():
        if j.GetType() == 5711:
            j.Remove()

c4d.EventAdd()
