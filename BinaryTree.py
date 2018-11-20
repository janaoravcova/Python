# autor: Jana Oravcová
# uloha: 4. domace zadanie binarny strom

class Vrchol:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def pridaj_vrchol(koren, riadok):
    if koren is None:
        koren = Vrchol(None)
    if riadok is not None:
        if ':' not in riadok:
            koren.data = riadok
        elif riadok[-1] == ':':
            koren.data = riadok[:-1]
        else:
            ret=riadok.split(':')[1]
            cesta=[]
            for znak in ret:
                if znak in 'lL' or znak in 'Rr':
                    cesta.append(znak)
            meno = riadok.split(':')[0]
            vrchol = koren
            if cesta==[]:
                vrchol.data  = riadok.split(':')[0]
            while True and cesta:
                krok = cesta.pop(0)
                if krok in 'Ll':
                    if cesta == []:
                        if isinstance(vrchol.left, Vrchol):
                            vrchol.left.data = meno
                        else:
                            vrchol.left = Vrchol(meno)
                        return koren
                    elif cesta != []:
                        if isinstance(vrchol.left, Vrchol):
                            vrchol = vrchol.left
                        else :
                            vrchol.left = Vrchol(None)
                            vrchol = vrchol.left
                else:
                    if cesta == []:
                        if isinstance(vrchol.right, Vrchol):
                            vrchol.right.data = meno
                        else:
                            vrchol.right = Vrchol(meno)
                        return koren
                    elif cesta != []:
                        if isinstance(vrchol.right, Vrchol):
                            vrchol = vrchol.right
                        else :
                            vrchol.right = Vrchol(None)
                            vrchol = vrchol.right
    return koren

def vytvor_strom(meno_suboru):
    vrchol = None
    try:
        with open(meno_suboru, 'r') as s:
            riadok=s.readline()
            while riadok!="":
                vrchol = pridaj_vrchol(vrchol,riadok)
                riadok=s.readline()
    except:
        pass
    return vrchol

def zapis_strom_do_suboru(koren, meno_suboru):
    #"{0:b}".format(int) decimal to binary
    cesta = ''
    queue = [(cesta,koren)]
    with open (meno_suboru, 'w') as s:
        if koren is None:
            return
        while queue:
            cesta, vrchol = queue.pop()
            if vrchol.left is not None:
                cesta=cesta+'l'
                queue.append((cesta,vrchol.left))
                cesta = cesta[:-1]
            if vrchol.right is not None:
                cesta = cesta + 'r'
                queue.append((cesta,vrchol.right))
                cesta = cesta[:-1]
            if vrchol.data is not None:
                if cesta=='':
                    print(str(vrchol.data), file=s)
                else:
                    print(str(vrchol.data) + ':' + cesta, file=s)

def pocet(koren):
    if koren is None:
        return 0,0
    queue = []
    queue.append(koren)        
    count,empty = 0,0 
    while(len(queue) > 0):
        node = queue.pop(0)
        if node is not None:
            if node.data:
                count = count+1
            else:
                empty = empty + 1
        if node.left is not None:
            queue.append(node.left)
 
        if node.right is not None:
            queue.append(node.right)
             
    return count, count+empty
if __name__ == '__main__':
    s = pridaj_vrchol(None, 'syn vlavo:syn vlavo')
    s = pridaj_vrchol(s, 'syn vlavo:syn vlavo')
    s = pridaj_vrchol(s, 'otec:otec')
    s = pridaj_vrchol(s, 'syn vpravo:syn vpravo')
    zapis_strom_do_suboru(s, 'strom4.txt')
    s = pridaj_vrchol(s, 'x     y: L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L')
    zapis_strom_do_suboru(s, 'strom5.txt')
    pocet(s)
    s = vytvor_strom('subor4_0.txt')
    print(pocet(s))
