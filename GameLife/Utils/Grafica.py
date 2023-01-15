from tkinter import Tk,Label,Frame,Entry,Button
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
# la clase no es una ventana raiz, es un FRAME
class Grafica(Frame):
    
    def __init__(self,master,width:int,height:int):
        # Constructor de Frame()
        super().__init__(master,width=width,height=height)
        # empaquetando elementos dentro de su ventana contenedora
        self.pack()
        
    
    # Aqui se crean todos los widgets del frame
    
    def createGraph(self,width:int,height:int):

        # Definimos las figuras y sus posiciones en la ventana
        # Para ello utilizamos "Figure"
        fig = Figure( figsize=(width,height) )
        
        self.ejes=fig.add_subplot()
        self.linea,=self.ejes.plot([],[])
        self.ejes.set_ylabel("celulas vivas")
        self.ejes.set_xlabel("Generacion")
        self.ejes.set_title("Life")
        
        self.canvas=FigureCanvasTkAgg(fig,self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        
        toolbar=NavigationToolbar2Tk(self.canvas,self,pack_toolbar=False)
        toolbar.update()
        toolbar.pack()
        
    def updateGraph(self,x:list,y:list):
        self.linea.set_data(x,y)
        self.canvas.draw()
       
        
        

        

# root=Tk()
# root.title("Ejemplo de place")
# app=Grafica(root,100,100)
# app.createGraph(8,4)
# app.updateGraph([0,1,2,3],[0,5,7,2])
# app.mainloop()