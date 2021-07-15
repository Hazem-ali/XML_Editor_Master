from xml_private_functions import Bring_Data, checkErrors


def solve(errors, tokenPlus):


    # filter syntax
    sytaxErrors = []
    for error in errors:
        if(error):
            error['type'] == 'syntax'
            sytaxErrors.append(error)
    solvedText = _solveSyntax(sytaxErrors, tokenPlus)

    # Another Check
    errorsAndNewTokens = checkErrors(solvedText)
    errors = errorsAndNewTokens[0]
    tokenPlus = errorsAndNewTokens[1]

    # # filter miss order
    # missOrderErrors = []
    # for error in errors:
    #     if(error):
    #         error['type'] == 'missOrder'
    #         missOrderErrors.append(error)
    # solvedText = _solveOrder(missOrderErrors, tokenPlus)

    # # Final Check
    # errorsAndNewTokens = checkErrors(solvedText)
    solvedText = _getString(errorsAndNewTokens[1])
    errors = errorsAndNewTokens[0]

    return (solvedText,errors) # solved + remaining errors

def _solveSyntax(errors, tokens) -> str:
    tokens = list(tokens)
    for error in errors:
        index = search(error['tag'],tokens)
        selectedToken = tokens[index]
        #####  #####
        if ( selectedToken['token'].find('<') != -1 ):
            selectedToken['token'] = '>'.join(selectedToken['token'].split(' ',1))
        elif ( selectedToken['token'].find('>') != -1 ):
            selectedToken['token'] = '<'.join(selectedToken['token'].split(' ',1))
    return _getString(tokens)


def _solveOrder(errors, tokens):
    ss


def _getString(tokens) -> str:
    normalTokens = []
    for token in tokens:
        normalTokens.append(token['token'])

    string = ' '.join(normalTokens)
    return string

def search(token,tokens):
    for item in enumerate(tokens):
        if(item[1]['token'] == token):
            return item[0]
    return -1



ss = Bring_Data('ss.txt')
errorsWithTokens = checkErrors(ss)
#print(errorsWithTokens[0])
print( solve(errorsWithTokens[0],errorsWithTokens[1]) )