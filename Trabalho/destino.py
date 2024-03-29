class Destino:
    def __init__(self):
        self.__id= 0
        self.__destino_trans_id=0
        self.__inicial=''
        self.__final=''

    @property
    def id (self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id
    
    @property
    def destino_trans_id(self):
        return self.__destino_trans_id
    @destino_trans_id.setter
    def destino_trans_id(self,destino_trans_id):
        self.__destino_trans_id = destino_trans_id

    @property
    def inicial(self):
        return self.__inicial
    @inicial.setter
    def inicial(self,inicial):
        self.__inicial = inicial    


    @property
    def final(self):
        return self.__final
    @final.setter
    def final(self,final):
        self.__final = final            