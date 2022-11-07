import pygame
import numpy as np
from AutomataCelular import *
from time import *

class MatrixWindow:
    """
        Cada instancia crea un cuadro que mostrara celdas dibujadas
        Se debe de especificar el tamaño en pixeles del cuatro
    """    
    def __init__(self,X_screen:int,Y_screen:int) -> None:
        # Tamaño del cuatro
        self.X_Screen=X_screen
        self.Y_Screen=Y_screen
        
        #declarando colores que se usaran RGB
        self.BLACK=(0,0,0)
        self.WHITE=(255,255,255)
        self.BLUE=(0,0,255)
        self.GREEN=(0,255,0)
        self.RED=(255,0,0)
        
        # Iniciando el cuadro
        pygame.init()
        self.screen = pygame.display.set_mode([self.X_Screen,self.Y_Screen])

    """
        Color de fondo de la pantalla
    """
    def setBackgroundScreenWhite(self):
        self.screen.fill(self.WHITE)
        pygame.display.update()
    
    """
        Dibuja unacelula viva
    """
    def drawCellLive(self,x,y,w,h):
        cuadro=pygame.Rect(x,y,w,h)
        pygame.draw.rect(self.screen,self.BLACK,cuadro)
    
    
    def flipScreen(self):
        pygame.display.flip()
        
    """
        Dibuja unacelula muerta
    """
    def drawCellDead(self,x,y,w,h):
        cuadro=pygame.Rect(x,y,w,h)
        pygame.draw.rect(self.screen,self.WHITE,cuadro)
    """
        De la matriz que se reciba se dibujara cada celula
    """
    def drawMatrix(self,matrix:np.ndarray,side_cell:float):
        
        # c->columna: indicara la coodernada del eje X
        # f->fila: indicara la coordenada del eje Y
        for f in range(0,matrix.shape[0]):
            for c in range(0,matrix.shape[1]):
                if matrix[f][c]==1:
                    self.drawCellLive(c*side_cell,f*side_cell,side_cell,side_cell)
                else:
                    self.drawCellDead(c*side_cell,f*side_cell,side_cell,side_cell)
        self.flipScreen()
    
    """
        Ciclo que mantendra el cuadro a la vista y detectara los eventos
        
        Aqui es en donde se creara el automata para evitar problemas en el render
        en lo que se busca una alternativa
    """
    def mainloop(self,tam_automata_c:int,runtime:float):
        self.setBackgroundScreenWhite()
        running=True
        side_cell=self.X_Screen/tam_automata_c
        
        AC=AutomataCelular(tam_automata_c)
        AC.initialRandom()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
            
            sleep(runtime)
            AC.next()
            self.drawMatrix(AC.Matriz,side_cell)

                   
