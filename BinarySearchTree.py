# autor: Jana Oravcová
# uloha: 6. domace zadanie tree_sort

class BVS:
    class Vrchol:
        def __init__(self, data, left=None, right=None):
            if type(data) is int or type(data) is str:
                self.data = data
            if type(data) is tuple or type(data) is list:
                self.data = data[0]
            self.left = left
            self.right = right
            self.rest = [data]

    def __init__(self, postupnost=None):
        self.root = None
        for prvok in postupnost:
            self.vloz(prvok)
             
                    
    def vloz(self, data):
        root = self.Vrchol(data)
        if isinstance(data, list) or isinstance(data,tuple):
            _data = data[0]
        else:
            _data = data
        pom  = self.root
        node = None
        while pom:
            node = pom
            if _data<node.data:
                pom = pom.left
            else:
                if _data==node.data:
                    pom.rest.append(data)
                    return
                pom = pom.right
        if node is None:
            self.root = root
        else:
            if _data<node.data:
                node.left = root
            else:
                node.right = root
                
    def duplicate(self,data):
        q = []
        q.append(self.root)
        while q!=[]:
            node = q.pop()
            if node.data == data:
                return True
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return False
    def inorder_list(self):
        zoz = []
        stack = []
        current = self.root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if len(stack)>0:
                    node = stack.pop()
                    for n in range(len(node.rest)):
                        zoz.append(node.rest[n])
                    current = node.right
                else:
                    break
                
        return zoz

def tree_sort(zoznam):
    return BVS(zoznam).inorder_list()


if __name__ == '__main__':
    zoz = (10, 20, 30, 5, 15,15,10,5,20)
    print(tree_sort(zoz))
    zoz = [(10,), (20,), (30,), (5,), (15,)]
    print(tree_sort(zoz))
    zoz = [('b',6), ('d',7), ('e',8), ('a',9), ('b',10), ('b',1), ('d',2), ('e',3), ('a',4), ('b',5),('a',4),('a',4),('a',4)]
    print(tree_sort(zoz))
    zoz = ['prvy', ('druhy',), ['treti'], ('stvrty', 1),
           ['piaty', 2], ('siesty', 'x'), ['siedmy', 'y']]
    print(tree_sort(zoz))
