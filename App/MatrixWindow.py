import pygame
from pygame.locals import *
import numpy as np
from AutomataCelular import *
from time import *
import threading

class App:
    """
        Cada instancia crea un cuadro que mostrara celdas dibujadas
        Se debe de especificar el tamaño en pixeles del cuatro
    """    
    def __init__(self,X_screen:int,Y_screen:int) -> None:
        # Tamaño de la ventana en px, variables fijas al instanciar
        self.X_Screen=X_screen
        self.Y_Screen=Y_screen
        
        # Declarando colores que se usaran RGB
        self.BLACK=(0,0,0)
        self.WHITE=(255,255,255)
        self.BLUE=(0,0,255)
        self.GREEN=(0,255,0)
        self.RED=(255,0,0)
        
        # Iniciando el cuadro
        pygame.init()
        flags = RESIZABLE
        self.screen = pygame.display.set_mode([self.X_Screen,self.Y_Screen],flags)
        self.running = True
            
    """
        Color de fondo de la pantalla
    """
    def setBackgroundScreenWhite(self):
        self.screen.fill(self.WHITE)
        pygame.display.update()
    
    """
        Ciclo que mantendra el cuadro a la vista y detectara los eventos.
        Aqui es en donde se creara el automata para evitar problemas en el render
        en lo que se busca una alternativa
    """
    def run(self):
        self.setBackgroundScreenWhite()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running=False
            
            pygame.display.flip()
        pygame.quit()

class MatrixComponent:
    
    def __init__(self) -> None:
        # Valiable que almacenara a la matriz
        self._MatrixArray=None 
        
        # Lado y ancho matriz dado en celdas
        self.CellsSideMatrix=None
        
        # Tamaño de la ventana donde se mostrara la amtrix
        self.SizeScreen=None
        
        # Lado y ancho de cada celula en pixeles
        self.SideCell=None
    #------------------MatrixArray-----------------------
    @property
    def MatrixArray(self):
        """numpy.ndarray: contiene los 0s y 1s"""
        return self._MatrixArray

    @MatrixArray.setter
    def MatrixArray(self, matrix_array:np.ndarray):
        self._MatrixArray = matrix_array
        self._CellsSideMatrix= matrix_array.shape[0]
        
    @MatrixArray.deleter
    def MatrixArray(self):
        del self._MatrixArray
    #----------------------------------------------------
    
    #------------------SizeScreen-----------------------
    @property
    def SizeScreen(self):
        """numpy.ndarray: contiene los 0s y 1s"""
        return self._SizeScreen

    @SizeScreen.setter
    def SizeScreen(self, matrix_array:np.ndarray):
        self._SizeScreen = matrix_array
        self._CellsSideMatrix= matrix_array.shape[0]
        
    @SizeScreen.deleter
    def SizeScreen(self):
        del self._SizeScreen
    #----------------------------------------------------
    """
        Dibuja unacelula viva
    """
    def _drawCellLive(self,x,y,w,h):
        cuadro=pygame.Rect(x,y,w,h)
        pygame.draw.rect(self.screen,self.BLACK,cuadro)
        
    """
        Dibuja unacelula muerta
    """
    def _drawCellDead(self,x,y,w,h):
        cuadro=pygame.Rect(x,y,w,h)
        pygame.draw.rect(self.screen,self.WHITE,cuadro)
    """
        De la matriz que se reciba se dibujara cada celula
    """
    def drawMatrix(self):
        self.SideCell=self.SizeScreen/self.CellsSideMatrix
        # c->columna: indicara la coodernada del eje X
        # f->fila: indicara la coordenada del eje Y
        for f in range(0,self.CellsSideMatrix):
            for c in range(0,self.CellsSideMatrix):
                if self.MatrixArray[f][c]==1:
                    self._drawCellLive(c*self.SideCell,f*self.SideCell,self.SideCell,self.SideCell)
                else:
                    self._drawCellDead(c*self.SideCell,f*self.SideCell,self.SideCell,self.SideCell)
                    


if __name__ == '__main__':

    # AC=AutomataCelular(100)
    # AC.initialRandom()

    MW=App(500,500)
    MW.run()

    
    # h1=threading.Thread(target=MW.run)
    # h1.start()
    # h1.join()

