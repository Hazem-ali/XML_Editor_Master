from xml_private_functions import Bring_Data, extractTagAttr, stringToTokens
from node import Node

####### XML Class implemented by Nodes #######
class Xml:
    def __init__(self) -> None:
        self.root = Node()

    # Fill the XML tree with a List #
    def insert(self, string):
        array = stringToTokens(string) # convert string to tokens
        
        self.root.tag = array.pop(0)
        self.root.closingTag = array.pop()
        nodePointer = self.root
        stack = []
        for item in array:
            # Opening tag #
            if(item[1] != '/' and item[0] == '<' and item[-2]!='/'):
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

            # Self Closing tag #
            elif(item[-2]=='/'):
                node = Node(parent=nodePointer, tag=item, closingTag='',data='')
                nodePointer.children.append(node)

            # Data #
            else:
                stack.append(item)

    # show all nodes #
    def show(self):
        self.root.show()

    # Convert Xml Tree to simplify XML Text #
    def toXml(self):
        self.root.clearVisited()
        return self.root.toXml()

     # Convert Xml Tree to simplify JSON #
    def toJson(self):
        self.root.clearVisited()

        json = '{\n'+self.root.toJson()+'\t\n}'
        json = json.replace('<', '')
        json = json.replace('>', '')
        return json


########## TESTING ###########
input = Bring_Data('test1.txt')
print(stringToTokens(input))
print('_______________________________________________')

rr = Xml()
rr.insert(input)
print(rr.toXml())
print('_______________________________________________')
print(rr.toJson())

 
print(extractTagAttr("<name id=\"123\" ref='123 0221' ff=\"ssssssss dds df frs dds\">" ) )




        
