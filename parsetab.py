
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND BOOLEAN COMA CORCHETE_A CORCHETE_C DISTINTOQUE DIVISION ELSE FALSE FLOAT FOR FUNCTION ID IF IGUAL IGUALQUE LLAVE_A LLAVE_C MASIGUAL MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MODULO MULTIPLICACION NOT NUMBER OR PARENTESIS_A PARENTESIS_C PRINT PUNTO REMOVE RESTA STRING SUMA TO TRUE WHILEinit : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion : print_statement\n| while_statement\n| if_statement\n| if_else_statement\n| assign_statement\n| for_statement\n| declare_function\n| call_functionprint_statement : PRINT PARENTESIS_A expression PARENTESIS_Cfor_statement : FOR PARENTESIS_A ID IGUAL expression TO expression PARENTESIS_C LLAVE_A instrucciones LLAVE_Cwhile_statement : WHILE PARENTESIS_A expression PARENTESIS_C LLAVE_A instrucciones LLAVE_Cif_statement : IF PARENTESIS_A expression PARENTESIS_C LLAVE_A instrucciones LLAVE_Cif_else_statement : IF PARENTESIS_A expression PARENTESIS_C LLAVE_A instrucciones LLAVE_C ELSE LLAVE_A instrucciones LLAVE_Cassign_statement : ID IGUAL expressiondeclare_function : FUNCTION ID PARENTESIS_A parametros PARENTESIS_C LLAVE_A instrucciones LLAVE_Cparametros : ID \n| ID COMA parametros\n| emptycall_function : ID PARENTESIS_A argumentos PARENTESIS_Cargumentos : expression\n| expression COMA argumentosexpression : NUMBER\n| STRING\n| BOOLEAN\n| binary_op\n| variable\n| logical_opelementos : expression\n| elementos COMA expressionvariable : IDassign_statement : ID IGUAL CORCHETE_A elementos CORCHETE_Cexpression : ID CORCHETE_A expression CORCHETE_Cexpression : ID PUNTO ADD PARENTESIS_A expression PARENTESIS_Cexpression : ID PUNTO REMOVE PARENTESIS_A expression PARENTESIS_Cbinary_op : expression SUMA expression\n| expression RESTA expression\n| expression MULTIPLICACION expression\n| expression DIVISION expression\n| expression MENORQUE expression\n| expression MAYORQUE expression\n| expression IGUALQUE expression\n| expression MODULO expressionlogical_op : expression AND expression\n| expression OR expression\n| NOT expressioninstruccion : ID MASIGUALempty :'
    
_lr_action_items = {'ID':([0,2,3,4,5,6,7,8,9,10,11,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,43,44,46,47,48,49,50,51,52,53,54,55,58,59,60,61,64,71,72,73,74,75,76,77,78,79,80,81,82,84,85,87,89,90,91,93,94,95,97,100,101,103,104,105,108,109,110,111,112,113,114,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-11,26,-2,-49,27,27,27,27,27,42,-33,-17,27,-25,-26,-27,-28,-29,-30,27,65,27,27,27,27,27,27,27,27,27,27,27,-48,-22,27,-12,27,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-34,27,12,12,65,-35,27,27,12,12,27,12,-14,-15,12,-36,-37,-18,12,12,12,12,-16,-13,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,18,19,27,28,30,31,32,33,34,35,58,59,61,71,72,73,74,75,76,77,78,79,80,81,84,85,89,93,94,97,100,101,103,104,105,108,109,110,111,112,113,114,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-49,-33,-17,-25,-26,-27,-28,-29,-30,-48,-22,-12,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-34,13,13,-35,13,13,13,-14,-15,13,-36,-37,-18,13,13,13,13,-16,-13,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,18,19,27,28,30,31,32,33,34,35,58,59,61,71,72,73,74,75,76,77,78,79,80,81,84,85,89,93,94,97,100,101,103,104,105,108,109,110,111,112,113,114,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-49,-33,-17,-25,-26,-27,-28,-29,-30,-48,-22,-12,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-34,14,14,-35,14,14,14,-14,-15,14,-36,-37,-18,14,14,14,14,-16,-13,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,18,19,27,28,30,31,32,33,34,35,58,59,61,71,72,73,74,75,76,77,78,79,80,81,84,85,89,93,94,97,100,101,103,104,105,108,109,110,111,112,113,114,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-49,-33,-17,-25,-26,-27,-28,-29,-30,-48,-22,-12,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-34,15,15,-35,15,15,15,-14,-15,15,-36,-37,-18,15,15,15,15,-16,-13,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,18,19,27,28,30,31,32,33,34,35,58,59,61,71,72,73,74,75,76,77,78,79,80,81,84,85,89,93,94,97,100,101,103,104,105,108,109,110,111,112,113,114,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-49,-33,-17,-25,-26,-27,-28,-29,-30,-48,-22,-12,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-34,16,16,-35,16,16,16,-14,-15,16,-36,-37,-18,16,16,16,16,-16,-13,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,11,18,19,27,28,30,31,32,33,34,35,58,59,61,71,72,73,74,75,76,77,78,79,80,81,84,85,89,93,94,97,100,101,103,104,105,108,109,110,111,112,113,114,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-49,-33,-17,-25,-26,-27,-28,-29,-30,-48,-22,-12,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-34,17,17,-35,17,17,17,-14,-15,17,-36,-37,-18,17,17,17,17,-16,-13,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,18,19,27,28,30,31,32,33,34,35,58,59,61,71,72,73,74,75,76,77,78,79,80,81,89,100,101,104,105,108,113,114,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-49,-33,-17,-25,-26,-27,-28,-29,-30,-48,-22,-12,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-34,-35,-14,-15,-36,-37,-18,-16,-13,]),'LLAVE_C':([3,4,5,6,7,8,9,10,11,18,19,27,28,30,31,32,33,34,35,58,59,61,71,72,73,74,75,76,77,78,79,80,81,89,93,94,100,101,103,104,105,108,111,112,113,114,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-49,-33,-17,-25,-26,-27,-28,-29,-30,-48,-22,-12,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-34,-35,100,101,-14,-15,108,-36,-37,-18,113,114,-16,-13,]),'MASIGUAL':([12,],[19,]),'IGUAL':([12,42,],[20,64,]),'PARENTESIS_A':([12,13,14,15,16,26,69,70,],[21,22,23,24,25,43,90,91,]),'CORCHETE_A':([20,27,],[29,44,]),'NUMBER':([20,21,22,23,24,29,36,44,46,47,48,49,50,51,52,53,54,55,60,64,82,90,91,95,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'STRING':([20,21,22,23,24,29,36,44,46,47,48,49,50,51,52,53,54,55,60,64,82,90,91,95,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'BOOLEAN':([20,21,22,23,24,29,36,44,46,47,48,49,50,51,52,53,54,55,60,64,82,90,91,95,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'NOT':([20,21,22,23,24,29,36,44,46,47,48,49,50,51,52,53,54,55,60,64,82,90,91,95,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'PUNTO':([27,],[45,]),'SUMA':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,46,-25,-26,-27,-28,-29,-30,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-35,46,46,46,46,-36,-37,]),'RESTA':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,47,-25,-26,-27,-28,-29,-30,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-35,47,47,47,47,-36,-37,]),'MULTIPLICACION':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,48,-25,-26,-27,-28,-29,-30,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-35,48,48,48,48,-36,-37,]),'DIVISION':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,49,-25,-26,-27,-28,-29,-30,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-35,49,49,49,49,-36,-37,]),'MENORQUE':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,50,-25,-26,-27,-28,-29,-30,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-35,50,50,50,50,-36,-37,]),'MAYORQUE':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,51,-25,-26,-27,-28,-29,-30,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-35,51,51,51,51,-36,-37,]),'IGUALQUE':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,52,-25,-26,-27,-28,-29,-30,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-35,52,52,52,52,-36,-37,]),'MODULO':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,53,-25,-26,-27,-28,-29,-30,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-35,53,53,53,53,-36,-37,]),'AND':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,54,-25,-26,-27,-28,-29,-30,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-35,54,54,54,54,-36,-37,]),'OR':([27,28,30,31,32,33,34,35,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,86,89,92,98,99,102,104,105,],[-33,55,-25,-26,-27,-28,-29,-30,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-35,55,55,55,55,-36,-37,]),'COMA':([27,30,31,32,33,34,35,38,56,57,58,65,71,72,73,74,75,76,77,78,79,80,89,92,104,105,],[-33,-25,-26,-27,-28,-29,-30,60,82,-31,-48,87,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-35,-32,-36,-37,]),'PARENTESIS_C':([27,30,31,32,33,34,35,37,38,39,40,41,43,58,65,66,67,71,72,73,74,75,76,77,78,79,80,83,87,89,96,98,99,102,104,105,],[-33,-25,-26,-27,-28,-29,-30,59,-23,61,62,63,-50,-48,-19,88,-21,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-24,-50,-35,-20,104,105,107,-36,-37,]),'CORCHETE_C':([27,30,31,32,33,34,35,56,57,58,68,71,72,73,74,75,76,77,78,79,80,89,92,104,105,],[-33,-25,-26,-27,-28,-29,-30,81,-31,-48,89,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-35,-32,-36,-37,]),'TO':([27,30,31,32,33,34,35,58,71,72,73,74,75,76,77,78,79,80,86,89,104,105,],[-33,-25,-26,-27,-28,-29,-30,-48,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,95,-35,-36,-37,]),'ADD':([45,],[69,]),'REMOVE':([45,],[70,]),'LLAVE_A':([62,63,88,106,107,],[84,85,97,109,110,]),'ELSE':([101,],[106,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,84,85,97,109,110,],[2,93,94,103,111,112,]),'instruccion':([0,2,84,85,93,94,97,103,109,110,111,112,],[3,18,3,3,18,18,3,18,3,3,18,18,]),'print_statement':([0,2,84,85,93,94,97,103,109,110,111,112,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'while_statement':([0,2,84,85,93,94,97,103,109,110,111,112,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'if_statement':([0,2,84,85,93,94,97,103,109,110,111,112,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'if_else_statement':([0,2,84,85,93,94,97,103,109,110,111,112,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'assign_statement':([0,2,84,85,93,94,97,103,109,110,111,112,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'for_statement':([0,2,84,85,93,94,97,103,109,110,111,112,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'declare_function':([0,2,84,85,93,94,97,103,109,110,111,112,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'call_function':([0,2,84,85,93,94,97,103,109,110,111,112,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'expression':([20,21,22,23,24,29,36,44,46,47,48,49,50,51,52,53,54,55,60,64,82,90,91,95,],[28,38,39,40,41,57,58,68,71,72,73,74,75,76,77,78,79,80,38,86,92,98,99,102,]),'binary_op':([20,21,22,23,24,29,36,44,46,47,48,49,50,51,52,53,54,55,60,64,82,90,91,95,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'variable':([20,21,22,23,24,29,36,44,46,47,48,49,50,51,52,53,54,55,60,64,82,90,91,95,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'logical_op':([20,21,22,23,24,29,36,44,46,47,48,49,50,51,52,53,54,55,60,64,82,90,91,95,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'argumentos':([21,60,],[37,83,]),'elementos':([29,],[56,]),'parametros':([43,87,],[66,96,]),'empty':([43,87,],[67,67,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','lexer_parser.py',85),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','lexer_parser.py',89),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','lexer_parser.py',94),
  ('instruccion -> print_statement','instruccion',1,'p_instruccion','lexer_parser.py',98),
  ('instruccion -> while_statement','instruccion',1,'p_instruccion','lexer_parser.py',99),
  ('instruccion -> if_statement','instruccion',1,'p_instruccion','lexer_parser.py',100),
  ('instruccion -> if_else_statement','instruccion',1,'p_instruccion','lexer_parser.py',101),
  ('instruccion -> assign_statement','instruccion',1,'p_instruccion','lexer_parser.py',102),
  ('instruccion -> for_statement','instruccion',1,'p_instruccion','lexer_parser.py',103),
  ('instruccion -> declare_function','instruccion',1,'p_instruccion','lexer_parser.py',104),
  ('instruccion -> call_function','instruccion',1,'p_instruccion','lexer_parser.py',105),
  ('print_statement -> PRINT PARENTESIS_A expression PARENTESIS_C','print_statement',4,'p_print_statement','lexer_parser.py',109),
  ('for_statement -> FOR PARENTESIS_A ID IGUAL expression TO expression PARENTESIS_C LLAVE_A instrucciones LLAVE_C','for_statement',11,'p_for_statement','lexer_parser.py',113),
  ('while_statement -> WHILE PARENTESIS_A expression PARENTESIS_C LLAVE_A instrucciones LLAVE_C','while_statement',7,'p_while_statement','lexer_parser.py',117),
  ('if_statement -> IF PARENTESIS_A expression PARENTESIS_C LLAVE_A instrucciones LLAVE_C','if_statement',7,'p_if_statement','lexer_parser.py',121),
  ('if_else_statement -> IF PARENTESIS_A expression PARENTESIS_C LLAVE_A instrucciones LLAVE_C ELSE LLAVE_A instrucciones LLAVE_C','if_else_statement',11,'p_if_else_statement','lexer_parser.py',125),
  ('assign_statement -> ID IGUAL expression','assign_statement',3,'p_assign_statement','lexer_parser.py',129),
  ('declare_function -> FUNCTION ID PARENTESIS_A parametros PARENTESIS_C LLAVE_A instrucciones LLAVE_C','declare_function',8,'p_declarar_funciones','lexer_parser.py',134),
  ('parametros -> ID','parametros',1,'p_parametros','lexer_parser.py',138),
  ('parametros -> ID COMA parametros','parametros',3,'p_parametros','lexer_parser.py',139),
  ('parametros -> empty','parametros',1,'p_parametros','lexer_parser.py',140),
  ('call_function -> ID PARENTESIS_A argumentos PARENTESIS_C','call_function',4,'p_llamar_funcion','lexer_parser.py',147),
  ('argumentos -> expression','argumentos',1,'p_argumentos','lexer_parser.py',151),
  ('argumentos -> expression COMA argumentos','argumentos',3,'p_argumentos','lexer_parser.py',152),
  ('expression -> NUMBER','expression',1,'p_expression','lexer_parser.py',159),
  ('expression -> STRING','expression',1,'p_expression','lexer_parser.py',160),
  ('expression -> BOOLEAN','expression',1,'p_expression','lexer_parser.py',161),
  ('expression -> binary_op','expression',1,'p_expression','lexer_parser.py',162),
  ('expression -> variable','expression',1,'p_expression','lexer_parser.py',163),
  ('expression -> logical_op','expression',1,'p_expression','lexer_parser.py',164),
  ('elementos -> expression','elementos',1,'p_elementos','lexer_parser.py',168),
  ('elementos -> elementos COMA expression','elementos',3,'p_elementos','lexer_parser.py',169),
  ('variable -> ID','variable',1,'p_variable','lexer_parser.py',176),
  ('assign_statement -> ID IGUAL CORCHETE_A elementos CORCHETE_C','assign_statement',5,'p_crearLista','lexer_parser.py',180),
  ('expression -> ID CORCHETE_A expression CORCHETE_C','expression',4,'p_obtenerIndexLista','lexer_parser.py',185),
  ('expression -> ID PUNTO ADD PARENTESIS_A expression PARENTESIS_C','expression',6,'p_agregarLista','lexer_parser.py',192),
  ('expression -> ID PUNTO REMOVE PARENTESIS_A expression PARENTESIS_C','expression',6,'p_eliminarLista','lexer_parser.py',201),
  ('binary_op -> expression SUMA expression','binary_op',3,'p_binary_op','lexer_parser.py',212),
  ('binary_op -> expression RESTA expression','binary_op',3,'p_binary_op','lexer_parser.py',213),
  ('binary_op -> expression MULTIPLICACION expression','binary_op',3,'p_binary_op','lexer_parser.py',214),
  ('binary_op -> expression DIVISION expression','binary_op',3,'p_binary_op','lexer_parser.py',215),
  ('binary_op -> expression MENORQUE expression','binary_op',3,'p_binary_op','lexer_parser.py',216),
  ('binary_op -> expression MAYORQUE expression','binary_op',3,'p_binary_op','lexer_parser.py',217),
  ('binary_op -> expression IGUALQUE expression','binary_op',3,'p_binary_op','lexer_parser.py',218),
  ('binary_op -> expression MODULO expression','binary_op',3,'p_binary_op','lexer_parser.py',219),
  ('logical_op -> expression AND expression','logical_op',3,'p_logical_op','lexer_parser.py',223),
  ('logical_op -> expression OR expression','logical_op',3,'p_logical_op','lexer_parser.py',224),
  ('logical_op -> NOT expression','logical_op',2,'p_logical_op','lexer_parser.py',225),
  ('instruccion -> ID MASIGUAL','instruccion',2,'p_incremento_statement','lexer_parser.py',232),
  ('empty -> <empty>','empty',0,'p_empty','lexer_parser.py',236),
]
