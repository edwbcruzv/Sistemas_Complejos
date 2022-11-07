from tkinter import Tk,Label,Frame,Entry,Button,Scale,Checkbutton
from MatrixWindow import *
from AutomataCelular import *

"""
    La siguiente clase no es una ventana raiz, es un frame.
    Sabiendo que en el frame se pueden agregar widgets tambien
    se pueden poner frames sobre otro frame.
    
    Al instanciar esta clase se debe de mandar la ventana raiz o el contenedor padre.
"""
class MyFrame(Frame):
    
    def __init__(self,master,width:int,height:int):
        # Constructor de Frame()
        super().__init__(master,width=width,height=height)
        # empaquetando elementos dentro de su ventana contenedora
        self.pack()
        self.createWidgets()
        
        # MW=MatrixWindow(500,500)
        # MW.mainloop(110,0.5)
        
        
        
    
    # Aqui se crean todos los widgets del frame
    def createWidgets(self):
        self.lbl1=Label(self,text="Desliza...")
        self.lbl1.place(x=10,y=10,width=250,height=30)
        
        self.scl1=Scale(self,orient="horizontal",command=self.setLabelScale,from_=500,to=5000,
                        tickinterval=100,resolution=0)
        self.scl1.place(x=10,y=40,width=400,height=40)

        self.lbl2=Label(self,text="No. generaciones:")
        self.lbl2.place(x=300,y=400,width=100,height=20)
        
        self.lbl3=Label(self,text="No. celulas:")
        self.lbl3.place(x=300,y=420,width=100,height=20)

     

        # self.lbl3=Label(self,text="Tercer numero", bg="yellow")
        # self.lbl3.place(x=10,y=100,width=100,height=30)

        # self.txt3=Entry(self, bg="pink")
        # self.txt3.place(x=120,y=100,width=100,height=30)

        self.btn1=Button(self,text="Guardar Configuracion",command=self.saveConfig)
        self.btn1.place(x=10,y=400,width=130,height=30)
        
        self.btn2=Button(self,text="Cargar Configuracion",command=self.loadConfig)
        self.btn2.place(x=150,y=400,width=130,height=30)
        
        self.btn3=Button(self,text="Correr simulacion")
        self.btn3.place(x=10,y=450,width=400,height=30)
        
        self.cbtn1=Checkbutton(self,text="Color")
        self.cbtn1.place(x=400,y=10,width=100,height=30)
    
    def setLabelScale(self,v):
        # automaticamente obtiene el valor del Scale
        cad="Tamaño cuadro: "+str(v)+" X "+str(v)
        self.lbl1.config(text=cad)
        
    def saveConfig(self):
        pass
    
    def loadConfig(self):
        pass
    
    def runSimulation(self):
        MW=MatrixWindow(500,500)
        MW.mainloop(110,0.5)

root=Tk()
root.title("Ejemplo de place")
app=MyFrame(root,500,500)
app.mainloop()