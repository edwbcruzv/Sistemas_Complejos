import numpy as np


class AutomataCelular:
    
    def __init__(self,cells_side:int) -> None:
        # lado dado en celdas
        self.CellsSide=cells_side
        # contador celulas vivas
        self._StatusCellsLive=0
        # contador de celulas muertas
        self._StatusCellsDead=self.CellsSide*self.CellsSide
        #  matriz de puros ceros
        self.__Matriz=None
        self._MatrizAux=None
        self.initialZeros()
        
    #------------------Matriz-----------------------
    @property
    def Matriz(self):
        """numpy.ndarray: contiene los 0s y 1s"""
        return self.__Matriz

    @Matriz.setter
    def Matriz(self, matrix_array:np.ndarray):
        self.__Matriz = matrix_array
        self.CellsSide= matrix_array.shape[0]
        # self._MatrizAux=np.zeros((self.CellsSide,self.CellsSide),dtype=int)
        
    @Matriz.deleter
    def Matriz(self):
        del self.__Matriz
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
    
    def setShape(self,cells_side:int):
        self.CellsSide= cells_side
        
    def evaluate(self,border:int=0):
        self._StatusCellsLive=0
        self._MatrizAux=np.zeros((self.CellsSide,self.CellsSide),dtype=int)
        bandera_toggle=False
        
        if self.CellsSide>self.Matriz.shape[0]:
            # si el tamaño aumento
            self.CellsSide=self.Matriz.shape[0]
            bandera_toggle=True
            
        for f in range(0,self.CellsSide):
            for c in range(0,self.CellsSide):
                if border==0:
                    livingNeigbor=self.Border0(f,c) 
                if border==1:
                    livingNeigbor=self.Border0(f,c) 
                elif border==2:
                    livingNeigbor=self.Border0(f,c) + self.Toroide(f,c)
                    
                if (self.Matriz[f][c]==1):
                    # Si la celula esta viva  
                    if (livingNeigbor==2 or livingNeigbor==3 ):
                        # se mantiene viva
                        self.MatrizAux[f][c]=1
                        self._StatusCellsLive=self._StatusCellsLive+1
                    else:
                        # muere
                        self.MatrizAux[f][c]=0
                else:
                    # si la celula esta muerta
                    if (livingNeigbor==3):
                        # revive
                        self.MatrizAux[f][c]=1
                        self._StatusCellsLive=self._StatusCellsLive+1
                    else:
                        # seguira muerta
                        self.MatrizAux[f][c]=0
                        
            
        # Cambio de estado del automata 
        self.Matriz=self.MatrizAux
        
        if bandera_toggle:
            self.CellsSide=self.Matriz.shape[0]
            
                
    
    def Border0(self,f:int,c:int)->int:
        # con el siguiente caso aseguramos estabilidad dentro de la frontera (Cerrada)
        # (frontera) (ṕosicion de la celda respecto al centro de la vecindad)
       
        # celula y sus vecindades
        #    +---+---+---+
        #    | 1 | 2 | 3 |
        #    +---+---+---+
        #    | 4 |   | 5 |
        #    +---+---+---+
        #    | 6 | 7 | 8 |
        #    +---+---+---+   
        # Contador de vecinos vivios
        livingNeigbor=0         
        
        # // 1
        if ((f>0 and c>0) and (self.Matriz[f-1][c-1])):
            livingNeigbor=livingNeigbor+1
        
        
        # // 2
        if ((c>0) and (self.Matriz[f][c-1])):
            livingNeigbor=livingNeigbor+1
        
        # // 3
        if ((f<self.CellsSide-1 and c>0) and (self.Matriz[f+1][c-1])):
            livingNeigbor=livingNeigbor+1
        
        # // 4
        if ((f>0) and (self.Matriz[f-1][c])):
            livingNeigbor=livingNeigbor+1
        
        # // 5
        if ((f<self.CellsSide-1) and (self.Matriz[f+1][c])):
            livingNeigbor=livingNeigbor+1
        
        # // 6
        if ((f>0 and c<self.CellsSide-1) and (self.Matriz[f-1][c+1])):
            livingNeigbor=livingNeigbor+1
        
        # // 7
        if ((c<self.CellsSide-1) and (self.Matriz[f][c+1])):
            livingNeigbor=livingNeigbor+1
        
        # // 8
        if ((f<self.CellsSide-1 and c<self.CellsSide-1) and (self.Matriz[f+1][c+1])):
            livingNeigbor=livingNeigbor+1
        return livingNeigbor
    
    def Toroide(self,f:int,c:int)->int:
        # Forma toroidal de la matriz
        livingNeigbor=0   
        M=self.CellsSide-1
        
        # matriz[0,0]:  1=[M,M],    2=[M,c],    3=[M,c+1],  4=[f,M],    6=[f+1,M]      5
        if (f==0 and c==0):
            if (self.Matriz[M][M]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[M][c]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[M][c+1]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f][M]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f+1][M]):
                livingNeigbor=livingNeigbor+1
            return livingNeigbor
            
        # matriz[f,0]:  1=[f-1,M],                          4=[f,M],    6=[f+1,M]      
        if ( 0<f and f<M and c==0):
            if (self.Matriz[f-1][M]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f][M]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f+1][M]):
                livingNeigbor=livingNeigbor+1
            return livingNeigbor
        
        # matriz[0,c]:  1=[M,c-1],  2=[M,c],    3=[M,c+1]
        if (f==0 and 0<c and c<M):
            if (self.Matriz[M][c-1]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[M][c]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[M][c+1]):
                livingNeigbor=livingNeigbor+1
            return livingNeigbor
        
        # matriz[M,M]:  8=[0,0],    3=[f-1,0],  5=[f,0],    6=[0,c-1],  7=[0,c]         5
        if (f==M and c==M):
            if (self.Matriz[0][0]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f-1][0]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f][0]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[0][c-1]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[0][c]):
                livingNeigbor=livingNeigbor+1
            return livingNeigbor
        
        # matriz[M,c]:  8=[0,c+1],                          6=[0,c-1],  7=[0,c]         
        if (f==M and 0<c and c<M):
            if (self.Matriz[0][c+1]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[0][c-1]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[0][c]):
                livingNeigbor=livingNeigbor+1
            return livingNeigbor
        
        # matriz[f,M]:  8=[f+1,0],  3=[f-1,0],  5=[f,0]
        if (0<f and f<M and c==M):
            if (self.Matriz[f+1][0]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f-1][0]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f][0]):
                livingNeigbor=livingNeigbor+1
            return livingNeigbor
        
        # matriz[M,0]:  6=[0,M],    8=[0,c+1],  1=[f-1,M],  4=[M,M],    7=[0,0]         5
        if (f==M and c==0):
            if (self.Matriz[0][M]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[0][c+1]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f-1][M]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[M][M]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[0][0]):
                livingNeigbor=livingNeigbor+1
            return livingNeigbor
        
        # matriz[0,M]:  3=[M,0],    1=[M,c-1],  2=[M,M],    5=[0,0],    8=[f+1,0]       5
        if (f==0 and c==M):
            if (self.Matriz[M][0]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[M][c-1]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[M][M]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[0][0]):
                livingNeigbor=livingNeigbor+1
            if (self.Matriz[f+1][0]):
                livingNeigbor=livingNeigbor+1
            return livingNeigbor
        return 0
    
    def initialRandom(self,cells_side:int=None):
        if cells_side!=None:
            self.CellsSide=cells_side
        self._StatusCellsLive=0
        self.Matriz=np.random.randint(2,size=(self.CellsSide,self.CellsSide))
        # self._MatrizAux=np.zeros((self.CellsSide,self.CellsSide),dtype=int)
    
    def initialZeros(self,cells_side:int=None):
        if cells_side!=None:
            self.CellsSide=cells_side
        self._StatusCellsLive=0
        self.Matriz=np.zeros((self.CellsSide,self.CellsSide),dtype=int)
        # self._MatrizAux=np.zeros((self.CellsSide,self.CellsSide),dtype=int)
    
    def __str__(self) -> str:
        return self.Matriz.__str__()+"\n"