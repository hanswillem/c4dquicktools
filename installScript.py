"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R18

Name-US:Install Script
Description-US:Copies the selected python script to the scripts folder
"""

import c4d
import shutil
import os

def main():
    scriptFullPath = c4d.storage.LoadDialog()
    scriptFile = os.path.basename(scriptFullPath)
    scriptFileExt =  os.path.splitext(scriptFile)[1]
    
    iconFullPath = os.path.dirname(scriptFullPath)
    iconFile = os.path.splitext(scriptFile)[0] + '.tif'
    iconFullPath = os.path.join(iconFullPath, iconFile)

    pathToScriptsScriptFile = c4d.storage.GeGetC4DPath(1)[:-6] + '/library/scripts/' + scriptFile
    pathToScriptsIconFile = c4d.storage.GeGetC4DPath(1)[:-6] + '/library/scripts/' + iconFile

    if scriptFileExt == '.py':   
        shutil.copyfile(scriptFullPath, pathToScriptsScriptFile)
        if os.path.isfile(iconFullPath):
            shutil.copyfile(iconFullPath, pathToScriptsIconFile)
            c4d.gui.MessageDialog('Script and icon installed!')
        else:
            c4d.gui.MessageDialog('Script installed!')
    else:
        c4d.gui.MessageDialog('Select a python file!')


if __name__ == '__main__':
    main()
