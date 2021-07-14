import re

########## FUNCTIONS ###########


def getRepeatedArray(x) -> list:
    rep = []
    lastItem = None
    array = []

    for item in x:
        if(str(item.tag).find('"') == -1):
            currentItemTag = str(item.tag)
        else:
            currentItemTag = str(item.tag).split(' ', 1)[0]+'>'

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
        hh = re.search("<\?.*\?>|<!--.*-->", xmlStr)
        if(hh):
            hh = hh.group(0)
            xmlStr = xmlStr.replace(hh, '')
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
    xmlStr = x
    xmlStr = xmlStr.split()
    xmlStr = ' '.join(xmlStr)
    return xmlStr

# get tokens with index {"token","index"} #


def getTokensPlus(string):
    tokens = stringToTokens(string)
    tokensPlus = []
    for token in tokens:
        index = str(string).replace(' ', '').find(str(token).replace(' ', ''))
        tokensPlus.append({"token": token, "beginIndex": index})

    return tokensPlus


# Check Errors Function #
def checkErrors(string):
    tokensPlus = getTokensPlus(string)
    errors = []

    for item in tokensPlus:
        token = str(item['token'])
        beginIndex = int(item['beginIndex'])

        ###### Syntax Error Cases #####
        if(token[0] == '<' and token[-1] != '>'):
            errors.append(
                {"position": (beginIndex, (beginIndex + len(token))),
                 "type": "syntax"}
            )

        if(token[0] != '<' and token[-1] == '>'):
            errors.append(
                {"position": (beginIndex, (beginIndex + len(token))),
                 "type": "syntax"}
            )

    ####### Ordering Errors #######
    stack = []
    i = 0
    while(i < len(tokensPlus)):
        item = tokensPlus[i]

        # Opening tag #
        if(item['token'][1] != '/' and item['token'][0] == '<' and item['token'][-2] != '/'):
            item['tagType'] = 'opening'
            stack.append(item)

        # Closing tag #
        elif(item['token'][1] == '/'):
            item['tagType'] = 'closing'

            # if empty stack
            if(len(stack)==0):
                beginIndex = item['beginIndex']
                token = item['token']
                errors.append(
                    {"position": (beginIndex, (beginIndex + len(token))),
                        "type": "missOrder"}
                )
                i+=1
                continue

            # if not empty
            popedItem = stack.pop()

            # poped is data #
            if(popedItem['token'][0] != '<'):
                popedItem = stack.pop()  # pop opening tag

            test1 = str(popedItem['token']).split(' ', 1)[0]
            test1 = test1.replace('<', '')
            test1 = test1.replace('>', '')

            test2 = str(item['token'])
            test2 = test2.replace('</', '')
            test2 = test2.replace('>', '')

            print("tests", test1, test2)
            if(test1 != test2):
                beginIndex = popedItem['beginIndex']
                token = popedItem['token']
                errors.append(
                    {"position": (beginIndex, (beginIndex + len(token))),
                        "type": "missOrder"}
                )
                i -= 1

        # Self Closing tag #
        elif(item['token'][-2] == '/'):
            item['tagType'] = 'selfClosing'

        # Data #
        else:
            item['tagType'] = 'data'
            stack.append(item)
        i += 1  # increament iterator

    # left items in stack #
    for item in stack:
        beginIndex = item['beginIndex']
        token = item['token']
        errors.append(
            {"position": (beginIndex, (beginIndex + len(token))),
                "type": "missOrder"}
        )

    return errors


# ss = Bring_Data('ss.txt')
# print(checkErrors(ss))
