# autor: Jana Oravcová
# uloha: 3. domace zadanie SpajanyZoznam2
class SpajanyZoznam2:
    class Vrchol:
        def __init__(self, data, next=None):
            self.data, self.next = data, next

    def __init__(self, postupnost=None):
        self.zac = self.kon = None
        if postupnost is not None:
            for prvok in postupnost:
                self.append(prvok)
    def append(self, hodnota):
        #print(hodnota)
        if self.zac is None:
            if type(hodnota) == list  or type(hodnota) == tuple:
                self.kon = self.zac = self.Vrchol(SpajanyZoznam2(hodnota))
            else:
                self.kon = self.zac = self.Vrchol(hodnota)
        else:
            if (type(hodnota) == list  or type(hodnota) == tuple):
                self.kon.next = self.Vrchol(SpajanyZoznam2(hodnota))
                #print(hodnota)
                self.kon = self.kon.next
            else:
                #print(hodnota)
                self.kon.next = self.Vrchol(hodnota)
                self.kon = self.kon.next
    def count(self, hodnota):
        pom=self.zac
        pocet=0
        while pom is not None:
            if isinstance(pom.data,SpajanyZoznam2):
                pocet+=pom.data.count(hodnota)
            elif isinstance(pom.data,list) or isinstance(pom.data,tuple):
                for prvok in pom.data:
                    if prvok==hodnota:
                        pocet+=1
            else:
                if pom.data==hodnota:
                    pocet+=1
            pom=pom.next
        return pocet

    def tolist(self):
        pole=[]
        pom=self.zac       
        while pom is not None:
            if isinstance(pom.data, SpajanyZoznam2):
                pole.append(pom.data.tolist())
            else:
               
                pole.append(pom.data)
            pom=pom.next
        return pole

    def totuple(self):
        ntica=()
        pom=self.zac        
        while pom is not None:
            if isinstance(pom.data,SpajanyZoznam2):
                ntica+=(pom.data.totuple(),)
            else:
                ntica+=(pom.data,)
            pom=pom.next
        return ntica
if __name__ == '__main__':
    z = SpajanyZoznam2([[], [], [[[], []], [], [[[]]]], [], []])
    print(z.totuple())
    
