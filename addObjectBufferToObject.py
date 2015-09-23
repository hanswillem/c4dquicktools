
"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R16.021

Name-US:Add Object Buffer
Description-US:Adds one or multiple object buffers to selected objects
"""

#quickly add one or more object buffers to an object
import c4d
from c4d import gui
doc.StartUndo()

#add object buffer(s) in redersettings
def addObjectBuffer(userInputNumbers):
    for i in userInputNumbers:
        renderSettings = doc.GetActiveRenderData()
        mp = renderSettings.GetFirstMultipass()
        used = []
        #check if buffer already in use
        while mp:
            if mp.GetTypeName() == 'Object Buffer':
                usedNumber = mp[c4d.MULTIPASSOBJECT_OBJECTBUFFER]
                used.append(usedNumber)
            mp = mp.GetNext()
        #add object buffer in rendersettings
        if int(i) not in used:
            obuffer = c4d.BaseList2D(c4d.Zmultipass)
            obuffer.GetDataInstance()[c4d.MULTIPASSOBJECT_TYPE] = c4d.VPBUFFER_OBJECTBUFFER
            obuffer[c4d.MULTIPASSOBJECT_OBJECTBUFFER] = int(i)
            obuffer.SetName('Object Buffer ' + i)
            renderSettings.InsertMultipass(obuffer)
            doc.AddUndo(c4d.UNDOTYPE_NEW, obuffer)
            #turn multipasses on in rendersettings
            renderSettings[c4d.RDATA_MULTIPASS_ENABLE] = True

#add compositing tag(s)
def addTag(objs):
    foundBuffers = []
    for i in objs:
        #if object already has a compositing tag
        existingTag = [j for j in i.GetTags() if j.GetType() == 5637]
        if len(existingTag) > 0:
            existingTag = existingTag[0]
            existingTagBuffers = []
            #get existing buffers in compositing tag
            try:
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN0] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN0])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN1] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN1])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN2] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN2])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN3] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN3])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN4] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN4])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN5] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN5])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN6] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN6])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN7] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN7])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN8] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN8])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN9] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN9])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN10] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN10])
                if existingTag[c4d.COMPOSITINGTAG_ENABLECHN11] == True:
                    existingTagBuffers.append(existingTag[c4d.COMPOSITINGTAG_IDCHN11])
            except IndexError:
                pass
            existingTagBuffers = [str(i) for i in existingTagBuffers]
            buffersToAdd = []
            for i in userInputNumbers:
                if i not in existingTagBuffers:
                    buffersToAdd.append(i)
            #0 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN0] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN0] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN0] = int(buffersToAdd[0])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN0] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 0:
                    buffersToAdd.append(buffersToAdd[0])
            #1 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN1] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN1] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN1] = int(buffersToAdd[1])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN1] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 1:
                    buffersToAdd.append(buffersToAdd[1])
            #2 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN2] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN2] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN2] = int(buffersToAdd[2])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN2] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 2:
                    buffersToAdd.append(buffersToAdd[2])
            #3 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN3] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN3] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN3] = int(buffersToAdd[3])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN3] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 3:
                    buffersToAdd.append(buffersToAdd[3])
            #4 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN4] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN4] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN4] = int(buffersToAdd[4])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN4] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 4:
                    buffersToAdd.append(buffersToAdd[4])
            #5 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN5] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN5] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN5] = int(buffersToAdd[5])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN5] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 5:
                    buffersToAdd.append(buffersToAdd[5])
            #6 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN6] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN6] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN6] = int(buffersToAdd[6])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN6] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 6:
                    buffersToAdd.append(buffersToAdd[6])
            #7 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN7] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN7] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN7] = int(buffersToAdd[7])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN7] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 7:
                    buffersToAdd.append(buffersToAdd[7])
            #8 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN8] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN8] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN8] = int(buffersToAdd[8])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN8] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 8:
                    buffersToAdd.append(buffersToAdd[8])
            #9 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN9] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN9] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN9] = int(buffersToAdd[9])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN9] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 9:
                    buffersToAdd.append(buffersToAdd[9])
            #10 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN10] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN10] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN10] = int(buffersToAdd[10])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN10] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 10:
                    buffersToAdd.append(buffersToAdd[10])
            #11 --------------------------------
            if existingTag[c4d.COMPOSITINGTAG_ENABLECHN11] == None or existingTag[c4d.COMPOSITINGTAG_ENABLECHN11] == False:
                try:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, existingTag)
                    existingTag[c4d.COMPOSITINGTAG_IDCHN11] = int(buffersToAdd[11])
                    existingTag[c4d.COMPOSITINGTAG_ENABLECHN11] = True
                except IndexError:
                    pass
            else:
                if len(buffersToAdd) > 11:
                    buffersToAdd.append(buffersToAdd[11])
        #if object has no compositing tag        
        else:
            newTag = c4d.BaseTag(c4d.Tcompositing)
            i.InsertTag(newTag)
            doc.AddUndo(c4d.UNDOTYPE_NEW, newTag)
            try:
                newTag[c4d.COMPOSITINGTAG_IDCHN0] = int(userInputNumbers[0])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN0] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN1] = int(userInputNumbers[1])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN1] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN2] = int(userInputNumbers[2])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN2] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN3] = int(userInputNumbers[3])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN3] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN4] = int(userInputNumbers[4])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN4] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN5] = int(userInputNumbers[5])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN5] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN6] = int(userInputNumbers[6])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN6] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN7] = int(userInputNumbers[7])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN7] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN8] = int(userInputNumbers[8])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN8] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN9] = int(userInputNumbers[9])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN9] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN10] = int(userInputNumbers[10])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN10] = True
                newTag[c4d.COMPOSITINGTAG_IDCHN11] = int(userInputNumbers[11])
                newTag[c4d.COMPOSITINGTAG_ENABLECHN11] = True
            except IndexError:
                pass

#remove double items from list (used to remove the doubles the user might enter)
def removeDoublesFromList(l):
    nl = []
    for i in l:
        if i not in nl:
            nl.append(i)
    return nl

userInput = gui.RenameDialog('type object buffer number')
if userInput != None:
    userInputNumbers = userInput.split(',')
    userInputNumbers = removeDoublesFromList(userInputNumbers)
    objs = doc.GetActiveObjects(1)
    addTag(objs)
    addObjectBuffer(userInputNumbers)

c4d.EventAdd()
doc.EndUndo()
