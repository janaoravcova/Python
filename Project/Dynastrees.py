import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import messagebox
from tkinter import Text

import os.path
import time
import random
from passlib.hash import pbkdf2_sha256



class Login:
    def __init__(self, canvas=None):
        self.canvas = canvas
        if self.canvas == None:
            self.canvas = tkinter.Canvas(width=500, heigh=500, background='#475152')
        else:
            self.canvas.configure(width=500, height=500)
        self.canvas.pack()
        self.create_login()
        self.canvas.bind('<Motion>', self.hover)
        self.canvas.bind('<Button-1>', self.click)
        

    def create_login(self):
        self.canvas.create_rectangle(0,0, 502, 115, fill='white', outline='')
        self.im = tkinter.PhotoImage(file='rsz_2logo2.png')
        #smaller_image = self.im.subsample(2, 2)
        self.canvas.create_image(250,51, image=self.im)
        #self.canvas.create_line(0,115,500,115, fill='white')
        #self.canvas.create_text(250,90, text='Vítajte!', fill='wheat1', font='courier 35 italic')
        self.canvas.create_text(250,130, text='Prosím, registrujte sa.', fill='white', font='courier 10 italic')
        self.canvas.create_text(250,150, text='Ak už ste v minulosti vykonali registráciu,', fill='white', font='courier 10 italic')
        self.canvas.create_text(250,170, text='zadajte vaše meno a heslo.', fill='white', font='courier 10 italic')
        self.canvas.create_text(125,250, text='Chcem sa registrovať!', fill='white', font='courier 10 italic')
        self.canvas.create_text(375,250, text='Chcem sa prihlásiť!', fill='white', font='courier 10 italic')
        #=====#registracia
        self.canvas.create_text(28,280,text="Meno",fill='white', font='courier 10 italic' )
        self.nick_nonregistered = Entry(self.canvas)
        self.nick_nonregistered.place(x=100, y=270)
        self.canvas.create_text(30,310,text="Heslo",fill='white', font='courier 10 italic' )
        self.pass_nonregistered = Entry(self.canvas, show="*")
        self.pass_nonregistered.place(x=100,y=300)
        self.canvas.create_text(50,340,text="Heslo znova",fill='white', font='courier 10 italic' )
        self.repass_nonregistered = Entry(self.canvas, show="*")
        self.repass_nonregistered.place(x=100,y=330)
        #self.canvas.create_rectangle(130,370,230,390, fill='wheat1', outline='')
        #self.canvas.create_text(140,380, text='Registrovať', fill='wheat1', font='courier 12 italic bold')
  
        #=====#prihlasenie
        self.canvas.create_text(285,280,text="Meno",fill='white', font='courier 10 italic')
        self.nick_registered = Entry(self.canvas)
        self.nick_registered.place(x=330, y=270)
        self.canvas.create_text(285,310,text="Heslo",fill='white', font='courier 10 italic' )
        self.pass_registered = Entry(self.canvas, show="*")
        self.pass_registered.place(x=330,y=300)
        #self.canvas.create_rectangle(330,370,430,390, fill='wheat1', outline='')
        #self.canvas.create_text(380,380, text='Prihlásiť', fill='wheat1', font='courier 12 italic bold')
        
        
##        self.nickname = Entry(self.canvas)
##        self.nickname.place(x=180,y=250)
        self.canvas.create_line(250,220,250,500, fill='white')
        self.canvas.create_rectangle(110,390,180,420, fill='white', outline='')
        self.canvas.create_text(145,405, text='Štart', fill='#475152', font='courier 15 italic')
        self.canvas.create_rectangle(330,390,400,420, fill='white', outline='')
        self.canvas.create_text(365,405, text='Štart', fill='#475152', font='courier 15 italic')

    def hover(self,event):
        x,y = event.x, event.y
        if (x>=110 and x<=180 and y>=390 and y<=420) or (x>=330 and x<=400 and y>=390 and y<=420):
            self.canvas.configure(cursor='hand1')
        else:
            self.canvas.configure(cursor='arrow')


    def administration(self,status):
        nick_nr = self.nick_nonregistered.get()
        pass_nr = self.pass_nonregistered.get()
        repass_nr = self.repass_nonregistered.get()
        nick_r = self.nick_registered.get()
        pass_r = self.pass_registered.get()
        if( ( nick_nr!=''or pass_nr!='' or repass_nr!='') and (nick_r!='' or pass_r!='')):
            messagebox.showwarning("Pozor","Vyplň len registráciu alebo len prihlásenie!")
            return False
        else:
            if status=='nonregistered':
                if nick_nr!='' and nick_nr!=' ':
                    if not os.path.isfile(nick_nr+'.txt'):
                        if pass_nr!='' and pass_nr!=' ':
                            if repass_nr!='' and repass_nr!=' ':
                                if pass_nr==repass_nr:
                                    hash = pbkdf2_sha256.hash(pass_nr)
                                else:
                                    messagebox.showwarning("Pozor","Heslá sa nezhodujú!")
                                    return False
                            else:
                                messagebox.showwarning("Pozor","Nezopakovali ste heslo!")
                                return False
                        else:
                            messagebox.showwarning("Pozor","Nezadali ste heslo!")
                            return False
                    else:
                        messagebox.showwarning("Pozor","Toto meno už je obsadené, skúste iné!")
                        return False
                else:
                    messagebox.showwarning("Pozor","Nezadali ste meno !")
                    return False
            elif status=='registered':
                if nick_r!='' and nick_r!=' ':
                    if pass_r!='' and pass_r!=' ':
                        #hash = pbkdf2_sha256.hash(pass_r)
                        try:
                            with open(nick_r+'.txt','r') as f:
                                name=f.readline()
                                hash=f.readline().strip()
                            if pbkdf2_sha256.verify(pass_r, hash):
                                return True
                            else:
                                messagebox.showwarning("Pozor","Nesprávne heslo!")
                                return False
                        except:
                            messagebox.showwarning("Pozor","Nesprávne meno!")
                            return False
                    else:
                        messagebox.showwarning("Pozor","Nezadali ste heslo alebo použili nepovolené znaky!")
                        return False
                else:
                    messagebox.showwarning("Pozor","Nezadali ste meno lebo použili nepovolené znaky!")
                    return False
        return hash
    
    def click(self,event):
        x,y = event.x, event.y
        if x>=110 and x<=180 and y>=390 and y<=420:
            if self.administration('nonregistered')!=False:
                meno=self.nick_nonregistered.get()
                self.create_file(meno,self.administration('nonregistered'))
                self.canvas.delete('all')
                self.nick_nonregistered.destroy()
                self.pass_nonregistered.destroy()
                self.repass_nonregistered.destroy()
                self.nick_registered.destroy()
                self.pass_registered.destroy()
                self.canvas.update()
                self.canvas.unbind('<B1-Motion>')
                self.canvas.unbind('<Motion>')
                StartMenu(self.canvas,meno)
        elif (x>=330 and x<=400 and y>=390 and y<=420):
           if self.administration('registered')!=False:

                meno=self.nick_registered.get()
                self.canvas.delete('all')
                self.nick_nonregistered.destroy()
                self.pass_nonregistered.destroy()
                self.repass_nonregistered.destroy()
                self.nick_registered.destroy()
                self.pass_registered.destroy()
                self.canvas.update()
                self.canvas.unbind('<B1-Motion>')
                self.canvas.unbind('<Motion>')
                StartMenu(self.canvas, meno)
             
    def create_file(self, file, password):
        with open(file+'.txt', 'w') as f:
            f.write(file)
            f.write('\n')
            f.write(password)
            f.write('\n')
            
class StartMenu:
    def __init__(self, canvas, name):
        self.nick = name
        self.canvas = canvas
        self.canvas.configure(width=500, height=500, background='#475152')
        self.canvas.pack()
        self.menu()
        self.canvas.configure(cursor='arrow')
        self.canvas.bind('<Motion>', self.focused)
        self.canvas.bind('<Button-1>', self.gamestart)
        self.canvas.update()

    def menu(self):
        self.im = tkinter.PhotoImage(file='crown.png')
        #smaller_image = self.im.subsample(2, 2)
        self.canvas.create_image(250,50, image=self.im)
        self.canvas.create_text(250, 115, text = 'Zvoľte dynastiu, '+self.nick+'!', font='courier 24 italic bold', fill='white')
        self.habsburg_frame = self.canvas.create_rectangle(100,150,400,190, outline='white')
        self.habsburg = self.canvas.create_text(250, 170, text='Habsburgovci', font='courier 25 italic', fill='white')
##        self.arpad_frame = self.canvas.create_rectangle(100,210,400,250, outline='wheat1')
##        self.arpad = self.canvas.create_text(250, 230, text='Arpádovci', font='courier 25 italic', fill='wheat1')
##        self.premysl_frame = self.canvas.create_rectangle(100,270,400,310, outline='wheat1')
##        self.premysl = self.canvas.create_text(250, 290, text='Premyslovci', font='courier 25 italic', fill='wheat1')
##        self.tudor_frame = self.canvas.create_rectangle(100,330,400,370, outline='wheat1')
##        self.tudor = self.canvas.create_text(250, 350, text='Tudorovci', font='courier 25 italic', fill='wheat1')
        self.navigation_frame = self.canvas.create_rectangle(240,460 ,260, 480 , outline='white')
        self.navigation = self.canvas.create_text(250, 470, text='?', font='courier 25 bold', fill='white')
        

    def focused(self,event):
        x,y = event.x,event.y
        if x>=100 and x<=400 and y>=150 and y<=190:
            self.canvas.itemconfig(self.habsburg_frame, fill='white')
            self.canvas.itemconfig(self.habsburg, fill='#475152')
        else:
            self.canvas.itemconfig(self.habsburg_frame, fill='')
            self.canvas.itemconfig(self.habsburg, fill='white')
##        if x>=100 and x<=400 and y>=210 and y<=250:
##            self.canvas.itemconfig(self.romanov_frame, fill='wheat1')
##            self.canvas.itemconfig(self.romanov, fill='firebrick')
##        else:
##            self.canvas.itemconfig(self.romanov_frame, fill='')
##            self.canvas.itemconfig(self.romanov, fill='wheat1')
##        if x>=100 and x<=400 and y>=270 and y<=310:
##            self.canvas.itemconfig(self.premysl_frame, fill='wheat1')
##            self.canvas.itemconfig(self.premysl, fill='firebrick')
##        else:
##            self.canvas.itemconfig(self.premysl_frame, fill='')
##            self.canvas.itemconfig(self.premysl, fill='wheat1')
##        if x>=100 and x<=400 and y>=330 and y<=370:
##            self.canvas.itemconfig(self.tudor_frame, fill='wheat1')
##            self.canvas.itemconfig(self.tudor, fill='firebrick')
##        else:
##            self.canvas.itemconfig(self.tudor_frame, fill='')
##            self.canvas.itemconfig(self.tudor, fill='wheat1')


    def gamestart(self, event):
        x,y = event.x, event.y
        if x>=100 and x<=400 and y>=150 and y<=190:
            self.canvas.delete('all')
            self.canvas.update()
            self.canvas.unbind('<B1-Motion>')
            TestTree('habs_test.txt', self.canvas, self.nick, 'habs')

        if x>=240 and x<=260 and y>=460 and y<=480:
            self.canvas.delete('all')
            self.canvas.update()
            self.canvas.unbind('<B1-Motion>')
            Navigation(self.canvas, self.nick)
    

### class of page with descriptions of the game rules
class Navigation:
    def __init__(self,canvas, name):
        self.nick = name
        self.canvas = canvas
        self.text=[]
        self.canvas.configure(cursor='arrow')
        self.background = tkinter.PhotoImage(file='rsz_scroll.png')
        self.canvas.create_image(250, 250,anchor=tkinter.CENTER,  image=self.background)
        self.canvas.create_line(15,490,45,490, fill='white')
        self.canvas.create_text(30,480, text='Menu', font='courier 13 italic', fill='white')
        self.canvas.bind('<Button-1>', self.back_to_menu)
        self.write_navigation()

    def write_navigation(self):
        with open('navigation.txt', 'r') as file:
            _line = file.readline().strip()
            while _line!='':
                self.text.append(_line)
                _line = file.readline().strip()

        k=1
        for line in self.text:
            self.canvas.create_text(250, 30*k+40, text=line, font='arial 9 italic bold', fill='sienna4')
            k+=1
            
    def back_to_menu(self, event):
        x,y = event.x, event.y
        if x>=15 and x<=45 and y>=470 and y<=490:
            self.canvas.delete('all')
            self.canvas.update()
            self.canvas.unbind('<B1-Motion>')
            StartMenu(self.canvas, self.nick)
            
class TestTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.child=[]
    class Queue:
        def __init__(self):
            self.elements = []
        def is_empty(self):
            return self.elements==[]
        def enqueue(self, data):
            self.elements.append(data)
        def dequeue(self):
            return self.elements.pop(0)
    def __init__(self, file,canvas, name, dynasty):
        self.nick = name
        self.root = None
        self.tuples = {}
        self.sons = set()
        self.fathers = set()
        self.count = 0
        self.ppl = {}
        self.hints = {}
        self.hint_mess = {}
        self.hint_text = {}
        self.side = {}
        self.cords_side = {}
        self.name = {}
        self.line_height = {}
        self.sek=0
        self.placed =[]
        self.correctly_placed=[]
        self.names_correct={}
        self.relatives=[]
        self.dynasty=dynasty
        self.missing_cols(dynasty+'_missing.txt')
        self.random_pos = [x for x in range(len(self.missing))]
        random.shuffle(self.random_pos)
        self.canvas = canvas
        self.canvas.configure(width=1600,height=800)
        self.create_tree(file)
        self.canvas.configure(cursor='arrow')
        self.selected = None
        self.canvas.bind('<Button-1>', self.click)
        self.canvas.bind('<Motion>',self.hover)
        self.canvas.bind('<B1-Motion>', self.move)
        self.canvas.bind('<ButtonRelease-1>', self.stop_move)
        #self.canvas.bind('<Button-1>', self.submit)
        self.create_hints('habs_hints1.txt')
        self.timer()
        

    def timer(self, fin=0):
        self.sek +=1
        self.min = self.sek //60
        self.sekundy = self.sek % 60
        if fin==1:
            return self.sek
        else:
            self.canvas.after(1000,self.timer)
            
    def create_hints(self, file):
        with open (file, 'r') as f:
            hint = f.read().split('=')
            for h in hint:
                lines = h.strip().split('\n')
                self.line_height[lines[0]]=len(lines)
                self.hints[lines[0]] = lines[1:]
                
                
    def create_tree(self, meno_suboru):
        with open(meno_suboru, 'r') as file:
            family = file.read().split('\n')
            for members in family:
                if members!='':
                    father,son = members.split('-')
                    self.relatives.append([father,son])
                    self.fathers.add(father)
                    if father in self.tuples:
                        second_son = self.tuples[father]
                        self.tuples[father] = (son, second_son)
                    else:
                        self.tuples[father] = son
                    self.sons.add(son)
        self.root = self.Node(list(self.fathers  - self.sons)[0])
        queue = self.Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            father = queue.dequeue()
            try:
                children = self.tuples[father.data]
                if type(children)==tuple:
                    for kiddo in children:
                        new = self.Node(kiddo)
                        father.child.append(new)
                        queue.enqueue(new)
                    
                else:
                    new = self.Node(children)
                    father.child.append(new)
                    queue.enqueue(new)
            except KeyError:
                pass
        if meno_suboru=='habs_test.txt':
            self.missing_cols('habs_missing.txt')
        self.draw_tree()



    def missing_cols(self, file):
        self.missing=[]
        with open(file, 'r') as f:
            line = f.readline()
            while line!='':
                self.missing.append(line.strip())
                line = f.readline()
        return self.missing
                
        
    def by_levels(self):
        q = self.Queue()
        q.enqueue((self.root,0))
        nodes=[]
        self.all_nodes=[[self.root.data]]
        lower=0
        while not q.is_empty():
            node, level = q.dequeue()
            #print(node.data)
            if lower!=level:
                self.all_nodes.append(nodes)
                nodes=[]
            lower=level
            if len(node.child)>0:
                for kid in node.child:
                   # print(kid.data)
                    q.enqueue((kid,level+1))
                    nodes.append(kid.data)

        return self.all_nodes


    def get_key(self,x,y):
        for key, value in self.ppl.items():
            x0,y0,x1,y1 = value
            if x>=x0 and x<=x1 and y>=y0 and y<=y1:
                return key
        return False
    
    def hover(self,event):
        x,y = event.x, event.y
        key = self.get_key(x,y)
        if key!=False:
            self.canvas.coords(self.frame, x,y,x+300,y+2*(self.line_height[key]//2)*15)
            self.canvas.itemconfig(self.frame, outline='#475152', fill='white')
            self.canvas.itemconfig(self.hinto, text='\n'.join(self.hints[key]), font='arial 8 italic bold', fill='#475152')
            self.canvas.tag_raise(self.frame)
            self.canvas.tag_raise(self.hinto)
            self.canvas.coords(self.hinto,x+150,y+(self.line_height[key]//2)*15)
        else:
            self.canvas.coords(self.frame, 300,300,300,300)
            self.canvas.itemconfig(self.frame, outline='', fill='firebrick')
            self.canvas.itemconfig(self.hinto, text='', font='arial 8 italic bold')
            self.canvas.coords(self.hinto,350, 150)
                
        if (x>=20 and x<=50 and y>=677 and y<=690) or (x>=1270 and x<=1325 and y>=677 and y<=690):
            self.canvas.configure(cursor='hand1')
        else:
            self.canvas.configure(cursor='arrow')   
        
    def draw_tree(self):
        _all = self.by_levels()
        k,m=0,0
        self.coat = tkinter.PhotoImage(file="rsz_coat_of_arms_habsburg.png")
        self.canvas.create_image(1200,150, image=self.coat)
        self.canvas.create_line(20,690,50,690, fill='white')
        self.frame = self.canvas.create_rectangle(200,200,200,200, outline='', fill='firebrick' )
        self.canvas.create_text(35,680, text='Menu', font='courier 13 italic', fill='white')
        self.canvas.create_line(1270,690,1325,690, fill='white')
        self.canvas.create_text(1300,680, text='Kontrola', font='courier 13 italic', fill='white')
        self.hinto=self.canvas.create_text(350, 150, text='', font='arial 15 italic', fill='white')
        missing = self.missing
        for level in _all:
            n=len(level)
            start_position = (1600 - (n*100 + (n-1)*10))//2
            new_position = start_position
            for person in level:
                self.canvas.create_rectangle(new_position, 35*k+5, new_position+100, 35*k+30, fill='white')
                if person not in missing:
                    self.canvas.create_text(new_position+50, 35*k+15, text=str(person), fill='#475152', font='arial 8 italic')
                    self.names_correct[person] = new_position+50, 35*k+15
                else:
                    x0,y0,x1,y1 = new_position, 35*k+5, new_position+100, 35*k+30
                    m=self.random_pos.pop()
                    self.ppl[person] =  list((x0,y0,x1,y1)) #stvorica vyclenujuca polohu policka ako hodnota asoc pola s klucom=panovnik
                    self.side[person] = self.canvas.create_rectangle(3,35*m+5,103,35*m+30, fill='white')#asoc pole policok na doplnenie
                    self.names_correct[person] = ((x1-x0)//2)+x0, ((y1-y0)//2)+y0
                    self.cords_side[person] = 3, 35*m+5, 103, 35*m+30
                    self.name[person] = self.canvas.create_text(53,35*m+15, text=str(person),fill='#475152',font='arial 8 italic')
                new_position+=110
            k+=1

        for pair in self.relatives:
            initial = self.names_correct[pair[0]]
            final = self.names_correct[pair[1]]
            line = self.canvas.create_line(initial,final, fill='white', width=2)
            self.canvas.tag_lower(line)
            


    def find_matching_coords(self, x, y):
        for key, value in self.ppl.items():
            x0,y0,x1,y1 = value
            if x>=x0 and x<=x1 and y>=y0 and y<=y1:
                return value
        return None
    
    def find_matching_name(self, x, y):
        for key, value in self.ppl.items():
            x0,y0,x1,y1 = value
            if x>=x0 and x<=x1 and y>=y0 and y<=y1:
                return key
        return None
    
    def find_overlapping_object(self, x, y):
        for key, value in self.cords_side.items():
            x0,y0,x1,y1 = value
            if x>=x0 and x<=x1 and y>=y0 and y<=y1:
                return self.side[key]
        return None

    def get_overlapping_name(self, x,y):
        for key, value in self.cords_side.items():
            x0,y0,x1,y1 = value
            if x>=x0 and x<=x1 and y>=y0 and y<=y1:
                return key
        return None
                
    def click(self, event):
        x,y = event.x, event.y
        self.selected = self.find_overlapping_object(x,y)
        self.selected_name = self.get_overlapping_name(x,y)
        #print(self.selected_name)
        if(x>=20 and x<=50 and y>=677 and y<=690):
                self.canvas.delete('all')
                self.canvas.update()
                self.canvas.unbind('<B1-Motion>')
                #self.canvas.configure(width=500, height=500)
                StartMenu(self.canvas, self.nick)
        if (x>=1270 and x<=1325 and y>=677 and y<=690):
            if len(self.placed)==len(self.missing):
                if len(self.correctly_placed)==len(self.missing):
                    messagebox.showinfo("Gratulujem","Správne ste vyplnili celý rodokmeň.")
                    self.save_result()
                    self.show_average()
                else:
                    messagebox.showinfo("Ľutujem","Bohužiaľ, skúste si látku viac naštudovať.")

            else:
                messagebox.showwarning("Pozor","Nevyplnil si všetky prázdne políčka")
        

    def save_result(self):
        time = self.timer(1)
        with open(self.nick+'.txt', 'a') as file:
            file.write(str(time))
            file.write('\n')

    def show_average(self):
        count=0
        sum=0
        with open(self.nick+'.txt', 'r') as file:
            name = file.readline()
            hash = file.readline()
            result = file.readline()
            while result!='':
                sum +=int(result)
                count+=1
                result = file.readline()
            messagebox.showinfo("Výsledok","Váš priemerný čas je: "+str(sum//count)+' sekúnd.')
    def move(self,event):
        if self.selected is not None:
            self.canvas.coords(self.selected, event.x-50, event.y-13, event.x+50,event.y+13)
            self.canvas.coords(self.name[self.selected_name], event.x, event.y)
            self.canvas.tag_raise(self.selected)
            self.canvas.tag_raise(self.name[self.selected_name])
            self.cords_side[self.selected_name]=list((event.x-13, event.y-50, event.x+13,event.y+50))
        
        
    def stop_move(self, event):
        if self.selected is not None:
            x0,y0,x1,y1 = self.canvas.coords(self.selected) #cords of selected object
            stred=x,y = ((x1-x0)//2)+x0, ((y1-y0)//2)+y0 #cords of the center of selected object
            limit=x0,y0,x1,y1= self.ppl[self.selected_name] #cords of the place the object belong
            if x>=x0 and x<=x1 and y>=y0 and y<=y1:
                self.canvas.coords(self.selected, self.ppl[self.selected_name])
                self.canvas.coords(self.name[self.selected_name], self.names_correct[self.selected_name])
                if self.selected_name not in self.correctly_placed:
                    self.correctly_placed.append(self.selected_name)
            else:
                matched = self.find_matching_coords(event.x, event.y)
                name = self.find_matching_name(event.x, event.y)
                if name!=None:
                    x0,y0,x1,y1 = self.ppl[name]
                    x,y = ((x1-x0)//2)+x0, ((y1-y0)//2)+y0
                    self.canvas.coords(self.selected, matched)
                    self.canvas.coords(self.name[self.selected_name], x,y)
                else:
                    self.canvas.coords(self.selected, event.x-50, event.y-13, event.x+50, event.y+13)
                    self.canvas.coords(self.name[self.selected_name], event.x,event.y)
                    
            if self.selected_name not in self.placed:
                self.placed.append(self.selected_name)
            
            #print(len(self.placed), len(self.missing))
            self.selected = None
            self.selected_name=None


       
    
Login()
        
