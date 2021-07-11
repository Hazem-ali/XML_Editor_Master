########## FUNCTIONS ###########
def getRepeatedArray(x) -> list:
    rep = []
    lastItem = None
    array = []
    
    for item in x:
        if(item != lastItem and not lastItem is None):
            rep.append(array)
            array = []
            array.append(item)
        else:
            array.append(item)
        lastItem = item

    if array:
        rep.append(array)

    return rep
