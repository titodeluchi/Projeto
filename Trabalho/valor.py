class Valores:
    @property
    def id (self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id
    
    @property
    def valores_trans_id(self):
        return self.__valor_trans_id
    @valores_trans_id.setter
    def cpf(self,valor_trans_id):
        self.__valor_trans_id = valor_trans_id

    @property
    def valores(self):
        return self.__valor
    @valores.setter
    def valores(self,valor):
        self.__valor = valor    
