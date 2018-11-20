# autor: Jana Oravcova
# uloha: 9. domace zadanie do_sirky
class Graf:
    def __init__(self, meno_suboru):
        self.vrcholy = {}
        with open(meno_suboru, 'r') as file:
            nodes = file.readline().strip().split()#vsetky vrcholy
            for node in nodes:
                self.vrcholy[node] = set()
            tuples = []
            line = file.readline().strip()
            while line!='':
                for el in line.split():
                    tuples.append(el)
                line = file.readline().strip()
            while tuples:
                first=tuples.pop(0)
                second=tuples.pop(0)
                self.vrcholy[first].add(second)
                self.vrcholy[second].add(first)
        
    def vo_vzdialenosti(self, v1, od, do=None):
        nodes = set()
        queue = [(v1,0)]
        visited = set()
        while queue:
            v1, level = queue.pop(0)
            if v1 not in visited:
                visited.add(v1)
                if do!=None:
                    if level>=od and level<=do:
                        nodes.add(v1)
                else:
                    if level + 1 == od:
                        print('b')
                    if level==od:
                        print('a')
                        nodes.add(v1)
                for v2 in self.vrcholy[v1]:
                    if v2 not in visited:
                        queue.append((v2,level+1))
        return nodes

    def max(self, v1):
        queue = [(v1, 0)]
        visited = set()
        v=v1
        while queue:
            v1, level = queue.pop(0)
            if v1 not in visited:
                visited.add(v1)
                for v2 in self.vrcholy[v1]:
                    if v2 not in visited:
                        queue.append((v2, level+1))
        return level, self.vo_vzdialenosti(v, level)


    def pocet_levelov(self,v):
        queue = [(v,0)]
        visited = set()
        while queue:
            v1, level = queue.pop(0)
            if v1 not in visited:
                visited.add(v1)
                for v2 in self.vrcholy[v1]:
                    if v2 not in visited:
                        queue.append((v2,level+1))
        return level

    
    def vsetky(self, v1):
        zoznam = []
        n = self.pocet_levelov(v1)
        for i in range(n+1):
            zoznam.append(self.vo_vzdialenosti(v1,i))
        return zoznam

    def v_strede(self, v1, v2):
        first = self.vsetky(v1)
        second = self.vsetky(v2)
        zoz = set()
        for n in range(len(first)):
            for prvok in first[n]:
                try:
                    if prvok in second[n]:
                        zoz.add(prvok)
                except:
                    pass
        return zoz
if __name__ == '__main__':

    g = Graf('subor5.txt')
    print(g.max('mure'))
