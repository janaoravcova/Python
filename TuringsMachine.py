# autor: Jana Oravcová
# uloha: 2. domace zadanie Turing

class Turing:
    class Paska:
        def __init__(self, obsah=''):
            self.paska = list(obsah or '_')
            self.poz = 0

        def symbol(self):
            return self.paska[self.poz]

        def zmen_symbol(self, znak):
            self.paska[self.poz] = znak

        def __repr__(self):
            return ''.join(self.paska) + '\n' + ' '*self.poz + '^'

        def vpravo(self):
            self.poz += 1
            if self.poz == len(self.paska):
                self.paska.append('_')

        def vlavo(self):
            if self.poz > 0:
                self.poz -= 1
            else:
                pom = self.paska
                self.paska = None
                self.paska.append('_')
                self.paska.append(pom)
                pom=None
                #self.paska.insert(0, '_')

        def text(self):
            return ''.join(self.paska).strip('_')
    def __init__(self,program, obsah=''):
        self.prog = {}
        self.pocet=0
        self.paska=self.Paska(obsah)
        self.poz=0
        self.stav=None
        self.koniec={'end', 'stop'}
        prvy=program.split('\n')[1]
        self.stavy=prvy.split()
        self.znaky=[]
        #print(self.stavy)
        for riadok in program.strip().split('\n')[1:]:
            #print(program.strip().split('\n')[2:])
            riadok = riadok.split()
            if riadok!=[]:
                #print(riadok)
                znak=riadok.pop(0)
                self.znaky.append(znak)
                instrukcie=riadok[0:]
                i=0
                #print(stavy)
                for stav in self.stavy:
                   # print(instrukcie[i])
                   if self.stav is None:
                       self.stav=stav
                       #print(self.stav)
                   self.prog[stav,znak[0:1]]=self.na_prvky(instrukcie[i:i+1])
                   i+=1


                   
    def je_cifra(self,znak):
        return '0' <= znak <= '9'
   
    def je_znak(self,znak):
        return 'a' <= znak <= 'z' or 'A' <= znak <= 'Z'

    def na_prvky(self,vyraz):
        pom=[]
        ret=''
        i=0
        vyraz=vyraz[0]
        vyraz+=' '
        while vyraz!='':
            if self.je_znak(vyraz[i]):
                while self.je_znak(vyraz[i]) or self.je_cifra(vyraz[i]):
                    i+=1
                pom.append(vyraz[:i])
                vyraz=vyraz[i:]
                i=0
            elif self.je_cifra(vyraz[i]):
                while self.je_cifra(vyraz[i]):
                    i+=1
                pom.append(vyraz[:i])
                vyraz = vyraz[i:]
                i=0
            elif vyraz[i] is ' ':
                vyraz=vyraz[i+1:]
                i=0
            elif vyraz[i] in '<>=.':
                pom.append(vyraz[i])
                vyraz=vyraz[i+1:]
                i=0
        return pom
    def je_stav(self,pole):
        for stav in self.stavy:
            if pole.count(stav)!=0:
                return True
        return False
    def je_znak0(self,pole):
        for znak in self.znaky:
            if pole.count(znak)!=0:
                return True
        return False
   
    def restart(self, stav=None, obsah=None, n=None):
        
        # od noveho stavu (ak nie je None), s novou paskou (ak nie je None) a zavola rob()
        
        if stav is not None:
            self.stav=stav
            
            
        if obsah is not None:
            self.paska=self.Paska(obsah)
        if n is not None:    
            return self.rob(n)
        else:
            return self.rob()
##        if b==False:
##            return False, self.pocet
##        return True, self.pocet
        

        #return False, self.pocet
    def krok(self):
        stav1, znak1 = self.stav, self.paska.symbol()
        
        #print(len(self.prog[stav1, znak1]))
        try:
            if len(self.prog[stav1, znak1])==3:#vsetky 3 parametre
                        
                    znak2, smer, stav2 = self.prog[stav1, znak1]
            elif len(self.prog[stav1, znak1])==2:#nieco chyba
                if not self.je_stav(self.prog[stav1,znak1]):#chyba stav=je tam znak a smer
                        
                    znak2,smer=self.prog[stav1, znak1]
                    stav2=stav1
                else:#chyba znak
                        
                    smer, stav2=self.prog[stav1, znak1]
                    znak2=znak1
            elif len(self.prog[stav1, znak1])==1:#je tam len smer
                #print('tu')
                smer=self.prog[stav1, znak1][0]
                znak2, stav2 = znak1, stav1
                #print (smer,znak2,stav2)
            elif self.prog[stav1,znak1]=='.':
                return False, self.pocet
        except KeyError:
            return False, self.pocet
        self.paska.zmen_symbol(znak2)
        self.stav = stav2
        if smer == '>':
            self.paska.vpravo()
        elif smer == '<':
            self.paska.vlavo()
        return True,self.pocet
    def rob(self, n=None):
        self.pocet=0
##        if isinstance(n,int) and n+1==self.pocet:
##            print(self)
##            return False, self.pocet

        pocet = 0
        while self.stav not in self.koniec  and n is None or (n is not None and self.stav not in self.koniec  and pocet <= n):
            if not self.krok():
                return False, pocet
##            if  isinstance(n,int) and  n==self.pocet:
##                print(self)
##                return False, self.pocet 
            pocet+=1
    
        return True, pocet
    def text(self):
        return self.paska.text()

if __name__ == '__main__':
    prog = '''
        s1    s2
    0    >    1=end
    1    >    0<
    _   <s2   1=end
    '''
    t = Turing(prog, '1011')
    print(t.prog)
    print(t.rob())
    print('vysledok =', t.text())
    print(t.restart('s1', '10102010'))
