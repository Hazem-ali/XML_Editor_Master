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
                File_Content = File_Content[:Index] + '>' + File_Content[Index:]
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
                            print(File_Content[StartIndex:EndIndex+1])
                            #print(File_Content[StartIndex:EndIndex])
                            #ADD = '</' + TopTag + '>'
                            #if(File_Content[EndIndex+1]) == '<': 
                                #File_Content = File_Content[:TopIndex] + ADD + File_Content[TopIndex:]
                                #fCheck_TagList.pop()
                                #Index = TopIndex+3+len(ADD)-1
                            #else :
                                #M = EndIndex+1
                                #while File_Content[M] != '<':
                                    #M = M+1
                                #File_Content = File_Content[:M] + ADD + File_Content[M:]
                                #fCheck_TagList.pop()
                                #Index = TopIndex+3+len(ADD)-1
                        else :
                            fCheck_TagList.pop()
                            fCheck_IndexList.pop()
                            fCheck_IndexList.pop()
                    else :
                        x = (TopIndex,Index)
                        indexerr.append(x)
                        print(File_Content[TopIndex:Index])
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
                    print(File_Content[j+1:Index+1])
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
                    print(File_Content[j:Index+1])
                    File_Content = File_Content[:j] + '<' + File_Content[j:]
                    fCheck_TagList.pop()    
                elif j == 0:
                    x = (j,Index)
                    indexerr.append(x)
                    print(File_Content[j:Index+1])
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
        print(File_Content[TopIndex:Index+1])
        File_Content = File_Content[:Index] + '>' + File_Content[Index:]
        print(File_Content)
        print(indexerr)
#if(Inconsistent == False):
    #print("consistent")

