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

        xmlText += taps+self.tag  # add tap and opening tag

        # add data of another opening tag #
        if(self.data):
            xmlText += self.data
        else:
            taps += '\t'
            xmlText += '\n'

        # Add the children recurrsively #
        for node in self.children:
            xmlText += node.toXml(taps=taps)
            xmlText += '\n'  # new line after each child

        taps = taps[:-1]  # decrease number of taps after finish this children

        if(not self.data):
            xmlText += taps  # put taps before closing tag
        xmlText += self.closingTag  # put the closing tag

        return xmlText

####### XML Class implemented by Nodes #######
class Xml:
    def __init__(self) -> None:
        self.root = Node()

    # Fill the XML tree with a List #
    def insert(self, array):
        self.root.tag = array.pop(0)
        self.root.closingTag = array.pop()
        nodePointer = self.root
        stack = []
        for item in array:
            # Opening tag #
            if(item[1] != '/' and item[0] == '<'):
                stack.append(item)
                node = Node(parent=nodePointer, tag=item)
                nodePointer.children.append(node)
                nodePointer = node
            # Closing tag #
            elif(item[1] == '/'):
                popedItem = stack.pop()
                if(popedItem[0] != '<'):
                    nodePointer.setData(popedItem)
                nodePointer.closingTag = item
                nodePointer = nodePointer.parent #Return to the node previous parent
            # Data #
            else:
                stack.append(item)

    # show all nodes #
    def show(self):
        self.root.show()

    # Convert Xml Tree to simplify XML Text #
    def toXml(self):
        xmlText = ''
        taps = ''
        return self.root.toXml(xmlText, taps)


########## TESTING ###########
rr = Xml()
input = [
    "<xml id='xx1'>",
    '<prod>',
    '<name>',
    '<first>',
    'Hossam',
    '</first>',
    '<second>',
    'Momooo',
    '</second>',
    '</name>',
    '<id>',
    '112',
    '</id>',
    '</prod>',
    '<prod>',
    '<name>',
    'Hassan',
    '</name>',
    '<id>',
    '011',
    '</id>',
    '</prod>',
    "</xml>"
]

rr.insert(input)
print(rr.toXml())

# rr.insert([
#     '<name>',
#     '<id>',
#     'Hossam',
#     '</id>',
#     '<id>',
#     'Bibo',
#     '</id>',
#     '</name',

# ])
# rr.show()
