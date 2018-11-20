# autor: Janko Hrasko
# uloha: 11. domace zadanie labyrint
class Labyrint:
    class Vrchol:
        def __init__(self, riadok, stlpec):
            self.sus = []      # zoznam susedov, susedia su typu Vrchol
            self.poloha = riadok, stlpec
            self.odmena = False

        def __repr__(self):
            return '<{},{}>'.format(*self.poloha)

    def __init__(self, meno_suboru):
        self.g = []           # zoznam vrcholov grafu – obsahuje objekty typu Vrchol
        self.pocet=0
        with open(meno_suboru, 'r') as file:
            m,n = list(map(int,file.readline().strip().split()))
            for i in range(m):
                zoz=[]
                for j in range(n):
                    zoz.append(self.Vrchol(i,j))
                self.g.append(zoz)
                
            self.vytvor_susedov(m,n)
           
            line = file.readline().strip()
            while line!='':
                line = list(map(int,line.split()))
                if len(line)==2: #je to odmena:
                    self.g[line[0]][line[1]].odmena = True
                    self.pocet+=1
                else:
                    while len(line)>3:
                        r1,s1,r2,s2 = line.pop(0),line.pop(0),line.pop(0),line.pop(0)
                        self.daj_stenu(r1,s1,r2,s2)
                        self.daj_stenu(r2,s2,r1,s1)
                        line.insert(0,s2)
                        line.insert(0,r2)
                line = file.readline().strip()

##        for i in range(3):
##            for v in self.g[i]:
##                print(v,v.sus)
    def daj_stenu(self, r1,s1,r2,s2):
        i=0
        for sused in self.g[r1][s1].sus:
            if sused.poloha == (r2,s2):
              
                self.g[r1][s1].sus.remove(sused)
            i+=1
            
    def vytvor_susedov(self,m,n):
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    self.g[i][j].sus.append(self.daj_vrchol(0,j+1))
                    self.g[i][j].sus.append(self.daj_vrchol(i+1,0))
                elif i==0 and j==n-1:
                    self.g[i][j].sus.append(self.daj_vrchol(0,j-1))
                    self.g[i][j].sus.append(self.daj_vrchol(i+1,j))
                elif i==m-1 and j==0:
                    self.g[i][j].sus.append(self.daj_vrchol(i,j+1))
                    self.g[i][j].sus.append(self.daj_vrchol(i-1,0))
                elif i==m-1 and j==n-1:
                    self.g[i][j].sus.append(self.daj_vrchol(i,j-1))
                    self.g[i][j].sus.append(self.daj_vrchol(i-1,j))
                elif i==0 and j!=0 and j!=n-1:
                    self.g[i][j].sus.append(self.daj_vrchol(i,j+1))
                    self.g[i][j].sus.append(self.daj_vrchol(i,j-1))
                    self.g[i][j].sus.append(self.daj_vrchol(i+1,j))
                elif i==m-1 and j!=0 and j!=n-1:
                    self.g[i][j].sus.append(self.daj_vrchol(m-1,j+1))
                    self.g[i][j].sus.append(self.daj_vrchol(m-1,j-1))
                    self.g[i][j].sus.append(self.daj_vrchol(i-1,j))
                elif j==0 and i!=0 and i!=m-1:
                    self.g[i][j].sus.append(self.daj_vrchol(i-1,j))
                    self.g[i][j].sus.append(self.daj_vrchol(i+1,j))
                    self.g[i][j].sus.append(self.daj_vrchol(i,j+1))
                elif j==n-1 and i!=0 and i!=m-1:
                    self.g[i][j].sus.append(self.daj_vrchol(i-1,j))
                    self.g[i][j].sus.append(self.daj_vrchol(i+1,j))
                    self.g[i][j].sus.append(self.daj_vrchol(i,j-1))
                else:
                    self.g[i][j].sus.append(self.daj_vrchol(i-1,j))
                    self.g[i][j].sus.append(self.daj_vrchol(i+1,j))
                    self.g[i][j].sus.append(self.daj_vrchol(i,j-1))
                    self.g[i][j].sus.append(self.daj_vrchol(i,j+1))
                    
    
    def daj_vrchol(self, riadok, stlpec):
       
        return self.g[riadok][stlpec]
   

    def zmen_odmeny(self, *post):
        for prvok in post:
            r,s = prvok
            if self.g[r][s].odmena==True:
                self.g[r][s].odmena=False
                self.pocet-=1
            elif self.g[r][s].odmena==False:
                self.g[r][s].odmena=True
                self.pocet+=1

    def start(self, riadok, stlpec):
        self.cesty=[]
        if self.daj_vrchol(riadok,stlpec).odmena:
            poc=1
        else:
            poc=0
        self.backtracking(riadok, stlpec, [(riadok,stlpec)], [(riadok,stlpec)],poc)

        if self.cesty!=[]:
            return self.cesty[0]
        else:
            return []

    def porovnaj(self,cesta):
        def _pom(pole):
            vysl=[]
            for prvok in pole:
                vysl.append(prvok)
            return vysl

        self.cesty.append(_pom(cesta))


    def backtracking(self,r,s,visited,cesta, poc):

        for v in self.daj_vrchol(r,s).sus:
        
            if v.poloha not in visited:
                visited.append(v.poloha)
                cesta.append(v.poloha)
                r1,s1 = v.poloha

                if v.odmena:
                    poc+=1
                   
                
                self.backtracking(r1,s1, visited, cesta,poc)
                
                if v.odmena:
                    poc-=1

                visited.pop()
                cesta.pop()

        if poc == self.pocet:
    
            self.porovnaj(cesta)

if __name__ == '__main__':
    lab = Labyrint('subor3.txt')
##    v = lab.daj_vrchol(1, 0)
##    print('vrchol:', v, 'susedia:', v.sus, 'odmena:', v.odmena)
##    v = lab.daj_vrchol(2, 2)
##    print('vrchol:', v, 'susedia:', v.sus, 'odmena:', v.odmena)
##    print(lab.start(0, 0))
##    print(lab.start(0, 2))
##    lab.zmen_odmeny((2, 2))
##
##    print(lab.start(0, 0))
