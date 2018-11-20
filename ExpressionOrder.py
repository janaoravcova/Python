# autor: Jana Oravcová
# uloha: 1. domace zadanie Vyraz
class Vyraz:
    class Stack:
        def __init__(self):
            self._prvky = []

        def push(self, data):
            self._prvky.append(data)

        def pop(self):
            if self.is_empty():
                return None
            return self._prvky.pop()

        def top(self):
            if self.is_empty():
                return None
            return self._prvky[-1]

        def is_empty(self):
            return self._prvky == []

    def __init__(self):
        self.tabulka = {}

    def __repr__(self):
        self.ret=''
        for kluc in self.tabulka:
            self.ret+=str(kluc)+ ' = ' + str(self.tabulka[kluc]) + '\n'
        return self.ret.strip()
    
    def je_cifra(self,znak):
        return '0' <= znak <= '9'
   
    def je_znak(self,znak):
        return 'a' <= znak <= 'z' or 'A' <= znak <= 'Z'

    def prirad(self, premenna, vyraz):
        pole=self.na_prvky(vyraz)
        if len(pole) == 1:#jednoprvkovy vyraz
            if pole[0] in '-*/+%':#len operator 
                return None
            elif self.je_cifra(pole[0]):#je cislo
                self.tabulka[premenna]=int(pole[0])
            elif pole[0] in self.tabulka:#premenna uz je v tabulke
                self.tabulka[premenna]=self.tabulka[pole[0]]
        else:
            if self.vyhodnot(vyraz) ==None:
                self.tabulka[premenna]=None
            else:
                self.tabulka[premenna]=int(self.vyhodnot(vyraz))
                
    
    def je_operator(self,vyraz):
        for prvok in vyraz:
            if prvok in '-*/+%':
                return True
        return False
     
    def na_prvky(self,vyraz):
        pom=[]
        ret=''
        i=0
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
            elif vyraz[i] in '-*/+%()':
                pom.append(vyraz[i])
                vyraz=vyraz[i+1:]
                i=0
        return pom
    def spaces(self, pole):
        vystup=''
        for prvok in self.na_prvky(pole):
            vystup+=str(prvok)+' '
        return vystup.strip()
    def vyhodnot(self, vyraz):
        if vyraz[0] in '*-/%+':
              s = self.Stack()
              vyraz = self.na_prvky(vyraz)
              for prvok in reversed(vyraz):
                    if prvok in self.tabulka:
                          prvok = self.tabulka.get(prvok)
                          try:
                              s.push(int(prvok))
                          except:
                              return None
                    elif prvok == '+':
                          try:
                              s.push(s.pop() + s.pop())
                          except:
                              return None
                    elif prvok == '-':
                          try:
                              s.push(s.pop() - s.pop())
                          except:
                              return None
                    elif prvok == '*':
                          try:
                              s.push(s.pop() * s.pop())
                          except:
                              return None
                    elif prvok == '/':
                          op1, op2 = s.pop(), s.pop()
                          if op1 is None or op2 is None:
                              return None
                          elif op2 == 0:
                              return None
                          else:
                              s.push(op1 // op2)
                    elif prvok == '%':
                          op1, op2 = s.pop(), s.pop()
                          if op1 is None or op2 is None:
                              return None
                          else:
                              s.push(op1 % op2)
                    elif self.je_cifra(prvok):
                          s.push(int(prvok))
              return s.pop()

        if vyraz[-1] in '+-*/%':
              s = self.Stack()
              vyraz = self.na_prvky(vyraz)
              for prvok in vyraz:
                    if prvok in self.tabulka:
                          prvok = self.tabulka.get(prvok)
                          try:
                              s.push(int(prvok))
                          except:
                              return None
                    elif prvok == '+':
                          try:
                              s.push(s.pop() + s.pop())
                          except:
                              return None
                    elif prvok == '-':
                          try:
                              s.push(-s.pop() + s.pop())
                          except:
                              return None
                    elif prvok == '*':
                          try:
                              s.push(s.pop() * s.pop())
                          except:
                              return None
                    elif prvok == '/':
                          op2 = s.pop()
                          op1 = s.pop()
                          if op1 is None or op2 is None:
                              return None
                          elif op2 == 0:
                              return None
                          else:
                              s.push(op1 // op2)
                    elif prvok == '%':
                          op2, op1 = s.pop(), s.pop()
                          if op1 is None or op2 is None:
                              return None
                          else:
                              s.push(op1 % op2)
                    elif self.je_cifra(prvok):
                          s.push(int(prvok))

              return s.pop()

        else:
              if self.je_operator(vyraz):
                    try:
                        return self.vyhodnot(self.in2post(vyraz))
                    except:
                        return None

    def in2post(self, vyraz):
        
        vystup=''
        vystup1=''
        s=self.Stack()
        prior={} # slovnik so zoradenou prioritnostou operatorov
        prior['/']=3
        prior['*']=3
        prior['%']=3
        prior['+']=2
        prior['-']=2
        prior['(']=1
        operatory=['/','*','%','+','-']
        prvok=self.na_prvky(vyraz)
        #print(prvok)
        for znak in prvok:
            if znak == '(':
                s.push(znak)
            elif znak==')':
                top=s.pop()
                while top!='(':
                    vystup+=top+' '
                    top=s.pop()
            elif znak in '-*/+%':
               
                while (not s.is_empty()) and (prior[s.top()] >= prior[znak]):
                    vystup+=s.pop()+' '
                s.push(znak)
            else:
                vystup+=znak+' '
        while not s.is_empty():
            op=s.pop()
            vystup+=op+' '
        
        return (vystup.strip())
if __name__ == '__main__':
    v = Vyraz()
    print(v.in2post('2+(44+a3*222+1)/pocet'))
    v.prirad('x','13')
    print(v.vyhodnot('x%5'))
    print(v.vyhodnot('x 5%'))
    print(v.vyhodnot('%x 5'))
    print(v.vyhodnot('x 5'))
    v.prirad('a','123')
    v.prirad('abc','a+1')
    v.prirad('a','abc 4 /')
    v.prirad('res22','/ 5 0')
    print(v)
    
   
   
