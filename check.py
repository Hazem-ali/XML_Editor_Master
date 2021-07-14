from xml_private_functions import Bring_Data

def Check(File_Content):
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
                #print(File_Content[start:Index])
                if File_Content[start+1] == '/':
                    fCheck_TagList.pop()
                else :
                    fCheck_IndexList.append(Index)
                    tagStr = File_Content[start+1: Index]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                        fCheck_TagList.append(tagStr)
                    
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
                            fCheck_TagList.pop()
                        else :
                            fCheck_TagList.pop()
                            fCheck_IndexList.pop()
                            fCheck_IndexList.pop()
                    else :
                        x = (TopIndex,Index)
                        indexerr.append(x)
                        #print(File_Content[TopIndex:Index])
                       
                else:
                    fCheck_IndexList.append(Index)
                    tagStr = File_Content[TopIndex + 1 : Index]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                    fCheck_TagList.append(tagStr)
            else : 
                j = Index-1
                while (File_Content[j] != '>') and (File_Content[j] != '/')  :
                    if j == 0:
                        break
                    j = j-1
                if(File_Content[j] == '>'):
                    x = (j+1,Index)
                    indexerr.append(x)
                    #print(File_Content[j+1:Index+1])
                    fCheck_IndexList.append(j+1)
                    fCheck_IndexList.append(Index)
                    tagStr = File_Content[j+1: Index]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                    fCheck_TagList.append(tagStr)
                elif(File_Content[j] == '/'):
                    x = (j,Index)
                    indexerr.append(x)
                    #print(File_Content[j:Index+1])
                    fCheck_TagList.pop()    
                elif j == 0:
                    x = (j,Index)
                    indexerr.append(x)
                    #print(File_Content[j:Index+1])
                    fCheck_IndexList.append(j)
                    fCheck_IndexList.append(Index)
                    tagStr = File_Content[j: Index]
                    if(tagStr.find(' ') != -1):
                        tagStr = tagStr.split(' ')[0]
                    fCheck_TagList.append(tagStr)
        Index = Index + 1
    if len(fCheck_List) != 0:
        TopIndex = fCheck_IndexList.pop()
        x = (TopIndex,Index)
        indexerr.append(x)
        #print(File_Content[TopIndex:Index+1])
    while len(fCheck_IndexList) != 0:
        EndIndex = fCheck_IndexList.pop()
        StartIndex = fCheck_IndexList.pop()
        x = (StartIndex,EndIndex)
        indexerr.append(x)
        #print(File_Content[StartIndex:EndIndex+1])
    #print(File_Content)
    #print(indexerr)
    return indexerr
    

print(Check(Bring_Data('ss.txt')))
        


