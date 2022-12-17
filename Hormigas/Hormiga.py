import numpy as np


class Hormiga:
    
    def __init__(self,id_int:int,color:str,*position) -> None:
        self.__Color=color
        self.__ID=id_int
        self.__PositionHead=position #(x:int,y:int)
        self.__Vecindad:np.ndarray()
        self.__VecindadAux:np.ndarray()
        
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
    def Color(self):
        # Documentacion de Color 
        return self.__Color
    
    @Color.setter
    def Color(self,new_Color):
        self.__Color=new_Color
    
    @Color.deleter
    def Color(self):
        del self.__Color
    #------------------------------------
    
    #------------------------------------
    @property
    def ID(self):
        # Documentacion de ID 
        return self.__ID
    
    @ID.setter
    def ID(self,new_ID):
        self.__ID=new_ID
    
    @ID.deleter
    def ID(self):
        del self.__ID
    #------------------------------------
    
    #------------------------------------
    @property
    def PositionHead(self):
        # Documentacion de PositionHead 
        return self.__PositionHead
    
    @PositionHead.setter
    def PositionHead(self,new_PositionHead):
        self.__PositionHead=new_PositionHead
    
    @PositionHead.deleter
    def PositionHead(self):
        del self.__PositionHead
    #------------------------------------
    
    #------------------------------------
    @property
    def Vecindad(self):
        # Documentacion de Vecindad 
        return self.__Vecindad
    
    @Vecindad.setter
    def Vecindad(self,new_Vecindad):
        self.__Vecindad=new_Vecindad
    
    @Vecindad.deleter
    def Vecindad(self):
        del self.__Vecindad
    #------------------------------------
    
    def nextStep(self)->tuple:
        # celula y sus vecindades
        #      0   1   2
        #    +---+---+---+
        #  0 |   | N |   |
        #    +---+---+---+
        #  1 | E |   | O |
        #    +---+---+---+
        #  2 |   | S |   |
        #    +---+---+---+
        
        
        if self.VecindadAux[1][1]==0:
            # El cuadro es blanco:
            # El cuadro se cambia a negro, se va a su Izquierda
            
            return (self.ID,"I")
        
        else :
            # El cuadro es negroo de otro color
            # El cuadro se cambia a blanco, se va a su Derecha
            return (0,"D")
        
    