class Graf:
    def __init__(self, meno_suboru):
        self.graf = {}
        with open(meno_suboru, 'r') as file:
            line = file.readline().strip()
            while line!='':

                prvky = line.split(':')
                if len(prvky)==3:
                    v1,hodnota,v2 = prvky
                    self.pridaj_hranu(v1,v2,hodnota)
                    self.pridaj_hranu(v2,v1,hodnota)

                else:
                    v1,v2 = prvky
                    hodnota=''
                    self.pridaj_hranu(v1,v2,'')
                    self.pridaj_hranu(v2,v1,'')
                line = file.readline().strip()
        print(self.graf)    

    def pridaj_hranu(self, v1,v2,hodnota):
        if v1 not in self.graf:
            self.graf[v1]=dict()
        if v2 not in self.graf[v1]:
            self.graf[v1][v2] = set()
        self.graf[v1][v2]=hodnota
    def hrana(self, v1, v2):
        try:
            return self.graf[v1][v2]
        except:
            return None

    def vrcholy(self):
        s=set()
        for key in self.graf:
            s.add(key)
        return s

    def ries(self, v1):
        self.cesty=[]
        self.naj=[]
        self.backtracking(self, v1, [v1], [v1])

        if self.cesty!=[]:
            dlzky=[]
            for cesta in self.cesty:
                dlzky.append(len(cesta))

            max=0
            for d in dlzky:
                if d>max:
                    max=d

            for cesta in self.cesty:
                if len(cesta)==d:
                    self.naj.append(cesta)

            return self.naj

        else:
            return []
    def kontrola(self, hodnota):
        for i in len(hodnota):
            if i%3==0 and hodnota[i]=='a' or hodnota[i]=='':
                poc+=1
            if i%3==1 and hodnota[i]=='b' or hdonota[i]=='':
                poc+=1
            if i%3==2 and hodnota[i]=='c' or hodnota[i]=='':
                poc+=2

        if poc==len(hodnota):
            return True
        return False
    def porovnaj(self, cesta):
        def _pom(pole):
            vysl=[]
            for prvok in pole:
                vysl.append(prvok)
            return vysl

        self.cesty.append(_pom(cesta))
        
    def backtracking(self, v1, visited, cesta, hodnota):
        for v2 in self.graf[v1]:
            if v2 not in visited:
                visited.append(v2)
                cesta.append(v2)
                hodnota.append(self.hrana(v1,v2))
                if self.kontrola(hodnota):
                    self.backtracking(v2, visited, cesta,hodnota)

                visited.pop()
                cesta.pop()
                hodnota.pop()

        if cesta!=[]:
            self.porovnaj(cesta)
if __name__ == '__main__':
    g = Graf('subor1.txt')
    print('vrcholy =', g.vrcholy())
    for v1, v2 in ('mo', 'ub'), ('er', 'ub'), ('er', 'mo'):
        print(f'hrana({v1!r},{v2!r}) = {g.hrana(v1,v2)!r}')
    riesenie = g.ries('qa')
    print('pocet rieseni =', len(riesenie))
    print(*riesenie, sep='\n')
