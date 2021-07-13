########## FUNCTIONS ###########
def getRepeatedArray(x) -> list:
    rep = []
    lastItem = None
    array = []
    if(not x):
        x
    for item in x:
        if(not lastItem is None and item.tag != lastItem.tag):
            rep.append(array)
            array = []
            array.append(item)
        else:
            array.append(item)
        lastItem = item

    if array:
        rep.append(array)

    return rep


def Bring_Data(filename):
    with open(filename, 'r') as f:
        return f.read()


def stringToTokens(string) -> list:
    xmlStr = string
    xmlStr = xmlStr.split()
    xmlStr = ' '.join(xmlStr)
    xmlStr = xmlStr.replace('<', '?<')
    xmlStr = xmlStr.replace('>', '>?')
    xmlStr = xmlStr.split('?')
    for item in xmlStr:
        if(item == ' ' or item == ''):
            xmlStr.remove(item)
    return xmlStr
