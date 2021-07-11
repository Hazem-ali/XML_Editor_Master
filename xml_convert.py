from node import Node

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
                nodePointer = nodePointer.parent  # Return to the node previous parent
            # Data #
            else:
                stack.append(item)

    # show all nodes #
    def show(self):
        self.root.show()

    # Convert Xml Tree to simplify XML Text #
    def toXml(self):
        return self.root.toXml()

     # Convert Xml Tree to simplify JSON #
    def toJson(self):
        json = '{\n'+self.root.toJson()+'\t\n}'
        json = json.replace('<', '')
        json = json.replace('>', '')
        return json


########## TESTING ###########
rr = Xml()
input = [
    "<xml id='xx1'>",
    '<prod>',
    '<name>',
    '<first>',
    'Hossam',
    '</first>',
    '<second id="ss">',
    'Momooo',
    '</second>',
    '<a>',
    'www.facebook.com',
    '</a>',
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
    '<prod>',
    '<name>',
    '<first>',
    'Hossam',
    '</first>',
    '<second id="ss">',
    'Momooo',
    '</second>',
    '<a>',
    'www.facebook.com',
    '</a>',
    '</name>',
    '<id>',
    '112',
    '</id>',
    '</prod>',
    '<naa>',
    'hhh',
    '</naa>',
    '<xnxx>',
    '<ko>',
    'no',
    '</ko>',
    '</xnxx>',
    "</xml>"
]

rr.insert(input)
print(rr.toJson())


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


        
