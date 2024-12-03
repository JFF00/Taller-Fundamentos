from enum import Enum

class TIPO_DATO(Enum) :
    NUMERO = 1
    STRING = 2
    FLOAT = 3
    BOOLEAN = 4

class Simbolo() :
    def __init__(self, id,valor) :
        self.id = id
        #self.tipo = tipo
        self.valor = valor
class Environment:
    def __init__(self,simbolos={}):
        self.variables=simbolos
    def declarar(self,name,value):
        self.variables[name]=value
    def actualizar(self,name,value):
        if name in self.variables:
            self.variables[name]=value
        else:
            raise NameError(f"Variable {name} no existe")   
    def obtener(self,name):
        if name not in self.variables:
            raise NameError(f"La variable '{name}' no existe")
        return self.variables[name]
        ##if name in self.variables:
          ##  return self.variables[name]
        ##else:
          ##  raise NameError(f"Variable{name}no existe")
    def existe(self, nombre):
        return nombre in self.variables
    def __str__(self):
        return str(self.variables)
    def __setitem__(self,key,value):
        self.variables[key]=value
    