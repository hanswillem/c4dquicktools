import c4d
from c4d import gui
import urllib
import zipfile
import os
import shutil

def main():

    confirm = gui.QuestionDialog('Download and install scripts from github?')

    if confirm:

        # c4d script folder
        scriptFolder = c4d.storage.GeGetC4DPath(1)[:-6] + '/library/scripts/'


        # download github repo
        url = 'https://github.com/hanswillem/c4dquicktools/archive/master.zip'
        targetDir = '/Users/gewoonsander/Desktop/'
        target = targetDir + '/master.zip'
        urllib.urlretrieve(url, target)


        # unzip
        zip_ref = zipfile.ZipFile(target, mode='r')
        zip_ref.extractall(targetDir)
        zip_ref.close()
        extractdDir = '/Users/gewoonsander/Desktop/c4dquicktools-master'


        # copy
        allScriptFiles = [f for f in os.listdir(extractdDir) if os.path.splitext(f)[1] == '.py' or os.path.splitext(f)[1] == '.tif']
        for i in allScriptFiles:
            fullPath = os.path.join(extractdDir, i)
            fullPathTarget = os.path.join(scriptFolder, i)
            shutil.copy(fullPath, fullPathTarget)


        # clean up
        os.remove(target)
        shutil.rmtree(extractdDir)


        # message
        c4d.gui.MessageDialog('Scripts downloaded and installed!')


if __name__ == '__main__':
    main()
