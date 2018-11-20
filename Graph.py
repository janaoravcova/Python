# autor: Jana Oravcova
# uloha: 8. domace zadanie graf
class Graf:
    def __init__(self, meno_suboru):
        self.graf = set()
        with open(meno_suboru, 'r') as file:
            instruction = file.readline().strip()
            #print(instruction.strip())
            if instruction == '#1':
                line = file.readline().strip()
                #print(line)
                while line!='':
                    #print(line)
                    node = line.split()[0]
                    neig = line.split()[1:]
                    while neig!=[]:
                        element = neig.pop()
                        tuples = node,element
                        self.pridaj_hranu(node,element)
                    line = file.readline().strip()
            elif instruction == "#2":
                line = file.readline().strip()
                while line!='':
                    v1,v2 = line.split()
                    self.pridaj_hranu(v1,v2)
                    line = file.readline().strip()
            elif instruction == "#3":
                nodes = file.readline().strip().split()
                nodes_1 = [x for x in nodes]
                line = file.readline().strip()
                l = len(nodes)#pocet vrcholov
                while line!='':
                    node = nodes.pop(0)
                    line = line.split()
                    for i in range(l):#prechadzanie riadkom
                        if line[i] == '1':
                            v1,v2 = node, nodes_1[i]
                            self.pridaj_hranu(v1,v2)
             
                    line = file.readline().strip()
    def pridaj_hranu(self, v1, v2):
        self.graf.add((v1,v2))

    def je_hrana(self, v1, v2):
        return (v1,v2) in self.graf

    def daj_vrcholy(self):
        mena = set()             # vrati mnozinu mien vrcholov
        for tuples in self.graf:
            mena.add(list(tuples)[0])
            if list(tuples)[1]!=None:
                mena.add(list(tuples)[1])
        return mena
    def daj_hrany(self):
        return self.graf              # vrati mnozinu dvojic mien vrcholov
    def neighbours(self, el):
        n = []
        for tuples in self.graf:
            if list(tuples)[0]==el:
                n.append(list(tuples)[1])
        return n
    def uloz(self, meno_suboru, typ=1):
        if typ == 1:
            self.first_save(meno_suboru)
        elif typ == 2:
            self.second_save(meno_suboru)
        elif typ == 3:
            self.third_save(meno_suboru)
    def first_save(self, meno_suboru):
        nodes = list(self.daj_vrcholy())
        with open(meno_suboru, 'w') as file:
            print("#1", file = file)
            for element in nodes:
                print(element, end=' ', file = file)
                print(' '.join([v[1] for v in self.graf if v[0] == element]), file = file)
             
    def second_save(self, meno_suboru):
         with open(meno_suboru, 'w') as file:
             print("#2", file = file)
             for tuples in self.graf:
                 print(' '.join(list(tuples)), file = file)
                # print(file = file)
    def third_save(self, meno_suboru):
         with open(meno_suboru,'w') as file:
             #print(self.daj_vrcholy())
             print("#3", file = file)
             array = self.daj_vrcholy()
             print(' '.join(self.daj_vrcholy()),file = file)
             for element_1 in array:
                 for element_2 in array:
                     if (element_1,element_2) in self.graf:
                         print('1', end=' ', file = file)
                     else:
                         print('0', end=' ', file = file)
                 print(file = file)

##g = Graf('subor6.txt')
##print(g.graf)
##print(g.daj_vrcholy())
##g.uloz('subor1_2.txt',1)
