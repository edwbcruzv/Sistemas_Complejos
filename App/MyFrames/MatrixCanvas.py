from math import floor
from tkinter import Scrollbar, Tk,Frame,Canvas
import numpy as np
from Utils.Constantes import *

class MatrixCanvas(Frame):
    
    def __init__(self,master,size:int):
        # Constructor de Frame()
        super().__init__(master,width=size,height=size)
        # Tamaño del canvas
        self.__SizeCanvas=size
        
        # Variable que almacenara a la matriz,
        # Se calcula al settear la matriz
        self.__MatrixArray=None 
        
        # Lado y ancho matriz dado en celdas
        # Se calcula al settear la matriz
        self.CellsSideMatrix=None
        
        # Lado y ancho de cada celula en pixeles,
        # Se calcula al momento de leer e imprimir la matriz
        self.SideCell=None
        
        # empaquetando elementos dentro de su ventana contenedora
        self.createWidgets()
        self.pack()
        
    #------------------MatrixArray-----------------------
    @property
    def MatrixArray(self):
        """numpy.ndarray: contiene los 0s y 1s"""
        return self.__MatrixArray

    @MatrixArray.setter
    def MatrixArray(self, matrix_array:np.ndarray):
        self.__MatrixArray = matrix_array
        self.CellsSideMatrix= matrix_array.shape[0]
        
    @MatrixArray.deleter
    def MatrixArray(self):
        del self.__MatrixArray
    #----------------------------------------------------
    
    #------------------SizeCanvas-----------------------
    @property
    def SizeCanvas(self):
        """numpy.ndarray: contiene los 0s y 1s"""
        return self.__SizeCanvas
    #----------------------------------------------------
    
    def createWidgets(self):
        self.cv1=Canvas(self,width=self.SizeCanvas,height=self.SizeCanvas,background=WHITE)
        
        # self.hbar_x=Scrollbar(self,orient="horizontal",command=self.cv1.xview)
        # self.hbar_x.pack(side="bottom",fill="x")
        
        # self.hbar_y=Scrollbar(self,orient="vertical",command=self.cv1.yview)
        # self.hbar_y.pack(side="right",fill="y")
        
        self.cv1.bind("<Button-1>",self._alterate) # clic izquierdo
        
        # self.cv1.config(xscrollcommand=self.hbar_x.set,yscrollcommand=self.hbar_y.set)
        # self.cv1.create_rectangle(50,50,100,100,fill="white",outline="blue")
        # self.cv1.create_rectangle(50,110,100,160,fill="black",outline="blue")
        # self.cv1.create_rectangle(100,100,200,200,fill="white",outline="black")
        self.cv1.pack()
        
    def drawMatrix(self,invert_color:bool=False,matrix_array:np.ndarray=np.zeros((2,2),dtype=int)):
        self.MatrixArray=matrix_array
        
        if invert_color:
            self.ColorCellLive=WHITE
            self.ColorCellDead=BLACK
        else:
            self.ColorCellLive=BLACK
            self.ColorCellDead=WHITE
            
        # Se calcula el lado del la celula 
        # lado_celula=lado_canvas/num_celulas
        self.SideCell=self.SizeCanvas/self.CellsSideMatrix
        # self.SideCell=1
        # limpia la memoria, esto para evitar que se tarde y trabe el programa
        self.cv1.delete("all")
        # c->columna: indicara la coodernada del eje X
        # f->fila: indicara la coordenada del eje Y
        # print(self.CellsSideMatrix)
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
        
    def _alterate(self,event):
        var=(self.SizeCanvas/self.CellsSideMatrix)
        c=floor(event.x/var)
        f=floor(event.y/var)
        # print(f, c)
        if self.MatrixArray[f][c]==1:
            self.MatrixArray[f][c]=0
            self._drawCell(c*self.SideCell,f*self.SideCell,(c*self.SideCell)+self.SideCell,(f*self.SideCell)+self.SideCell,self.ColorCellDead)
        else:
            self.MatrixArray[f][c]=1
            self._drawCell(c*self.SideCell,f*self.SideCell,(c*self.SideCell)+self.SideCell,(f*self.SideCell)+self.SideCell,self.ColorCellLive)

# root=Tk()
# root.title("Ejemplo de canvas")
# app=MatrixCanvas(root,500)
# app.drawMatrix()
# app.mainloop()