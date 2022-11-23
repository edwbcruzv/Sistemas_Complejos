import copy
from time import sleep
import numpy as np
from tkinter import Tk, Frame, filedialog
from Logica.AutomataCelular import AutomataCelular
from MyFrames.MatrixCanvas import MatrixCanvas
from MyFrames.Controllers import Controllers

"""
    La siguiente clase no es una ventana raiz, es un frame.
    Sabiendo que en el frame se pueden agregar widgets tambien
    se pueden poner frames sobre otro frame.
    
    Al instanciar esta clase se debe de mandar la ventana raiz o el contenedor padre.
"""
class Window(Frame):
    
    def __init__(self,master,width:int,height:int):
        # Constructor de Frame()
        super().__init__(master,width=width,height=height)
        # empaquetando elementos dentro de su ventana contenedora
        self.Centinela=False
        self.controllers=Controllers(self)
        self.createWidgets()
        self.pack()
        
        # Instanciando el automata,
        self.AC=AutomataCelular(self.controllers.SizeMatrix)
    
    #------------------MatrixArray-----------------------
    @property
    def Centinela(self):
        """numpy.ndarray: contiene los 0s y 1s"""
        return self._Centinela

    @Centinela.setter
    def Centinela(self, centinela:bool):
        self._Centinela = centinela
        print("Valor del centinela:",self._Centinela)
        
    @Centinela.deleter
    def Centinela(self):
        del self._Centinela
    #----------------------------------------------------
    
    # Aqui se crean todos los widgets del frame
    def createWidgets(self):
        # area de botones y sus controladores
        self.controllers.btn_run_simulation.config(command=self.runSimulation)
        self.controllers.btn_load_conf.config(command=self.loadConfig)
        self.controllers.btn_pause.config(command=self.pauseSimulation)
        self.controllers.btn_save_conf.config(command=self.saveConfig)
        self.controllers.btn_reset.config(command=self.resetSimulation)
        self.controllers.btn_density_graph.config(command=self.showDensityGraphs)
        self.controllers.place(relx=0.02,rely=0.02)
        
        # se define el tamaño estatico del canvas en pixeles y la posicion
        self.matrix_canvas=MatrixCanvas(self,600)
        self.matrix_canvas.place(relx=0.5,rely=0.01)
    
    def showDensityGraphs(self):
        pass
    
    def resetSimulation(self):
        # Se borra la configuracion actual del automata
        self.Centinela=False
        self.AC.initialZeros()
        self.matrix_canvas.MatrixArray=self.AC.Matriz
        self.matrix_canvas.drawMatrix()
        self.matrix_canvas.update()
        
    
    def pauseSimulation(self):
        # Se pausa la simulacion
        self.Centinela=False
        
        
    def saveConfig(self):
        self.Centinela=False
        dirname_matrix_txt=filedialog.asksaveasfile()
        self.Centinela=True
        
    
    def loadConfig(self):
        # se rompe el proceso del automata 
        self.Centinela=False
        # se busca el archivo del automata
        dirname_matrix_txt=filedialog.askopenfile()
        
        self.controllers.lbl_path_file_load.config(text=dirname_matrix_txt)
        
        # se carga la matriz en el canvas para su visualizacion
        self.AC.Matriz=np.loadtxt(dirname_matrix_txt,dtype=int)
        self.matrix_canvas.MatrixArray=self.AC.Matriz
        self.matrix_canvas.drawMatrix()
        self.matrix_canvas.update()
        
        # Se continua con proceso del automata
        self.Centinela=True
    
    def runSimulation(self):
        # se tomara la matriz que este cargada en el automata
        
        while self.Centinela:
            # esta linea cambia la matriz del canvas
            self.matrix_canvas.MatrixArray=self.AC.Matriz
            # se actualiza el canvas y de dibujan las formas
            self.matrix_canvas.drawMatrix()
            # se actualiza el frame del canvas
            self.matrix_canvas.update()
            # se pasa al siguiente estado del automata
            self.AC.next()
            # time
            
            sleep(self.controllers.SpeedSim)


root=Tk()
root.title("Ventana Principal")
app=Window(root,1300,700)
app.mainloop()