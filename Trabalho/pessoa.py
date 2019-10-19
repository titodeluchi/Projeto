class Pessoa:
    def __init__(self):
        self.__id= 0
        self.__cpf=''
        self.__nome=''

    @property
    def id (self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id
    


    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf



    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome    