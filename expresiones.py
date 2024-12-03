class expresion:
    def evaluate(self,env):
        pass
    'expresiones (variables(string, bool, float e int), operaciones logicas y aritmeticas.)'
class operacionesBinarias(expresion):
    def __init__(self,op1,operator,op2):
        self.op1=op1
        self.op2=op2
        self.operator=operator
    def evaluate(self, env):
        op1_valor = self._evaluate_operand(self.op1, env)
        op2_valor = self._evaluate_operand(self.op2, env)
        if self.operator=='+':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor+op2_valor
            elif isinstance(op1_valor,str)and isinstance(op2_valor,str):
                return op1_valor+op2_valor
        elif self.operator=='-':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor-op2_valor
        elif self.operator=='/':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor/op2_valor
        elif self.operator=='*':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor*op2_valor
        elif self.operator=='==':
            return op1_valor==op2_valor
        elif self.operator=='>':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor>op2_valor
        elif self.operator=='<':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor<op2_valor
        elif self.operator=='>=':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor>=op2_valor
        elif self.operator=='<=':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor<=op2_valor
        elif self.operator=='||':
            if isinstance(op1_valor,bool)and isinstance(op2_valor,bool):
                return op1_valor or op2_valor
        elif self.operator=='&&':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor and op2_valor
        elif self.operator=='%':
            if isinstance(op1_valor,(int,float))and isinstance(op2_valor,(int,float)):
                return op1_valor % op2_valor
    def _evaluate_operand(self, operand, env):
        if isinstance(operand, expresion):
            return operand.evaluate(env)
        else:
            return operand 
        
class operacionUnitaria(expresion):
    def __init__(self,operando,operator):
        self.operando=operando
        self.operator=operator
    def evaluate(self,env):
        if isinstance(self.operando, expresion):
            op1_valor = self.operando.evaluate(env)
        else:
            op1_valor = self.operando
        if self.operator=='!':
            if isinstance(op1_valor,bool):
                return not op1_valor
            else:
                raise ValueError("El operador '!' solo puede aplicarse a valores booleanos")
        else:
            raise ValueError(f"Operador desconocido: {self.operator}")
       
class Incremento(expresion):
     def __init__(self, variable):
        self.variable = variable

     def evaluate(self, env):
        valor_actual = env.obtener(self.variable)
        if not isinstance(valor_actual, (int, float)):
            raise TypeError(f"La variable {self.variable} no es un número.")
        nuevo_valor = valor_actual + 1
        env.actualizar(self.variable, nuevo_valor)

class Variable(expresion):
    def __init__(self,nombre):
        self.nombre=nombre
    def evaluate(self, env):
        return env.obtener(self.nombre)


class Lista(expresion):
    def __init__(self,nombre,variables=None):
        if variables is None:
            variables=[]
        self.nombre=nombre
        self.variables=variables
    def evaluate(self, env):
        lista_var=[]
        for var in self.variables:
            if isinstance(var,(int,bool,float,str)):
                lista_var.append(var)
        env.declarar(self.nombre,lista_var)
    def agregar(self,elemento,env):
        print("Agregar a lista")
        if isinstance(elemento, expresion):
            elemento = elemento.evaluate(env)
        self.variables.append(elemento)
        env.actualizar(self.nombre, self.variables)
    
    def obtener(self, indice):
        if 0 <= indice < len(self.variables):
            return self.variables[indice]
        else:
            raise IndexError("Índice fuera de rango")
    
    def eliminar(self, indice,env):
        if 0 <= indice < len(self.variables):
            del self.variables[indice]
            env.actualizar(self.nombre,self.variables)

        else:
            raise IndexError("Índice fuera de rango")

    def actualizar(self, indice, nuevo_valor):
        if 0 <= indice < len(self.variables):
            self.variables[indice] = nuevo_valor
        else:
            raise IndexError("Índice fuera de rango")
    
    def __str__(self):
        return f"Lista {self.nombre}: {self.variables}"