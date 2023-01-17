import random
from time import sleep
import numpy as np
from Logica.Hormiga import Hormiga
from math import floor
from tkinter import ALL, Frame,Canvas, Tk
# from Utils.Constantes import *
from Logica.Constantes import *


class Colonia(Frame):
    
    def __init__(self,master,cells_side:int,size:int) -> None:
        # Constructor de Frame()
        super().__init__(master,width=size,height=size)
        self.SizeCanvas=size
        self.CellsSide=cells_side
        self.SideCell=None
        
        self.__ColorReina=COLOR_2
        self.__ColorTrabajadora=COLOR_4
        self.__ColorReproductora=COLOR_6
        self.__ColorSoldado=COLOR_8
        
        self.__WReina=1
        self.__WTrabajadora=55
        self.__WReproductora=9
        self.__WSoldado=35
        
        # Definiendo el espacio que contendra la colonia en celdas
        self.RastrosHormigasMatrix=np.zeros((cells_side,cells_side),dtype=int)
        self.__Hormigas=list()
        self.__AntsLive=len(self.__Hormigas)
        
        # empaquetando elementos dentro de su ventana contenedora
        self.createWidgets()
        self.pack()
    """
    #------------------------------------
    @property
    def Atributo(self):
        # Documentacion de Atributo 
        return self.__Atributo
    
    @Atributo.setter
    def Atributo(self,new_Atributo):
        self.__Atributo=new_Atributo
    
    @Atributo.deleter
    def Atributo(self):
        del self.__Atributo
    #------------------------------------
    """
    
    #------------------------------------
    @property
    def Hormigas(self):
        # Documentacion de Hormigas 
        return self.__Hormigas
    
    @Hormigas.setter
    def Hormigas(self,new_Hormigas):
        self.__Hormigas=new_Hormigas
    
    @Hormigas.deleter
    def Hormigas(self):
        del self.__Hormigas
    #------------------------------------
    
    #------------------------------------
    @property
    def AntsLive(self):
        # Documentacion de AntsLive 
        self.__AntsLive=len(self.Hormigas)
        return self.__AntsLive
    
    @AntsLive.setter
    def AntsLive(self,new_AntsLive):
        self.__AntsLive=new_AntsLive
    
    @AntsLive.deleter
    def AntsLive(self):
        del self.__AntsLive
    #------------------------------------
    
    #------------------------------------
    @property
    def ColorReina(self):
        # Documentacion de ColorReina 
        return self.__ColorReina
    #------------------------------------
    
    #------------------------------------
    @property
    def ColorTrabajadora(self):
        # Documentacion de ColorTrabajadora 
        return self.__ColorTrabajadora
    #------------------------------------
    
    #------------------------------------
    @property
    def ColorReproductora(self):
        # Documentacion de ColorReproductora 
        return self.__ColorReproductora
    #------------------------------------
    
    #------------------------------------
    @property
    def ColorSoldado(self):
        # Documentacion de ColorSoldado 
        return self.__ColorSoldado
    #------------------------------------
    
    #------------------------------------
    @property
    def WReina(self):
        # Documentacion de WReina 
        return self.__WReina
    
    @WReina.setter
    def WReina(self,new_WReina):
        self.__WReina=new_WReina
    
    @WReina.deleter
    def WReina(self):
        del self.__WReina
    #------------------------------------
    
    #------------------------------------
    @property
    def WTrabajadora(self):
        # Documentacion de WTrabajadora 
        return self.__WTrabajadora
    
    @WTrabajadora.setter
    def WTrabajadora(self,new_WTrabajadora):
        self.__WTrabajadora=new_WTrabajadora
    
    @WTrabajadora.deleter
    def WTrabajadora(self):
        del self.__WTrabajadora
    #------------------------------------
    
    #------------------------------------
    @property
    def WReproductora(self):
        # Documentacion de WReproductora 
        return self.__WReproductora
    
    @WReproductora.setter
    def WReproductora(self,new_WReproductora):
        self.__WReproductora=new_WReproductora
    
    @WReproductora.deleter
    def WReproductora(self):
        del self.__WReproductora
    #------------------------------------
    
    #------------------------------------
    @property
    def WSoldado(self):
        # Documentacion de WSoldado 
        return self.__WSoldado
    
    @WSoldado.setter
    def WSoldado(self,new_WSoldado):
        self.__WSoldado=new_WSoldado
    
    @WSoldado.deleter
    def WSoldado(self):
        del self.__WSoldado
    #------------------------------------
        
    def createWidgets(self):
        self.cv1=Canvas(self,width=self.SizeCanvas,height=self.SizeCanvas,background=WHITE)
        self.cv1.bind("<Button-1>",self._alterate) # clic izquierdo
        
        self.cv1.bind("<MouseWheel>", self.do_zoom)
        self.cv1.bind('<ButtonPress-3>', lambda event: self.cv1.scan_mark(event.x, event.y))
        self.cv1.bind("<B3-Motion>", lambda event: self.cv1.scan_dragto(event.x, event.y, gain=1))   
        self.cv1.bind('<space>', self.pausar)
        self.cv1.pack()

    def do_zoom(self, event):
        x = self.cv1.canvasx(event.x)
        y = self.cv1.canvasy(event.y)
        self.factor = 1.001 ** event.delta
        self.cv1.scale(ALL, x, y, self.factor, self.factor)
    
    def pausar(self):
        if not self.pausa:
            self.pausa = True
            self.boton_pausa.config(text="Play")
        else:
            self.pausa = False
            self.boton_pausa.config(text="Pausa")
            
    def drawMatrix(self,active_rastro:bool=True):
        # Se calcula el lado del la celula 
        # lado_celula=lado_canvas/num_celulas
        self.SideCell=self.SizeCanvas/self.CellsSide
        # limpia la memoria, esto para evitar que se tarde y trabe el programa
        self.cv1.delete("all")
        try:
            if active_rastro:
                self._drawRastroAnts()
            self._drawHeadsAnts()
        except :
            print("algo paso")
        
    def _drawRastroAnts(self):
        
        # c->columna: indicara la coodernada del eje X
        # f->fila: indicara la coordenada del eje Y
        # print(self.CellsSide)
        for f in range(0,self.CellsSide):
            for c in range(0,self.CellsSide):
                if self.RastrosHormigasMatrix[f][c]==0:
                    # se dibuja la celula muerta
                    self._drawCell(c*self.SideCell,f*self.SideCell,(c*self.SideCell)+self.SideCell,(f*self.SideCell)+self.SideCell,WHITE)
                else:
                    # se dibuja el rastro vivo
                    id_aux=int(self.RastrosHormigasMatrix[f][c])
                    h_aux=self.Hormigas[self.Hormigas.index(id_aux)]
                    color=h_aux.Color
                    self._drawCell(c*self.SideCell,f*self.SideCell,(c*self.SideCell)+self.SideCell,(f*self.SideCell)+self.SideCell,color)
        
        self.cv1.pack() # no quitar esta linea
        
    def _drawCell(self,x0,y0,x1,y1,color):
        self.cv1.create_rectangle(x0,y0,x1,y1,fill=color,outline=color)
        
    def _drawHeadsAnts(self):
        
        for h in self.Hormigas:
            if h.Live>=80:
                self.deleteAnt(h.ID)
                continue
            color=h.Color
            f=h.X_pos
            c=h.Y_pos
            self.cv1.create_rectangle(c*self.SideCell,f*self.SideCell,(c*self.SideCell)+self.SideCell,(f*self.SideCell)+self.SideCell,fill=color,outline=BLACK)
            self.cv1.create_line(c*self.SideCell,f*self.SideCell,(c*self.SideCell)+self.SideCell,(f*self.SideCell)+self.SideCell)
            self.cv1.create_line(c*self.SideCell,(f*self.SideCell)+self.SideCell,(c*self.SideCell)+self.SideCell,f*self.SideCell)
            
        self.cv1.pack() # no quitar esta linea
        
    def _alterate(self,event):
        var=(self.SizeCanvas/self.CellsSide)
        c=floor(event.x/var)
        f=floor(event.y/var)
        try:
            if self.RastrosHormigasMatrix[f][c]==0:
                h=self._RandomAnt(f,c)
                self.Hormigas.append(h)
                self._drawHeadsAnts()
            else:
                self.deleteAnt(int(self.RastrosHormigasMatrix[f][c]))
                self._drawHeadsAnts()
        except:
            print("paso en alterar")
            
    def _addRandomAnt(self):
        self.Hormigas.append(self._RandomAnt())
        
    def _RandomAnt(self,x:int=None,y:int=None):
        colores=([self.__ColorReina,self.__ColorTrabajadora,self.__ColorReproductora,self.__ColorSoldado])
        pesos=[self.WReina,self.WTrabajadora,self.WReproductora,self.WSoldado]
        # print(pesos)
        
        orientacion=random.choice(['N','E','O','S'])
        if x==None or y==None:
            x=random.randint(0,self.CellsSide-1)
            y=random.randint(0,self.CellsSide-1)
        return Hormiga(random.choices(colores,weights=pesos),
                                     orientacion,
                                     [x,y])
        
        # Se elimina la hormiga al tener el ID
    def deleteAnt(self,id_ant):
        # se elimina la hormiga de la lista
        h_aux=self.Hormigas[self.Hormigas.index(id_ant)]
        self.Hormigas.remove(h_aux)
        # se limpia toda la matriz de rastros
        for f in range(0,self.CellsSide):
            for c in range(0,self.CellsSide):
                if self.RastrosHormigasMatrix[f][c]==id_ant:
                    self.RastrosHormigasMatrix[f][c]=0
                    
    def distribution(self,porcent:int):
        
        for f in range(0,self.CellsSide):
            for c in range(0,self.CellsSide):
                if random.uniform(0,100)<porcent:
                    self.Hormigas.append(self._RandomAnt(f,c))
        
        
        
    def evaluate(self,border:int=0):
        # print(self.CellsSide)
        # print(self.RastrosHormigasMatrix.shape)
        # self.rules()
        
        for h in self.Hormigas:
                # La Celula esta Muerta.
            if self.RastrosHormigasMatrix[h.X_pos][h.Y_pos]==0:
                # Gira 90 grados a la derecha.
                h.rotate90Right()
                # cambia la célula actual con su ID 
                self.RastrosHormigasMatrix[h.X_pos][h.Y_pos]=h.ID
                # avanza una célula adelante
                h.moveForward()
            else:# La celula esta viva (hay un rastro)
                # Gira 90 grados a la izquierda
                h.rotate90Left()
                # cambia célula actual a una célula muerta
                self.RastrosHormigasMatrix[h.X_pos][h.Y_pos]=0
                # avanza una célula adelante
                h.moveForward()
            
            # condiciones de frontera
            if (border==0) and (h.X_pos==-1 or h.Y_pos==-1 or h.X_pos==self.CellsSide or h.Y_pos==self.CellsSide): # reflectora
                h.rotate180()
                h.moveForward()
                # print("Peligro 0!!!")
            elif (border==1): # Toroide
                if h.X_pos==-1:
                    h.X_pos=self.CellsSide-1
                elif h.Y_pos==-1:
                    h.Y_pos=self.CellsSide-1
                elif h.X_pos==self.CellsSide:
                    h.X_pos=0
                elif h.Y_pos==self.CellsSide:
                    h.Y_pos=0
                # print("Peligro 1!!!")
    
    def rules(self):
        
        self.EvaluateMatrix=np.zeros((self.CellsSide,self.CellsSide),dtype=int)
        
        for h in self.Hormigas:
            self.EvaluateMatrix[h.X_pos][h.Y_pos]=h.ID
            
        for f in range(0,self.CellsSide):
            for c in range(0,self.CellsSide):
                pass
                
                    
    def __str__(self) -> str:
        return self.RastrosHormigasMatrix.__str__()+"\n"
    
