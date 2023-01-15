
"""
    La siguiente clase no es una ventana raiz, es un frame.
    Sabiendo que en el frame se pueden agregar widgets tambien
    se pueden poner frames sobre otro frame.
    
    Al instanciar esta clase se debe de mandar la ventana raiz o el contenedor padre.
"""
from time import sleep
from tkinter import Frame, IntVar, Tk, filedialog

import numpy as np
from Logica.Colonia import Colonia
from MyFrames.Controllers import Controllers

class Window(Frame):
    
    def __init__(self,master,width:int,height:int):
        # Constructor de Frame()
        super().__init__(master,width=width,height=height,background="gray")
        self.SizeMatrix=10
        self.Centinela=False
        
        self.w_reinas=IntVar()
        self.w_trabajadoras=IntVar()
        self.w_reproductoras=IntVar()
        self.w_soldados=IntVar()
        
        self.speed=IntVar()
        self.speed.set(1000)
        
        # empaquetando elementos dentro de su ventana contenedora
        self.Centinela=False
        self.ContGeneration=0
        self.Ctls=Controllers(self)
        self.createWidgets()
        self.pack()
    
    def createWidgets(self):
        self.Ctls.btn_clear.config(command=self.clearSimulation)
        self.Ctls.btn_pause.config(command=self.pauseSimulation)
        self.Ctls.btn_run_simulation.config(command=self.runSimulation)
        
        self.Ctls.btn_load_conf.config(command=self.loadConfig)
        self.Ctls.btn_save_conf.config(command=self.saveConfig)
        
        self.Ctls.btn_reset_type_density.config(command=self.resetTypeDensity)
        
        self.Ctls.spn_box_reinas.config(command=self.updateTypeDensity,textvariable=self.w_reinas)
        self.Ctls.spn_box_reproductoras.config(command=self.updateTypeDensity,textvariable=self.w_reproductoras)
        self.Ctls.spn_box_trabajadoras.config(command=self.updateTypeDensity,textvariable=self.w_trabajadoras)
        self.Ctls.spn_box_soldados.config(command=self.updateTypeDensity,textvariable=self.w_soldados)
        
        self.Ctls.spn_box_speed.config(textvariable=self.speed)
        
        self.Ctls.scale_size_matrix.config(command=self.setLabelScaleSizeMatrix)
        
        self.Ctls.place(relx=0.02,rely=0.01)
        
        self.CH=Colonia(self,self.SizeMatrix,700)
        self.CH.drawMatrix()
        self.CH.place(relx=0.5,rely=0.01)
        
    def setLabelScaleSizeMatrix(self,v):
        # automaticamente obtiene el valor del Scale
        cad="Tamaño cuadro: "+v+" X "+v
        self.SizeMatrix=int(v)
        self.clearSimulation()
        self.Ctls.lbl1.config(text=cad)
    
    def clearSimulation(self):
        self.Centinela=False
        del self.CH
        self.CH=Colonia(self,self.SizeMatrix,700)
        self.CH.drawMatrix()
        self.CH.place(relx=0.5,rely=0.01)
        self.ContGeneration=0
        self.Ctls.lbl_num_generations.config(text="No. generaciones:"+str(self.ContGeneration))
        self.Ctls.lbl_num_cells.config(text="No. celulas:"+str(self.CH.AntsLive))
        
    
    def pauseSimulation(self):
        self.Centinela=False
        
    def runSimulation(self):
        self.Centinela=True
        while self.Centinela:
            self.CH.evaluate()
            self.CH.drawMatrix()
            
            print(self.speed.get())
            sleep(self.speed.get())
            
    def loadConfig(self):
        self.Centinela=False
        try:
            # se busca el archivo del automata
            dirname_matrix_txt=filedialog.askopenfilename()
            self.controllers.lbl_path_file_load.config(text=dirname_matrix_txt)
            
            # se carga la matriz en el canvas para su visualizacion
            # self.AC.Matriz=np.loadtxt(dirname_matrix_txt,dtype=int)
            # deserializado
            self.matrix_canvas.drawMatrix(self.controllers.InverterColorCells.get(),self.AC.Matriz)
            
            self.ContGeneration=0
            # Se continua con proceso del automata
            self.Ctls.lbl_num_generations.config(text="No. generaciones:"+str(self.ContGeneration))
            self.Ctls.lbl_num_cells.config(text="No. celulas:"+str(self.AC.StatusCellsLive))
        
        except Exception as e :
            print("Error al cargar matriz:",e)
        
    def saveConfig(self):
        self.Centinela=False
        try:
            dirname_matrix_txt=filedialog.asksaveasfilename()
            # np.savetxt(dirname_matrix_txt+'.txt',estado serializado,fmt='%d')
        except Exception as e:
            print("Error Al guardad:",e)
        
    def resetTypeDensity(self):
        self.w_reinas.set(1)
        self.w_trabajadoras.set(55)
        self.w_reproductoras.set(9)
        self.w_soldados.set(35)
        self.updateTypeDensity()
        
    def updateTypeDensity(self):
        self.CH.WReina=self.w_reinas.get()
        self.CH.WReproductora=self.w_reproductoras.get()
        self.CH.WTrabajadora=self.w_trabajadoras.get()
        self.CH.WSoldado=self.w_soldados.get()

root=Tk()
root.title("Ventana Principal")
app=Window(root,1500,750)
app.mainloop()