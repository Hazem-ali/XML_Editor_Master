import re

########## FUNCTIONS ###########
def getRepeatedArray(x) -> list:
    rep = []
    lastItem = None
    array = []
    
    for item in x:
        if( str(item.tag).find('"') == -1 ):
            currentItemTag = str(item.tag)
        else:
            currentItemTag = str(item.tag).split(' ',1)[0]+'>'

        if(not lastItem is None and currentItemTag != lastItem):
            rep.append(array)
            array = []
            array.append(item)
        else:
            array.append(item)
        lastItem = currentItemTag

    if array:
        rep.append(array)

    return rep


def Bring_Data(filename):
    with open(filename, 'r') as f:
        return f.read()


def stringToTokens(string) -> list:
    xmlStr = str(string)
    
    xmlStr = minify(xmlStr)
    
    # remove ?>
    while(1):
        hh = re.search("<\?.*\?>|<!--.*-->",xmlStr)
        if(hh): 
            hh=hh.group(0)
            xmlStr = xmlStr.replace(hh,'')
        else:
            break

    xmlStr = xmlStr.replace('<', '?hossam?<')
    xmlStr = xmlStr.replace('>', '>?hossam?')
    xmlStr = xmlStr.split('?hossam?')
    for item in xmlStr:
        if(item == ' ' or item == ''):
            xmlStr.remove(item)
    return xmlStr


def extractTagAttr(tag) -> list:
    # <name id=" h123" ref="12301 02" >

    if(str(tag).find('"') == -1):
        return []
    correctedTag = str(tag).split(' ', 1)[1]
    correctedTag = correctedTag.replace('>', '')

    attrs = []
    counter = 0
    formedAttr = ""
    for char in correctedTag:
        if(char == "\"" or char == "'"):
            counter += 1
        if(counter > 0 or char != ' '):
            formedAttr += char
        if(counter == 2):
            attrs.append(formedAttr)
            formedAttr = ""
            counter = 0
    nodes = []
    for item in attrs:
        item = str(item).replace('="', '?hossam?')
        item = str(item).replace("='", '?hossam?')
        item = str(item).replace('"', '')
        itemData = item.split('?hossam?')
        node = {"tag": itemData[0], "data": itemData[1]}
        nodes.append(node)

    return nodes

def minify(x):
    xmlStr=x
    xmlStr = xmlStr.split()
    xmlStr = ' '.join(xmlStr)
    return xmlStr
