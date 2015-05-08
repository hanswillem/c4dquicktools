"""
Copyright: RedRum Bureau (www.redrumbureau.com)
C4D R16.038

Name-US:Render Layers
Description-US:Renders each layer as a seperate png file with alpha
"""

import c4d
from c4d import gui
import os.path

def main():
    #get layers
    layerRoot = doc.GetLayerObjectRoot()
    layers = layerRoot.GetChildren()

    if len(layers) < 1:
        gui.MessageDialog('There Are No Layers...')
    else:
        c4d.CallCommand(1029486) #open texture manager  
        c4d.CallCommand(1029813) #select all textures in texture manager
        c4d.CallCommand(1029820) #globalize filenames
        #get renderpath
        userFilePath = c4d.storage.SaveDialog()
        
        if userFilePath == None:
            pass
        else:
            renderPath = os.path.dirname(userFilePath)
            renderFile = os.path.basename(userFilePath)
            #if it not yet exists create temp folder
            if not os.path.exists(renderPath + '/_tmp files'):
                os.makedirs(renderPath + '/_tmp files')
            #get rendersettings    
            rd = doc.GetActiveRenderData()
            #get renderqueue
            rq = c4d.documents.GetBatchRender()
            rq.Open()
            cnt = 1
            
            #find light layer
            for i in layers:
                if i.GetName() == '_light':
                    lightLayer = i
                else:
                    lightLayer = None
 
            for i in layers:
                if i != lightLayer:
                    #un-solo all layers
                    for j in layers:
                        j[c4d.ID_LAYER_SOLO] = 0
                        #you need a callbutton command for this to work somehow...
                        c4d.CallButton(j, 100004726)
                    #solo layer
                    i[c4d.ID_LAYER_SOLO] = 1
                    c4d.CallButton(i, 100004726)
                    #solo light layer
                    if lightLayer != None:
                        lightLayer[c4d.ID_LAYER_SOLO] = 1
                        c4d.CallButton(i, 100004726)
                    c4d.EventAdd()
                    #set image path
                    rd[c4d.RDATA_PATH] = renderPath + '/' + "%02d" % (cnt,) + ' ' + renderFile + '_' + i.GetName() #beauty
                    rd[c4d.RDATA_MULTIPASS_FILENAME] =  renderPath + '/' + "%02d" % (cnt,) + ' ' + renderFile + '_' + i.GetName() + '_mp' #mp
                    #turn on alpha
                    rd[c4d.RDATA_ALPHACHANNEL] = 1
                    rd[c4d.RDATA_STRAIGHTALPHA] = 1
                    #set format to PNG
                    rd[c4d.RDATA_FORMAT] = 1023671 #beauty
                    rd[c4d.RDATA_MULTIPASS_SAVEFORMAT] = 1023671 #mp
                    #set frame range to current frame
                    rd[c4d.RDATA_FRAMESEQUENCE] = 1
                    #save the document
                    outputFile = renderPath + '/_tmp files/'  + "%02d" % (cnt,) + ' ' + renderFile + '_' + i.GetName()
                    c4d.documents.SaveDocument(doc, outputFile ,c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT)
                    #add the file to the renderqueue
                    rq.AddFile(outputFile, cnt)
                    c4d.EventAdd()
                    #next
                    cnt += 1
            
                #un-solo all layers
                for i in layers:
                    i[c4d.ID_LAYER_SOLO] = 0
                    c4d.CallButton(i, 100004726)
        
if __name__ == '__main__':
    main()
