class Node:
    def __init__(self, tag=None, data=None, parent=None) -> None:
        self.tag = tag
        self.closingTag=None
        self.data = data
        self.children = []
        self.parent = parent
        self.visited = False

    def setData(self, data):
        self.data = data

    def show(self):

        print(f'[{self.tag}, {self.data}]')
        for node in self.children:
            node.show()

    def toXml(self, x='', taps='') -> str:
        if(self.tag is None or self.visited):
            return ''
        self.visited = True
        x += taps+self.tag
        if(not self.data):
            taps += '\t'
            x += '\n'
        else:
            x += self.data

        for node in self.children:
            x += node.toXml(taps=taps)
            x+='\n'

        taps = taps[:-1]
        if(not self.data): x+=taps

        x += self.closingTag
        
        return x


class Xml:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, array):
        self.root.tag = array.pop(0)
        self.root.closingTag = array.pop()
        temp = self.root
        stack = []
        for item in array:
            if(item[1] != '/' and item[0] == '<'):
                stack.append(item)
                node = Node(parent=temp, tag=item)
                temp.children.append(node)
                temp = node
            elif(item[1] == '/'):
                popedItem = stack.pop()
                if(popedItem[0] != '<'):
                    temp.setData(popedItem)
                temp.closingTag=item
                temp = temp.parent
            else:
                stack.append(item)

    def show(self):
        self.root.show()

    def toXml(self):
        x = ''
        taps = ''
        return self.root.toXml(x, taps)


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
print(rr.toXml())
