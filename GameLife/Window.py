from time import sleep
import numpy as np
from tkinter import Tk, Frame, filedialog
from Utils.Grafica import Grafica
from Logica.AutomataCelular import AutomataCelular
from MyFrames.MatrixCanvas import MatrixCanvas
from MyFrames.Controllers import Controllers
import matplotlib.pyplot as plt

"""
    La siguiente clase no es una ventana raiz, es un frame.
    Sabiendo que en el frame se pueden agregar widgets tambien
    se pueden poner frames sobre otro frame.
    
    Al instanciar esta clase se debe de mandar la ventana raiz o el contenedor padre.
"""
class Window(Frame):
    
    def __init__(self,master,width:int,height:int):
        # Constructor de Frame()
        super().__init__(master,width=width,height=height,background="gray")
        # empaquetando elementos dentro de su ventana contenedora
        self.Centinela=False
        self.ContGeneration=0
        self.controllers=Controllers(self)
        self.createWidgets()
        self.pack()
        
        self.x=[]
        self.y=[]
        
        # Instanciando el automata,
        self.SpeedSim=0.001
        self.SizeMatrix=10
        self.AC=AutomataCelular(10)
        self.clearSimulation()
    
    
    # Aqui se crean todos los widgets del frame
    def createWidgets(self):
        # area de botones y sus controladores
        self.controllers.btn_run_simulation.config(command=self.runSimulation)
        self.controllers.btn_load_conf.config(command=self.loadConfig)
        self.controllers.btn_pause.config(command=self.pauseSimulation)
        self.controllers.btn_save_conf.config(command=self.saveConfig)
        self.controllers.btn_reset.config(command=self.randomDensity)
        self.controllers.btn_clear.config(command=self.clearSimulation)
        self.controllers.scale_speed_sim.config(command=self.setLabelScaleSpeedSim,from_=0.001,to=5,
                        tickinterval=0.001,resolution=0.001)
        self.controllers.scale_size_matrix.config(command=self.setLabelScaleSizeMatrix,from_=10,to=5000,
                        tickinterval=10,resolution=10)
        
        # Posicion de los controles en la ventana principal
        self.controllers.place(relx=0.02,rely=0.01)
        
        # se define el tamaño estatico del canvas en pixeles y la posicion
        self.matrix_canvas=MatrixCanvas(self,650)
        self.matrix_canvas.place(relx=0.5,rely=0.01)
        # Grafica
        self.graph=Grafica(self,100,100)
        self.graph.createGraph(7,3.5)
        # self.graph.updateGraph([0,1,2,3],[0,5,7,2])
        self.graph.place(relx=0.02,rely=0.46)
        
    def setLabelScaleSizeMatrix(self,v):
        # automaticamente obtiene el valor del Scale
        self.Centinela=False
        cad="Tamaño cuadro: "+v+" X "+v
        self.SizeMatrix=int(v)
        self.AC.setShape(int(v))
        self.controllers.lbl1.config(text=cad)
    
    def setLabelScaleSpeedSim(self,v):
        # automaticamente obtiene el valor del Scale
        self.Centinela=False
        cad="Velocidad simulacion: "+v
        self.SpeedSim=float(v)
        self.controllers.lbl4.config(text=cad)
    
    def clearSimulation(self):
        # Se borra la configuracion actual del automata
        self.Centinela=False
        # Asignando el tamaño definido anteriormente
        self.AC.initialZeros(self.SizeMatrix)
        self.matrix_canvas.drawMatrix(self.controllers.InverterColorCells.get(),self.AC.Matriz)
        self.matrix_canvas.update()
        self.ContGeneration=0
        self.x=[]
        self.y=[]
        self.controllers.lbl_num_generations.config(text="No. generaciones:"+str(self.ContGeneration))
        self.controllers.lbl_num_cells.config(text="No. celulas:"+str(self.AC.StatusCellsLive))
    
    def randomDensity(self):
        # Se borra la configuracion actual del automata
        self.Centinela=False
        # Asignando el tamaño definido anteriormente
        self.AC.initialRandom(self.SizeMatrix)
        self.matrix_canvas.drawMatrix(self.controllers.InverterColorCells.get(),self.AC.Matriz)
        self.matrix_canvas.update()
        self.ContGeneration=0
        self.x=[]
        self.y=[]
        self.controllers.lbl_num_generations.config(text="No. generaciones:"+str(self.ContGeneration))
        self.controllers.lbl_num_cells.config(text="No. celulas:"+str(self.AC.StatusCellsLive))
        
    def pauseSimulation(self):
        # Se pausa la simulacion
        self.Centinela=False
        
    def saveConfig(self):
        self.Centinela=False
        try:
            dirname_matrix_txt=filedialog.asksaveasfilename()
            np.savetxt(dirname_matrix_txt+'.txt',self.matrix_canvas.MatrixArray,fmt='%d')
        except Exception as e:
            print("Error Al guardad:",e)
        
            
    def loadConfig(self):
        # se rompe el proceso del automata 
        self.Centinela=False
        try:
            # se busca el archivo del automata
            dirname_matrix_txt=filedialog.askopenfilename()
            self.controllers.lbl_path_file_load.config(text=dirname_matrix_txt)
            
            # se carga la matriz en el canvas para su visualizacion
            self.AC.Matriz=np.loadtxt(dirname_matrix_txt,dtype=int)
            self.matrix_canvas.drawMatrix(self.controllers.InverterColorCells.get(),self.AC.Matriz)
            self.matrix_canvas.update()
            self.ContGeneration=0
            # Se continua con proceso del automata
            self.controllers.lbl_num_generations.config(text="No. generaciones:"+str(self.ContGeneration))
            self.controllers.lbl_num_cells.config(text="No. celulas:"+str(self.AC.StatusCellsLive))
        
        except Exception as e :
            print("Error al cargar matriz:",e)
        
    
    
    def runSimulation(self):
        
        self.Centinela=True
        while self.Centinela:
            self.ContGeneration=self.ContGeneration+1
            self.controllers.lbl_num_generations.config(text="No. generaciones:"+str(self.ContGeneration))
            self.controllers.lbl_num_cells.config(text="No. celulas:"+str(self.AC.StatusCellsLive))
            self.x.append(self.ContGeneration)
            self.y.append(self.AC.StatusCellsLive)
            
            self.graph.updateGraph(self.x,self.y)
            # self.graph.updateGraph([0,1,2,3],[0,5,7,2])
            
            # self.graph.update()
            # se actualiza el canvas y de dibujan las formas
            self.matrix_canvas.drawMatrix(self.controllers.InverterColorCells.get(),self.AC.Matriz)
            # se actualiza el frame del canvas
            self.matrix_canvas.update()
            
            sleep(self.SpeedSim)
            # se pasa al siguiente estado del automata
            self.AC.evaluate(self.controllers.OptionBorder.get())
            


root=Tk()
root.title("Ventana Principal")
app=Window(root,1500,750)
app.mainloop()