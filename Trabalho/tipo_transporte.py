class Transporte:
    def __init__(self):
        self.__id= 0
        self.__pessoa_id=0
        self.__tipo=''

    @property
    def id (self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id


    @property
    def pessoa_id (self):
        return self.__pessoa_id
    @pessoa_id.setter
    def pessoa_id(self,pessoa_id):
        self.__pessoa_id = pessoa_id


    @property
    def tipo (self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo        
