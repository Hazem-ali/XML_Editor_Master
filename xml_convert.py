from xml_private_functions import Bring_Data, extractTagAttr, stringToTokens
from node import Node

####### XML Class implemented by Nodes #######


class Xml:
    def __init__(self) -> None:
        self.root = Node()

    # Fill the XML tree with a List #
    def insert(self, string):
        array = stringToTokens(string)  # convert string to tokens

        firstTag = array.pop(0)
        self.root.tag = firstTag
        for item in extractTagAttr(firstTag):
            beginningNode = Node(parent=self.root, tag='@'+str(item['tag']), jsonData=item['data'], closingTag='')
            self.root.attrChildren.append(beginningNode)

        self.root.closingTag = array.pop()
        nodePointer = self.root
        stack = []
        for item in array:
            # Opening tag #
            if(item[1] != '/' and item[0] == '<' and item[-2] != '/'):
                stack.append(item)

                # Normal children insersion
                node = Node(parent=nodePointer, tag=item)
                nodePointer.children.append(node)
                nodePointer = node

                # Attributes children insersion
                attrs = extractTagAttr(node.tag)
                for item in attrs:
                    openingTag = '@'+str(item['tag'])
                    data = item['data']
                    attrNode = Node(
                        parent=nodePointer, tag=openingTag, jsonData=data, closingTag='')
                    nodePointer.attrChildren.append(attrNode)

            # Closing tag #
            elif(item[1] == '/'):
                popedItem = stack.pop()

                # Data item #
                if(popedItem[0] != '<'):
                    nodePointer.setData(popedItem)
                    if(not nodePointer.attrChildren):
                        nodePointer.jsonData = popedItem

                    # Adding #text attr #
                    if(nodePointer.data and attrs):
                        dataNode = Node(
                            parent=nodePointer, jsonData=nodePointer.data, tag='#text', closingTag='')
                        nodePointer.attrChildren.append(dataNode)

                nodePointer.closingTag = item
                nodePointer = nodePointer.parent  # Return to the node previous parent

            # Self Closing tag #
            elif(item[-2] == '/'):
                node = Node(parent=nodePointer, tag=item,
                            closingTag='', data='')
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
input = Bring_Data('data-sample.xml')

rr = Xml()
rr.insert(input)
# print(rr.toXml())
# print('_______________________________________________')
# print(rr.toJson())
