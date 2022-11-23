from tkinter import Tk,Frame,Canvas


import numpy as np

class MatrixCanvas(Frame):
    
    def __init__(self,master,size:int):
        # Constructor de Frame()
        super().__init__(master,width=size,height=size)
        # Tamaño del canvas
        self._SizeCanvas=size
        
        # Variable que almacenara a la matriz,
        # Se calcula al settear la matriz
        self._MatrixArray=None 
        
        # Lado y ancho matriz dado en celdas
        # Se calcula al settear la matriz
        self.CellsSideMatrix=None
        
        
        # Lado y ancho de cada celula en pixeles,
        # Se calcula al momento de leer e imprimir la matriz
        self.SideCell=None
        
        # Variables de los colores
        self.WHITE="white"
        self.BLACK="black"
        
        # Variables de los colores de las celulas vivas y muertas
        self.ColorCellLive=self.BLACK
        self.ColorCellDead=self.WHITE
        
        # empaquetando elementos dentro de su ventana contenedora
        self.createWidgets()
        self.pack()
        
    #------------------MatrixArray-----------------------
    @property
    def MatrixArray(self):
        """numpy.ndarray: contiene los 0s y 1s"""
        return self._MatrixArray

    @MatrixArray.setter
    def MatrixArray(self, matrix_array:np.ndarray):
        self._MatrixArray = matrix_array
        self.CellsSideMatrix= matrix_array.shape[0]
        
    @MatrixArray.deleter
    def MatrixArray(self):
        del self._MatrixArray
    #----------------------------------------------------
    
    #------------------SizeCanvas-----------------------
    @property
    def SizeCanvas(self):
        """numpy.ndarray: contiene los 0s y 1s"""
        return self._SizeCanvas

    def createWidgets(self):
        self.cv1=Canvas(self,width=self._SizeCanvas,height=self._SizeCanvas,background=self.WHITE)
        # self.cv1.create_rectangle(50,50,100,100,fill="white",outline="blue")
        # self.cv1.create_rectangle(50,110,100,160,fill="black",outline="blue")
        # self.cv1.create_rectangle(100,100,200,200,fill="white",outline="black")
        
        
    def drawMatrix(self):
        
        # Se calcula el lado del la celula 
        # lado_celula=lado_canvas/num_celulas
        self.SideCell=self._SizeCanvas/self.CellsSideMatrix
        
        # c->columna: indicara la coodernada del eje X
        # f->fila: indicara la coordenada del eje Y
        for f in range(0,self.CellsSideMatrix):
            for c in range(0,self.CellsSideMatrix):
                if self.MatrixArray[f][c]==1:
                    self._drawCell(c*self.SideCell,f*self.SideCell,(c*self.SideCell)+self.SideCell,(f*self.SideCell)+self.SideCell,self.ColorCellLive)
                else:
                    self._drawCell(c*self.SideCell,f*self.SideCell,(c*self.SideCell)+self.SideCell,(f*self.SideCell)+self.SideCell,self.ColorCellDead)
        self.cv1.pack() # no quitar esta linea

    """
        Dibuja una celula
    """
    def _drawCell(self,x0,y0,x1,y1,color):
        self.cv1.create_rectangle(x0,y0,x1,y1,fill=color,outline=color)


# root=Tk()
# root.title("Ejemplo de canvas")
# # AC=AutomataCelular(10)
# # AC.initialRandom()
# app=MatrixCanvas(root,500)
# # app.MatrixArray=AC.Matriz
# # app.drawMatrix()
# app.mainloop()