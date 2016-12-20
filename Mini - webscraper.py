from tkinter import *

class WordSearch:
    def __init__(self,w):
        
        self.e1=StringVar()
        self.e2=StringVar()
        self.e3=StringVar()
        self.week=StringVar()
        self.week.set("Week of ...")
        Label(w,text="Find The HOTTEST Songs").pack()
        Entry(w,textvariable=self.week,state="readonly").pack()
        f=Frame()
        f.pack()
        Label(f,text="NO.1:").grid(row=0,column=0)
        Label(f,text="NO.2:").grid(row=1,column=0)
        Label(f,text="NO.3:").grid(row=2,column=0)
        Entry(f,width=30,textvariable=self.e1,state="readonly").grid(row=0,column=1)
        Entry(f,width=30,textvariable=self.e2,state="readonly").grid(row=1,column=1)
        Entry(f,width=30,textvariable=self.e3,state="readonly").grid(row=2,column=1) 
        self.e1.set("...")
        self.e2.set("...")
        self.e3.set("...")
        Button(f,text="HIT IT",command = self.display).grid(row=3,column=1,sticky="EW")


    def getInfo(self):
        import urllib.request
        from re import findall
        self.url = "http://www.billboard.com/charts/hot-100"
        self.response = urllib.request.urlopen(self.url)
        self.data=self.response.read()
        self.text=str(self.data)
        self.data2=findall("<h1>([^<]*)</h1>",self.text)
        self.data3=findall("""<li><span class="chart_date">([^<]*)</span>""",self.text)
        return self.data2[0:3]+self.data3
        
    def display(self):
        self.list=self.getInfo()
        self.e1.set(self.list[0])
        self.e2.set(self.list[1])
        self.e3.set(self.list[2])
        self.week.set( "Week of "+self.list[3])
        
     


win=Tk()
win.title("          Billboard Top Hit           ")
app=WordSearch(win)
win.mainloop()
