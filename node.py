from xml_private_functions import getRepeatedArray

####### Node Class Used in XML Class #######
class Node:
    def __init__(self, tag=None, data=None, parent=None, closingTag=None) -> None:
        self.tag = tag
        self.closingTag = closingTag
        self.data = data
        self.children = []
        self.attrChildren= []
        self.parent = parent
        self.visited = False

    # Setter for data attr #
    def setData(self, data):
        self.data = data

    # Show the Tree for Testing #
    def show(self):

        print(f'[{self.tag}, {self.data}]')
        for node in self.children:
            node.show()

    # Convert the Node Recursively to xml text #

    def toXml(self, xmlText='', taps='') -> str:
        if(self.tag is None or self.visited):
            return ''
        self.visited = True  # Mark as visited to not print again

        #### Opening ####
        xmlText += taps+self.tag  # add tap and opening tag

        # add data or another opening tag #
        if(self.data):
            xmlText += self.data
        else:
            taps += '\t'
            xmlText += '\n'

        #### Children ####
        # Add the children recurrsively #
        for node in self.children:
            xmlText += node.toXml(taps=taps)
            xmlText += '\n'  # new line after each child

        ##### Closing #####
        taps = taps[:-1]  # decrease number of taps after finish this children
        if(not self.data):
            xmlText += taps  # put taps before closing tag

        xmlText += self.closingTag  # put the closing tag

        return xmlText


    # Convert the Node Recursively to JSON text #
    def toJson(self, jsonText='', taps='\t',isArray=False,childIndex=0,lastChild=False):
        if(self.tag is None or self.visited):
            return ''
        self.visited = True  # Mark as visited to not print again

       
        correctedTag = self.tag.split(' ',1)[0]
        if(not isArray):
            #### Normal Opening ####
            jsonText += taps+"\"" + correctedTag + "\":"  # " adding ("") to all"
            if(not self.data):
                jsonText += '{'  # add tap { for parents only
            # add data or another opening tag #
            if(self.data):
                jsonText += "\"" + self.data + "\","
            else:
                taps += '\t'
                jsonText += '\n'

        else:
            #### Array Opening ####
            if(not self.data):
                if(childIndex==0): jsonText += taps+"\"" + correctedTag + "\":[\n"+taps+" {"  # " adding ("") to all"
                else: jsonText+='\n'+taps+' {'  # " adding ("") to all"

                taps += '\t'
                jsonText += '\n'
            else:
                jsonText+='\n'+taps+' '+self.data+','
                taps += '\t'
                 
        #### Children ####
        # Sort Every Children Array
        self.children = sorted(self.children,key=lambda child:child.tag )
        self.children = getRepeatedArray(self.children)
        # Add the children recurrsively #
        for node in self.children:
            if(len(node) == 1):
                jsonText += node[0].toJson(taps=taps)
                jsonText += '\n'  # new line after each child
            else:
                for index,nodeChild in enumerate(node):
                    lastElement = len(node)-1

                    jsonText += nodeChild.toJson(taps=taps,isArray=True,childIndex=index,lastChild=(lastElement==index))

        #### Closing ####
        taps = taps[:-1]  # decrease number of taps after finish this children
        if(not self.data):
            jsonText += taps  # put taps before closing tag
            if(not isArray) : jsonText += "}"  # put the closing tag
            else : jsonText += " },"  # put the closing tag

        if(isArray and lastChild):
            #jsonText += taps  # put taps before closing tag
            jsonText = jsonText[:-1]
            jsonText += "\n"+taps+"],\n"  # put the closing tag
        return jsonText


    # To Clear visited item after every method #
    def clearVisited(self):
        self.visited = False
        for item in self.children:
            item.clearVisited()
