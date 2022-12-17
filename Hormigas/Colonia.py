import numpy as np
from Hormiga import Hormiga
from constantes import *
class Colonia:
    
    def __init__(self,cells_side:int) -> None:
        # Definiendo el espacio que contendra la colonia en celdas
        self.ColoniaMatrix=np.zeros((cells_side,cells_side))
        self.Hormigas=list()
    
    def initialState(self):
        ant=Hormiga(self.RED,(5,5))
        self.Hormigas.append(ant)

    def evaluate(self):
        
        pass
    
    def __str__(self) -> str:
        return self.ColoniaMatrix.__str__()+"\n"
    
    
ch=Colonia(20)
ch.initialState()
print(ch)