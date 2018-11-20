# autor: Jana Oravcová
# uloha: 5. domace zadanie Rodokmen

##import tkinter
##canvas = tkinter.Canvas(width=1500, height=800)
##canvas.pack()

class FamilyTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    class Queue:
        def __init__(self):
            self._prvky = []

        def is_empty(self):
            return self._prvky == []

        def enqueue(self, data):
            '''na koniec radu vlozi novu hodnotu'''
            self._prvky.append(data)

        def dequeue(self):
            '''zo zaciatku radu vyberie prvu hodnotu, alebo vyvola EmptyError'''
            if self.is_empty():
                raise EmptyError('prazdny rad')
            return self._prvky.pop(0)


    # ----------------------------

    def __init__(self, meno_suboru):
        self.root = None
        self.tuples = {}
        self.sons = set()
        self.fathers = set()
        self.count = 0
        self.create_tree(meno_suboru)
        
##    def kresli(self, v,sir, x, y):
##        if v.left is not None:
##            canvas.create_line(x, y, x-sir/2, y+40)
##            self.kresli(v.left, sir/2, x-sir/2, y+40)
##        if v.right is not None:
##            canvas.create_line(x, y, x+sir/2, y+40)
##            self.kresli(v.right, sir/2, x+sir/2, y+40)
##        canvas.create_oval(x-15, y-15, x+15, y+15, fill='white')
##        if v.data == 'Gapeevig':
##            canvas.create_text(x, y, text=v.data, fill='red')
##        else:
##            canvas.create_text(x, y, text=v.data, font='consolas 12 bold')
   
    def create_tree(self, meno_suboru):
        with open(meno_suboru, 'r') as file:
            family = file.read().split('\n')
            for members in family:
                if members!='':
                    father,son = members.split('-')
                    self.fathers.add(father)
                    if father in self.tuples:
                        second_son = self.tuples[father]
                        self.tuples[father] = (son, second_son)
                    else:
                        self.tuples[father] = son
                    self.sons.add(son)
            self.root = self.Node(list(self.fathers  - self.sons)[0])
            #print(self.root.data)
        queue = self.Queue()
        queue.enqueue(self.root)#vlozime koren
        while not queue.is_empty():
            father = queue.dequeue()
            left_son, right_son = None, None
            try:
                children = self.tuples[father.data]
                if isinstance(children,tuple):
                    left_son = children[0]
                    right_son = children[1]
                else:
                    left_son = children
            except KeyError:
                pass
            if left_son is not None:
                father.left = self.Node(left_son)
                #self.count+=1
                queue.enqueue(father.left)
            if right_son is not None:
                father.right = self.Node(right_son)
                #self.count+=1
                queue.enqueue(father.right)
        #self.kresli(self.root,500,500,40)

    def __len__(self):
        q = self.Queue()
        q.enqueue(self.root)
        l = 0
        while not q.is_empty():
            node = q.dequeue()
            l+=1
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return l  
    def lenght(self, root):
        q = self.Queue()
        q.enqueue(root)
        l = 0
        while not q.is_empty():
            node = q.dequeue()
            l+=1
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return l
    def depth(self, data):
        q = [(self.root, 0)]
        lower = 0
        height = 0
        if self.root.data == data:
            return 0
        while q != []:
            node, level = q.pop(0)
            #spracuj
            if lower != level:
                height +=1
            lower = level
            if node.left is not None:
                if node.left.data == data:
                    return height+1
                q.append((node.left, level+1))
            if node.right is not None:
                if node.right.data == data:
                    return height+1
                q.append((node.right, level+1))
        return None

    def height(self):
        q = [(self.root, 0)]
        lower = 0
        height = 0
        while q != []:
            node, level = q.pop(0)
            if lower != level:
                height +=1
            lower = level
            if node.left is not None:
                q.append((node.left, level+1))
            if node.right is not None:
                q.append((node.right, level+1))
        return height

    def width(self):  
        q = self.Queue()
        q.enqueue(self.root)
        q.enqueue(None)
        _max = 0
        width_local = 0
        level = 0
        while not q.is_empty():
            node = q.dequeue()
            if node is None:
                if not q.is_empty():
                    q.enqueue(None)
                if width_local>_max:
                    _max = width_local
                    level = width_local
                width_local = 0
                level +=1
            else:
                if node.left is not None:
                    q.enqueue(node.left)
                if node.right is not None:
                    q.enqueue(node.right)
                width_local +=1
        return _max
                    
    def subtree_num(self, data):
        if data == self.root.data:
            return len(self)
        q = self.Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            node = q.dequeue()
            if node.data == data:
                return self.lenght(node)
            else:
                if node.left is not None:
                    q.enqueue(node.left)
                if node.right is not None:
                    q.enqueue(node.right)
        return 0
    def descendant(self, data1, data2):
        q = self.Queue()
        q.enqueue(self.root)
        ancestor = None
        while not q.is_empty():
            node = q.dequeue()
            if node.data == data1:
                ancestor = node
                break
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        if ancestor is None:
            return False
        q = self.Queue()#podstrom s korenom s predkom ktoreho potomka hladame
        if ancestor.right is not None:
            q.enqueue(ancestor.right)
        if ancestor.left is not None:
            q.enqueue(ancestor.left)
        while not q.is_empty():
            descen = q.dequeue()
            if descen.data == data2:
                return True
            if descen.left is not None:
                q.enqueue(descen.left)
            if descen.right is not None:
                q.enqueue(descen.right)
        return False
            
        
    def level_set(self, k):
        q = [(self.root, 0)]
        lower = 0
        height = 0
        nodes = set()
##        if k == 0:
##            return {self.root.data}
##        if k>self.lenght(self.root):
##            return set()
        while q != []:
            node, level = q.pop(0)
            if k == level:
                nodes.add(node.data)
            lower = level
            if node.left is not None:
                q.append((node.left, level+1))
            if node.right is not None:
                q.append((node.right, level+1))
        return nodes

    def leaves_num(self):
        q = [(self.root, 0)]
        lower = 0
        leaves = 0
        while q != []:
            node, level = q.pop(0)
            if node.left is None and node.right is None:
                leaves +=1
            if node.left is not None:
                q.append((node.left, level+1))
            if node.right is not None:
                q.append((node.right, level+1))
        return leaves
if __name__ == '__main__':
    f = FamilyTree('subor5.txt')
    print('pocet vrcholov =', len(f))
    print('podstrom pre Miroslav =', f.subtree_num('Miroslav'))
    print('podstrom pre Robert =', f.subtree_num('Robert'))
    print('vyska =', f.height())
    print('sirka =', f.width())
    print('hlbka vrcholu Vlastimil =', f.depth('Vlastimil'))
    print('Miroslav ma potomka Bohuslav =', f.descendant('Miroslav','Bohuslav'))
    print('Jaroslav ma potomka Svatopluk =', f.descendant('Jaroslav','Svatopluk'))
    print('vrcholy na urovni 2 =', f.level_set(2))
    print('vrcholy na urovni 10 =', f.level_set(10))
    print('pocet listov =', f.leaves_num())
