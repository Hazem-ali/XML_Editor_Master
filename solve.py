from xml_private_functions import Bring_Data, checkErrors


def solveAll(errors, tokenPlus):

    ##### Syntax solution #####
    solvedText = __solveSyntax(tokenPlus)

    solvedText = __solveOrder(solvedText)
    # # Another Check
    # errorsAndNewTokens = checkErrors(solvedText)
    # errors = errorsAndNewTokens[0]
    # tokenPlus = errorsAndNewTokens[1]

    # # filter miss order
    # missOrderErrors = []
    # for error in errors:
    #     if(error):
    #         error['type'] == 'missOrder'
    #         missOrderErrors.append(error)
    # solvedText = _solveOrder(missOrderErrors, tokenPlus)


    # # Final Check
    # errorsAndNewTokens = checkErrors(solvedText)
    # solvedText = _getString(errorsAndNewTokens[1])
    # errors = errorsAndNewTokens[0]

    return solvedText # solved


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

def __solveSyntax(File_Content):
    fCheck_List = []
    fCheck_IndexList = []
    fCheck_TagList = []
    indexerr = []
    Index = 0
    for char in(File_Content):
        if(char == '<'):
            if len(fCheck_List) == 0:
                fCheck_List.append(char)
                fCheck_IndexList.append(Index)
            else :
                fCheck_List.pop()
                fCheck_List.append(char)
                start=fCheck_IndexList[-1]
                x = (start,Index-1)
                indexerr.append(x)
                # File_Content = File_Content[:Index] + '>' + File_Content[Index:]
                if(File_Content[Index-1] == ' '):
                    File_Content = File_Content[:Index-1] + '>' + File_Content[Index-1:]
                else:
                    File_Content = File_Content[:Index] + '>' + File_Content[Index:]
                #print(File_Content[start:Index-1])
                if File_Content[start+1] == '/':
                    fCheck_TagList.pop()
                    fCheck_IndexList.pop()
                else :
                    fCheck_IndexList.append(Index)
                    tagStr = File_Content[start+1: Index]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                    fCheck_TagList.append(tagStr)
                #Index = Index + 1
        elif(char == '>') :
            if len(fCheck_List) != 0 :
                fCheck_List.pop()
                TopIndex = fCheck_IndexList[-1]
                if File_Content[Index-1] == '/':
                    fCheck_IndexList.pop()
                    continue
                elif File_Content[TopIndex + 1] == '/':
                    fCheck_IndexList.pop()
                    #TopIndex = fCheck_IndexList.pop()
                    if(len(fCheck_TagList) != 0) :
                        TopTag = fCheck_TagList[-1]
                        if TopTag != File_Content[TopIndex + 2 : Index] :
                            EndIndex = fCheck_IndexList.pop()
                            StartIndex = fCheck_IndexList.pop()
                            x = (StartIndex,EndIndex)
                            indexerr.append(x)
                            #print(File_Content[StartIndex:EndIndex+1])
                            #print(File_Content[StartIndex:EndIndex])
                            # ADD = '</' + TopTag + '>'
                            # if(File_Content[EndIndex+1]) == '<': 
                            #     File_Content = File_Content[:TopIndex] + ADD + File_Content[TopIndex:]
                            #     fCheck_TagList.pop()
                            #     Index = TopIndex+3+len(ADD)-1
                            # else :
                            #     M = EndIndex+1
                            #     while File_Content[M] != '<':
                            #         M = M+1
                            #     File_Content = File_Content[:M] + ADD + File_Content[M:]
                            #     fCheck_TagList.pop()
                            #     Index = TopIndex+3+len(ADD)-1
                        else :
                            fCheck_TagList.pop()
                            fCheck_IndexList.pop()
                            fCheck_IndexList.pop()
                    else :
                        x = (TopIndex,Index)
                        indexerr.append(x)
                        #print(File_Content[TopIndex:Index])
                        # if File_Content[TopIndex-1] == '>':
                        #       File_Content = File_Content[0: TopIndex:] + File_Content[Index + 1::]
                        # # else:
                        #     A = TopIndex
                        #     ADD = '<' + File_Content[TopIndex + 2 : Index] + '>'
                        #     while (File_Content[A] != '>'):
                        #         A = A-1
                        #     File_Content = File_Content[:A+1] + ADD + File_Content[A+1:]
                        # Index = Index-1
                        #print(File_Content[TopIndex:Index+1])
                else:
                    fCheck_IndexList.append(Index)
                    tagStr = File_Content[TopIndex + 1 : Index]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                    fCheck_TagList.append(tagStr)
            else :
                #x = (Index,Index)
                #indexerr.append(x)
            
                j = Index-1
                while (File_Content[j] != '>') and (File_Content[j] != '/')  :
                    if j == 0:
                        break
                    j = j-1
                if(File_Content[j] == '>'):
                    x = (j+1,Index)
                    indexerr.append(x)
                    #print(File_Content[j+1:Index+1])
                    File_Content = File_Content[:j+1] + '<' + File_Content[j+1:]
                    fCheck_IndexList.append(j+1)
                    fCheck_IndexList.append(Index)
                    tagStr = File_Content[j+2: Index+1]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                    fCheck_TagList.append(tagStr)
                    #print(tagStr)
                elif(File_Content[j] == '/'):
                    x = (j,Index)
                    indexerr.append(x)
                    #print(File_Content[j:Index+1])
                    File_Content = File_Content[:j] + '<' + File_Content[j:]
                    fCheck_TagList.pop()    
                elif j == 0:
                    x = (j,Index)
                    indexerr.append(x)
                    #print(File_Content[j:Index+1])
                    File_Content = File_Content[:j] + '<' + File_Content[j:]
                    fCheck_IndexList.append(j)
                    fCheck_IndexList.append(Index+1)
                    tagStr = File_Content[j+1: Index+1]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                    fCheck_TagList.append(tagStr)
                    #print(tagStr)
                Index = Index + 1
        Index = Index + 1
    if len(fCheck_List) != 0:
        TopIndex = fCheck_IndexList.pop()
        x = (TopIndex,Index)
        indexerr.append(x)
        #print(File_Content[TopIndex:Index+1])
        File_Content = File_Content[:Index+1] + '>' + File_Content[Index+1:]
        #print(File_Content)
        #print(indexerr)
    return File_Content

def __solveOrder(File_Content):
    fCheck_List = []
    fCheck_IndexList = []
    fCheck_TagList = []
    indexerr = []
    Index = 0
    while Index in range(len(File_Content)):
        if(File_Content[Index] == '<'):
            if len(fCheck_List) == 0:
                fCheck_List.append(File_Content[Index])
                fCheck_IndexList.append(Index)
            else :
                TopIndex = fCheck_List.pop()
                fCheck_List.append(File_Content[Index])
                start=fCheck_IndexList[-1]
                x = (start,Index-1)
                indexerr.append(x)
                if(File_Content[Index-1] == ' '):
                    File_Content = File_Content[:Index-1] + '>' + File_Content[Index-1:]
                else:
                    File_Content = File_Content[:Index] + '>' + File_Content[Index:]
                #File_Content = File_Content[:Index] + '>' + File_Content[Index:]
                print(File_Content[start:Index-1])
                if File_Content[start+1] == '/':
                    fCheck_TagList.pop()
                    fCheck_IndexList.pop()
                else :
                    fCheck_IndexList.append(Index)
                    tagStr = File_Content[start+1: Index]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                    fCheck_TagList.append(tagStr)
                #Index = Index + 1
        elif(File_Content[Index] == '>') :
            if len(fCheck_List) != 0 :
                fCheck_List.pop()
                TopIndex = fCheck_IndexList[-1]
                if File_Content[Index-1] == '/':
                    fCheck_IndexList.pop()
                    continue
                elif File_Content[TopIndex + 1] == '/':
                    fCheck_IndexList.pop()
                    #TopIndex = fCheck_IndexList.pop()
                    if(len(fCheck_TagList) != 0) :
                        TopTag = fCheck_TagList[-1]
                        if TopTag != File_Content[TopIndex + 2 : Index] :
                            EndIndex = fCheck_IndexList.pop()
                            StartIndex = fCheck_IndexList.pop()
                            ADD = '</' + TopTag + '>'
                            File_Condition = File_Content[:EndIndex+1].rstrip() + File_Content[EndIndex+1:]
                            if File_Condition[EndIndex+1] == '<': 
                                File_Content = File_Content[:TopIndex] + ADD + File_Content[TopIndex:]
                                fCheck_TagList.pop()
                                #Index = Index - (3+len(ADD)-1)
                            elif File_Content[EndIndex+1] != '<' :
                                M = EndIndex+1
                                while File_Content[M] != '<':
                                    M = M+1
                                File_Content = File_Content[:M] + ADD + File_Content[M:]
                                fCheck_TagList.pop()
                                # Index = Index - (3+len(ADD)-1)
                        else :
                            fCheck_TagList.pop()
                            fCheck_IndexList.pop()
                            fCheck_IndexList.pop()
                    else :
                        x = (TopIndex,Index)
                        indexerr.append(x)
                        #print(File_Content[TopIndex:Index])
                        #if File_Content[TopIndex-1] == '>':
                              #File_Content = File_Content[0: TopIndex:] + File_Content[Index + 1::]
                        #else:
                            #A = TopIndex
                            #ADD = '<' + File_Content[TopIndex + 2 : Index] + '>'
                            #while (File_Content[A] != '>'):
                                #A = A-1
                            #File_Content = File_Content[:A+1] + ADD + File_Content[A+1:]
                        #Index = Index-1
                        #print(File_Content[TopIndex:Index+1])
                else:
                    fCheck_IndexList.append(Index)
                    tagStr = File_Content[TopIndex + 1 : Index]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                    fCheck_TagList.append(tagStr)
           
        Index = Index + 1
    if len(fCheck_List) != 0:
        TopIndex = fCheck_IndexList.pop()
        x = (TopIndex,Index)
        indexerr.append(x)
        #print(File_Content[TopIndex:Index+1])
        File_Content = File_Content[:Index] + '>' + File_Content[Index:]
        #print(File_Content)
        #print(indexerr)
    return File_Content

    
    

# ss = Bring_Data('ss.txt')
# errorsWithTokens = checkErrors(ss)
# #print(errorsWithTokens[0])
# print( solveAll(errorsWithTokens[0],errorsWithTokens[1])[0] )