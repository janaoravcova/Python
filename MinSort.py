# autor: Jana Oravcová
# uloha: 7. domace zadanie min_sort
class Zoznam:
    class Vrchol:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self, postupnost):
        self.zac = self.Vrchol(None)
        node = self.zac
        for prvok in postupnost:
            node.next = self.Vrchol(prvok)
            node = node.next
    def prechod(self, prvy, reverse):
        pos = prvy.next
        if reverse:
            while pos.next is not None:
                if prvy.next.data < pos.next.data:
                    prvy.next, pos.next = pos.next, prvy.next
                    prvy.next.next, pos.next.next = pos.next.next, prvy.next.next
                else:
                    pos = pos.next
        else:
            while pos.next is not None:
                if prvy.next.data > pos.next.data:
                    prvy.next, pos.next = pos.next, prvy.next
                    prvy.next.next, pos.next.next = pos.next.next, prvy.next.next
                else:
                    pos = pos.next
    def min_sort(self, reverse):
        prvy = self.zac
        #print(self.daj_zoznam())
        while prvy.next is not None:
            self.prechod(prvy, reverse)
            prvy = prvy.next
    def daj_zoznam(self):
        result =[]
        node = self.zac
        while node:
            result.append(node.data)
            node = node.next
        return result[1:]

def min_sort(postupnost, reverse=False):
    z = Zoznam(postupnost)
    z.min_sort(reverse)
    return z.daj_zoznam()
if __name__ == '__main__':
    post = (4, 30, 8, 31, 48, 19)
    zoz = min_sort(post)
    print(zoz)

    post = 'kohutik jaraby nechod do zahrady'.split()
    zoz = min_sort(post, reverse=True)
    print(zoz)
