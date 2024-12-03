from ply import lex
from ply import yacc
from expresiones import *
from instruccion import *
from environment import *


tokens=[
    'NUMBER','STRING','BOOLEAN','ID','SUMA','RESTA','MULTIPLICACION','DIVISION','AND','OR','NOT','IGUAL','PARENTESIS_A','PARENTESIS_C','LLAVE_A','LLAVE_C','MAYORQUE','MENORQUE'
    ,'IGUALQUE','MAYORIGUAL','MENORIGUAL','DISTINTOQUE','FLOAT',"MASIGUAL",'MODULO','CORCHETE_A', 'CORCHETE_C','COMA','PUNTO'
]
reserved={
    'print':'PRINT',
    'while' :'WHILE',
    'if':'IF',
    'else':'ELSE',
    'true':'TRUE',
    'false':'FALSE',
    'for': 'FOR',
    'to':'TO',
    'funcion': 'FUNCTION',
    'add': 'ADD',
    'remove' :'REMOVE'
}
tokens+=list(reserved.values())

t_SUMA=r'\+'
t_RESTA=r'\-'
t_MULTIPLICACION=r'\*'
t_DIVISION=r'\/'
t_AND=r'\&{2}'
t_OR=r'\|{2}'
t_NOT=r'\!'
t_IGUAL=r'\='
t_PARENTESIS_A=r'\('
t_PARENTESIS_C=r'\)'
t_LLAVE_A=r'\{'
t_LLAVE_C=r'\}'
t_MAYORQUE=r'\>'
t_MENORQUE=r'\<'
t_IGUALQUE=r'\={2}'
t_MAYORIGUAL=r'\>='
t_MENORIGUAL=r'\<='
t_DISTINTOQUE=r'\!='
t_MASIGUAL=r'\+{2}'
t_MODULO=r'\%'
t_CORCHETE_A=r'\['
t_CORCHETE_C=r'\]'
t_COMA=r'\,'
t_PUNTO=r'\.'
t_ignore = " \t"
def t_NUMBER(t):
    r'\d+'
    t.value=int(t.value)
    return t
def t_STRING(t):
    r'"[^"]*"'
    t.value = str(t.value.strip('"'))
    return t
def t_BOOLEAN(t):
    r'true|false'
    t.value = bool(t.value == 'true')
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type=reserved.get(t.value.lower(),'ID')
    return t
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value=float(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")  # Incrementa el número de líneas
    return None
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer=lex.lex()
##################################PARSER#################################################################
def p_init(p):
    'init : instrucciones'
    p[0]=p[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(p):
    '''instruccion : print_statement
                 | while_statement
                 | if_statement
                 | if_else_statement
                 | assign_statement
                 | for_statement
                 | declare_function
                 | call_function'''
    p[0] = p[1]

def p_print_statement(p):
    'print_statement : PRINT PARENTESIS_A expression PARENTESIS_C'
    p[0] = Imprimir(p[3])

def p_for_statement(p):
    'for_statement : FOR PARENTESIS_A ID IGUAL expression TO expression PARENTESIS_C LLAVE_A instrucciones LLAVE_C'
    p[0] = For(p[3], p[5], p[7], p[10])

def p_while_statement(p):
    'while_statement : WHILE PARENTESIS_A expression PARENTESIS_C LLAVE_A instrucciones LLAVE_C'
    p[0] = While(p[3], p[6])

def p_if_statement(p):
    'if_statement : IF PARENTESIS_A expression PARENTESIS_C LLAVE_A instrucciones LLAVE_C'
    p[0] = If(p[3], p[6])

def p_if_else_statement(p):
    'if_else_statement : IF PARENTESIS_A expression PARENTESIS_C LLAVE_A instrucciones LLAVE_C ELSE LLAVE_A instrucciones LLAVE_C'
    p[0] = IfElse(p[3], p[6], p[10])

def p_assign_statement(p):
    'assign_statement : ID IGUAL expression'
    p[0] = valorVariable(p[1],p[3])
    

def p_declarar_funciones(p):
    'declare_function : FUNCTION ID PARENTESIS_A parametros PARENTESIS_C LLAVE_A instrucciones LLAVE_C'
    p[0]=defineFuncion(p[2],p[4],p[7])

def p_parametros(p):
    '''parametros : ID 
                  | ID COMA parametros
                  | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = [p[1]] + p[3]    

def p_llamar_funcion(p):
    'call_function : ID PARENTESIS_A argumentos PARENTESIS_C'
    p[0]=callFuncion(p[1],p[3])

def p_argumentos(p):
    '''argumentos : expression
                  | expression COMA argumentos'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = [p[1]] + p[3]

def p_expression(p):
    '''expression : NUMBER
                  | STRING
                  | BOOLEAN
                  | binary_op
                  | variable
                  | logical_op'''
    p[0] = p[1]

def p_elementos(p):
    '''elementos : expression
                 | elementos COMA expression'''
    if len(p)==2:
        p[0]=[p[1]] if p[1] is not None else[]
    else: 
        p[0]=p[1]+[p[3]]

def p_variable(p):
    'variable : ID'
    p[0] = Variable(p[1])
########################################LISTAS######################################
def p_crearLista(p):
    'assign_statement : ID IGUAL CORCHETE_A elementos CORCHETE_C'
    p[0]=Lista(p[1],p[4])
    env.declarar(p[1],p[0])

def p_obtenerIndexLista(p):
    'expression : ID CORCHETE_A expression CORCHETE_C'
    lista_var=env.obtener(p[1])
    index = p[3]
    if isinstance(lista_var,list) and 0<= index < len(lista_var):
        p[0]=lista_var[index]

def p_agregarLista(p):
    'expression : ID PUNTO ADD PARENTESIS_A expression PARENTESIS_C'
    lista_var=env.obtener(p[1])
    nuevo = p[5]
    if isinstance(lista_var, Lista):  
        nuevo = p[5]  
        lista_var.agregar(nuevo,env)  
        p[0] = lista_var  

def p_eliminarLista(p):
    'expression : ID PUNTO REMOVE PARENTESIS_A expression PARENTESIS_C'
    lista_var=env.obtener(p[1])
    removed = p[5]
    if isinstance(lista_var, Lista):  
        removed = p[5]  
        lista_var.eliminar(removed,env)  
        p[0] = lista_var 
    

####################OPERACIONES BINARIAS ############################################
def p_binary_op(p):
    '''binary_op : expression SUMA expression
                 | expression RESTA expression
                 | expression MULTIPLICACION expression
                 | expression DIVISION expression
                 | expression MENORQUE expression
                 | expression MAYORQUE expression
                 | expression IGUALQUE expression
                 | expression MODULO expression'''
    p[0] = operacionesBinarias(p[1], p[2], p[3])
#########################OPERACIONES LOGICAS ############################################
def p_logical_op(p):
    '''logical_op : expression AND expression
                  | expression OR expression
                  | NOT expression'''
    if len(p) == 3:
        p[0] = operacionUnitaria(p[2],p[1])
    else:
        p[0] = operacionesBinarias(p[1], p[2], p[3])
#########################FUNCION DE INCREMENTO ################################
def p_incremento_statement(p):
    'instruccion : ID MASIGUAL'
    p[0]=Incremento(p[1])

def p_empty(p):
    'empty :'
    p[0] = None
def p_error(p):
    if p:
        print(f"Syntax error at {p.value}")
    else:
        print("Syntax error at EOF")
parser=yacc.yacc()
input_data = '''
x=12
z=88
funcion pico(a,b){
xz=a+b
print(xz)
}
pico(x,z)
'''
lexer.input(input_data)

# Para ver qué tokens se reconocen
for tok in lexer:
    print(tok)
env=Environment()
# Probar el parser con una cadena de entrada
result = parser.parse(input_data)
for instruccion in result:
    instruccion.evaluate(env)
