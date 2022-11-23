from platform import python_branch
import numpy as np
import random

"""requisitos
    
    1. Tamaño de 10000 x 10000
    2. Zoom
    3. seleccion de colores
    4. Scroll
    5. Timer o runtime
    
    6. Densidades
    7. Mostrar el numero de generaciones y 1s
    8. salvar y guardar configuraciones
    9. asignar reglas
    10. calcular media y varianza

"""

class AutomataCelular:
    
    def __init__(self,cells_side:int) -> None:
        # lado dado en celdas
        self.CellsSide=cells_side
        # contador celulas vivas
        self._StatusCellsLive=0
        # contador de celulas muertas
        self._StatusCellsDead=self.CellsSide*self.CellsSide
        #  matriz de puros ceros
        self._Matriz=np.zeros((self.CellsSide,self.CellsSide))
        self._MatrizAux=None
        
    #------------------Matriz-----------------------
    @property
    def Matriz(self):
        """numpy.ndarray: contiene los 0s y 1s"""
        return self._Matriz

    @Matriz.setter
    def Matriz(self, matrix_array:np.ndarray):
        self._Matriz = matrix_array
        self.CellsSide= matrix_array.shape[0]
        self._MatrizAux=np.zeros((self.CellsSide,self.CellsSide))
        
    @Matriz.deleter
    def Matriz(self):
        del self._Matriz
    #----------------------------------------------------
    
    @property
    def StatusCellsLive(self):
        """lado en celdas de la matriz"""
        return self._StatusCellsLive
    
    @property
    def StatusCellsDead(self):
        """lado en celdas de la matriz"""
        return self._StatusCellsDead
    
    @property
    def MatrizAux(self):
        """numpy.ndarray: contiene los 0s y 1s auxiliares"""
        return self._MatrizAux
    
    def next(self):
        self.evaluate()
        
    def evaluate(self):
        
        # celula y sus vecindades
        #    +---+---+---+
        #    | 1 | 2 | 3 |
        #    +---+---+---+
        #    | 4 |   | 5 |
        #    +---+---+---+
        #    | 6 | 7 | 8 |
        #    +---+---+---+   
        
        for i in range(0,self.CellsSide):
            for j in range(0,self.CellsSide):
                livingNeigbor=self.frontera1(i,j)
                
                if (self.Matriz[i][j]==1):
                    # Si la celula esta viva  
                    
                    if (livingNeigbor==2 or livingNeigbor==3 ):
                        # se mantiene viva
                        self.MatrizAux[i][j]=1
                    else:
                        # muere
                        self.MatrizAux[i][j]=0
                
                else:
                    # si la celula esta muerta
                    
                    if (livingNeigbor==3):
                        # revive
                        self.MatrizAux[i][j]=1
                    else:
                        # seguira muerta
                        self.MatrizAux[i][j]=0
            
        # Cambio de estado del automata 
        self.Matriz=self.MatrizAux
                
    
    def frontera1(self,x:int,y:int)->int:
        # con el siguiente caso aseguramos estabilidad dentro de la frontera
        # (frontera) (ṕosicion de la celda)
        # (x>0 && y>0)
        
        # Contador de vecinos vivios
        livingNeigbor=0 
        
        # // 1
        if ((x>0 and y>0) and (self.Matriz[x-1][y-1])):
            livingNeigbor=livingNeigbor+1
        
        
        # // 2
        if ((y>0) and (self.Matriz[x][y-1])):
            livingNeigbor=livingNeigbor+1
        
        # // 3
        if ((x<self.CellsSide-1 and y>0) and (self.Matriz[x+1][y-1])):
            livingNeigbor=livingNeigbor+1
        
        # // 4
        if ((x>0) and (self.Matriz[x-1][y])):
            livingNeigbor=livingNeigbor+1
        
        # // 5
        if ((x<self.CellsSide-1) and (self.Matriz[x+1][y])):
            livingNeigbor=livingNeigbor+1
        
        # // 6
        if ((x>0 and y<self.CellsSide-1) and (self.Matriz[x-1][y+1])):
            livingNeigbor=livingNeigbor+1
        
        # // 7
        if ((y<self.CellsSide-1) and (self.Matriz[x][y+1])):
            livingNeigbor=livingNeigbor+1
        
        # // 8
        if ((x<self.CellsSide-1 and y<self.CellsSide-1) and (self.Matriz[x+1][y+1])):
            livingNeigbor=livingNeigbor+1
        return livingNeigbor
    
    def initialRandom(self):
        for x in range(0,self.CellsSide):
            for y in range(0,self.CellsSide):
                self.Matriz[x][y]=random.choice([0,1])
    
    def initialZeros(self):
        self._Matriz=np.zeros((self.CellsSide,self.CellsSide))
        self._MatrizAux=np.zeros((self.CellsSide,self.CellsSide))
    
    def __str__(self) -> str:
        return self.Matriz.__str__()+"\n"