
"""
Copyright: Hans Willem Gijzel (hanswillemgijzel@gmail.com)
C4D R17.048

Name-US:Set MP Filepath
Description-US:Sets the multipass filepath to the same directory as the regular filepath, replaces 'beauty' with 'mp'
"""

import c4d

#function to replace beauty with mp in the filename
def repl(str):
    l = str.split('/')
    nf = '';

    for i in range(len(l) - 1):
        nf += l[i]
        nf += '/'

    return nf + l[-1].replace('beauty', 'mp')


rd = doc.GetActiveRenderData()

#set filepath
originalImagePath = rd[c4d.RDATA_PATH] 
multiPassImage = repl(originalImagePath)

#set image format
rd[c4d.RDATA_MULTIPASS_FILENAME] = multiPassImage
rd[c4d.RDATA_MULTIPASS_SAVEFORMAT] = rd[c4d.RDATA_FORMAT]

c4d.EventAdd()