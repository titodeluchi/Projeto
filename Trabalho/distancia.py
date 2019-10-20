class Distancia:
    def __init__(self):
        self.__id= 0
        self.__distancia_trans_id=0
        self.__km=0

    @property
    def id (self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id
    
    @property
    def distancia_trans_id(self):
        return self.__distancia_trans_id
    @distancia_trans_id.setter
    def distancia_trans_id(self,distancia_trans_id):
        self.__distancia_trans_id = distancia_trans_id

    @property
    def km(self):
        return self.__km
    @km.setter
    def km(self,km):
        self.__km = km    


        