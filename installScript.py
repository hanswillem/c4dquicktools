import c4d
import shutil
import os



# import webbrowser

# url = 'https://github.com/hanswillem/c4dquicktools/archive/master.zip'
# webbrowser.open_new_tab(url)


scriptFullPath = c4d.storage.LoadDialog()
scriptFile = os.path.basename(scriptFullPath)

iconFullPath = os.path.dirname(scriptFullPath)
iconFile = os.path.splitext(scriptFile)[0] + '.tif'
iconFullPath = os.path.join(iconFullPath, iconFile)

pathToScriptsScriptFile = c4d.storage.GeGetC4DPath(1)[:-6] + '/library/scripts/' + scriptFile
pathToScriptsIconFile = c4d.storage.GeGetC4DPath(1)[:-6] + '/library/scripts/' + iconFile

shutil.copyfile(scriptFullPath, pathToScriptsScriptFile)

if os.path.isfile(iconFullPath):
    shutil.copyfile(iconFullPath, pathToScriptsIconFile)




c4d.gui.MessageDialog('Script installed!')