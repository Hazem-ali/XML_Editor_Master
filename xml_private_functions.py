########## FUNCTIONS ###########
def getRepeatedArray(x) -> list:
    rep = []
    lastItem = None
    array = []
    if(not x) : x
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
