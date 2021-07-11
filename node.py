####### Node Class Used in XML Class #######
class Node:
    def __init__(self, tag=None, data=None, parent=None) -> None:
        self.tag = tag
        self.closingTag = None
        self.data = data
        self.children = []
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

    def toJson(self, jsonText='', taps='\t'):
        if(self.tag is None or self.visited):
            return ''
        self.visited = True  # Mark as visited to not print again

        #### Opening ####
        jsonText += taps+"\"" + self.tag + "\":"  # " adding ("") to all"
        if(not self.data):
            jsonText += '{'  # add tap { for parents only
        # add data or another opening tag #
        if(self.data):
            jsonText += "\"" + self.data + "\""
        else:
            taps += '\t'
            jsonText += '\n'

        #### Children ####
        # Sort Every Children Array
        self.children = sorted(self.children,key=lambda child:child.tag )

        # Add the children recurrsively #
        for node in self.children:
            jsonText += node.toJson(taps=taps)
            jsonText += '\n'  # new line after each child

        #### Closing ####
        taps = taps[:-1]  # decrease number of taps after finish this children
        if(not self.data):
            jsonText += taps  # put taps before closing tag
            jsonText += "}"  # put the closing tag

        return jsonText
