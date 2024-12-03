from environment import *
from expresiones import *
class Instruccion:
    '''instruccion'''
    def evaluate(self,env):
        pass
class Imprimir(Instruccion) :
    def __init__(self,  cad) :
        self.cad = cad
    def evaluate(self, env):
        if isinstance(self.cad, (str,int,float,bool)):
            print(self.cad)
        else:
            print(self.cad.evaluate(env))
class While(Instruccion) :
    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones
    def evaluate(self,env):
        while self.expLogica.evaluate(env):
            for instruccion in self.instrucciones:
                instruccion.evaluate(env)

class valorVariable(Instruccion) :
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
    def evaluate(self, entorno):
        tipo = type(self.valor)
        if tipo == int:
            tipo_dato = TIPO_DATO.NUMERO
            entorno.declarar(self.id,self.valor)
        elif tipo == float:
            tipo_dato = TIPO_DATO.FLOAT
            entorno.declarar(self.id,self.valor)
        elif tipo == str:
            tipo_dato = TIPO_DATO.STRING
            entorno.declarar(self.id,self.valor)
        elif tipo == bool:
            tipo_dato = TIPO_DATO.BOOLEAN
            entorno.declarar(self.id,self.valor)
        elif isinstance(self.valor, operacionesBinarias):
            valor_result=self.valor.evaluate(entorno)
            entorno.declarar(self.id,valor_result)
        elif isinstance(self.valor,(list,Lista)):
            if isinstance(self.valor, Lista):
                entorno.declarar(self.id, self.valor.variables)
            else:
             entorno.declarar(self.id, self.valor)
        else:
            raise ValueError("Tipo de dato no soportado")
        
class If(Instruccion) : 
    def __init__(self,condicion, instrucciones = []) :
        self.condicion = condicion
        self.instrucciones = instrucciones
    def evaluate(self,env):
        if self.condicion.evaluate(env):
            for instruccion in self.instrucciones: 
                instruccion.evaluate(env)
class For(Instruccion):
    def __init__(self,variable,valor_inicio,valor_final, instrucciones = []):
        self.valor_inicio=valor_inicio
        self.variable=variable
        self.valor_final=valor_final
        self.instrucciones=instrucciones
    def evaluate(self,env):
        valor_inicio = self.valor_inicio.evaluate(env) if hasattr(self.valor_inicio, 'evaluate') else self.valor_inicio
        valor_final = self.valor_final.evaluate(env) if hasattr(self.valor_final, 'evaluate') else self.valor_final
        if not isinstance(valor_inicio,(int,float))or not isinstance(valor_final,(int,float)):
            raise ValueError("Valores dentro de FOR deben ser númericos")
        x=valor_inicio
        env.declarar(self.variable, x)
        if valor_inicio<valor_final:
            while x<= valor_final:
                env.actualizar(self.variable,x)
                for instruccion in self.instrucciones:
                    instruccion.evaluate(env)
                x+=1
        if valor_inicio>valor_final:
            while x>= valor_final:
                env.actualizar(self.variable,x)
                for instruccion in self.instrucciones:
                    instruccion.evaluate(env)
                x-=1

class defineFuncion(Instruccion):
    def __init__(self,nombre,parametros=[],instrucciones=[]):
        self.nombre=nombre
        self.parametros=parametros
        self.instrucciones=instrucciones
    def evaluate(self, env):
        env[self.nombre]=self



class callFuncion(Instruccion):
    def __init__(self,nombre,argumentos):
        self.nombre=nombre
        self.argumentos=argumentos
    def evaluate(self, env):
        if self.nombre not in env.variables:
            raise ValueError("La función no ha sido definida")
        funcion=env.variables[self.nombre]
        if len(funcion.parametros)!=len(self.argumentos):
            raise ValueError("La funcion espera {len(funcion.parametros)} argumentos")
        function_env=Environment()
        for funcparametro, selfarg in zip(funcion.parametros, self.argumentos):
            if hasattr(selfarg, 'evaluate'):
                value = selfarg.evaluate(function_env) 
            else:
                value = selfarg
            
            function_env.declarar(funcparametro, value)
        result=None
        for instruccion in funcion.instrucciones:
                result=instruccion.evaluate(function_env)
        return result



class IfElse(Instruccion) : 
    def __init__(self,condicion, instruccionThen = [], instruccionElse = []) :
        self.expLogica = condicion
        self.instrIfVerdadero = instruccionThen
        self.instrIfFalso = instruccionElse
    def evaluate(self,env):
        if self.expLogica.evaluate(env):
            for instruccion in self.instrIfVerdadero:
                instruccion.evaluate(env)
        else:
            for instruccion in self.instrIfFalso:
                instruccion.evaluate(env)