## Donaldo Salazar
from cubosem import *
from toolfncs import *
from vmem import *
from vmach import *
import ply.yacc as yacc
import ply.lex as lex

saltos = []
tipos =[]
variables = []
operadores =[]
## virtualmem = []
lstfunc =[]
scope = 1

cint   = 10000
cfloat = 11000
cchar  = 12000
cbool  = 13000

tvint   = 6000 
tvfloat = 7000
tvchar  = 8000
tvbool  = 9000

lvint   = 3500
lvfloat = 4000
lvchar  = 4500
lvbool  = 5000

gvint   = 1000
gvfloat = 1500
gvchar  = 2000
gvbool  = 2500

ptint   = 14000
ptfloat = 15000
ptchar  = 16000
ptbool  = 17000


#############################################################
#         LÓGICA DE ASIGNACIÓN DE MEMORIA EN COMPILACIÓN

def cleanlmemory():
  global  lvint,lvfloat,lvchar,tvint,tvfloat,tvchar,cint,cfloat,cchar,cbool,tvbool,lvbool, contTemp
  tvint   = 6000 
  tvfloat = 7000
  tvchar  = 8000
  tvbool  = 9000
  lvint   = 3500
  lvfloat = 4000
  lvchar  = 4500
  lvbool  = 5000
  contTemp = 1

conta = 1

def whereme(tipo):
  global scope, gvint , gvfloat , gvchar , lvint , lvfloat , lvchar , lvbool, gvbool
  if (scope == 1):
      if (tipo == 'int'):
          ret = gvint
          gvint += 1
          print(gvint)
          return ret
      elif (tipo == 'float'):
          ret = gvfloat
          gvfloat +=1
          print(gvfloat)
          return ret
      elif (tipo == 'char'):
          ret = gvchar
          gvchar +=1
          print(gvchar)
          return ret
      elif (tipo == 'bool'):
          ret = gvbool
          gvbool +=1
          print(gvbool)
          return ret
  else:
      if (tipo == 'int'):
          ret = lvint
          lvint +=1
          print(lvint)
          return ret
      elif (tipo == 'float'):
          ret = lvfloat
          lvfloat +=1
          print(lvfloat)
          return ret
      elif (tipo == 'char'):
          ret = lvchar
          lvchar +=1
          print(lvchar)
          return ret 
      elif (tipo == 'bool'):
          ret = lvbool
          lvbool +=1
          print(lvbool)
          return ret
  print("no está definida en memoria")
  exit()





def wheremet(tipo):
  global scope, tvint , tvfloat , tvchar
  if (tipo == 'int'):
      ret = tvint
      tvint   +=1
      print(tvint)
      return ret
  elif (tipo == 'float'):
      ret = tvfloat
      tvfloat +=1
      print(tvfloat)
      return ret
  elif (tipo == 'char'):
      ret = tvchar
      tvchar  +=1
      print(tvchar)
      return ret
  elif (tipo == 'bool'):
      ret = tvbool
      tvchar  +=1
      print(tvchar)
      return ret
    
  print("no está definida en memoria")
  exit()

def wheremec(tipo):
  global cint , cfloat , cchar , cbool
  if (tipo == 'int'):
      ret = cint
      cint   +=1
      return ret
  elif (tipo == 'float'):
      ret = cfloat
      cfloat +=1
      return ret 
  elif (tipo == 'char'):
      ret = cchar
      cchar  +=1
      return ret 
  elif (tipo == 'bool'):
      ret = cbool
      cbool  +=1
      return ret 
  print("no está definida en memoria")
  exit()

def wheremep(varType):
    global  ptint , ptfloat , ptchar ,ptbool
    if(varType == 'int'):
        ret = ptint
        ptint  +=1 
        return ret 
    elif(varType == 'float'):
        ret = ptfloat
        ptfloat +=1
        return ret 
    elif(varType == 'bool'):
        ret = ptbool
        ptbool +=1
        return ret 
    elif(varType == 'char'):
        ret = ptchar
        ptchar +=1
        return ret 

########################################################
# Funciones para obtener tipo y dirección
def getType(ID):
  varLocales = list(map(lambda x: x.id ,lstfunc[scope].vars))
  varGlobales = list(map(lambda x: x.id ,lstfunc[1].vars))
  varConstant = list(map(lambda x: x.id ,lstfunc[0].vars))
  if ID in varLocales:
    idx = varLocales.index(ID)
    return lstfunc[scope].vars[idx].tipo
  elif ID in varGlobales:
    idx = varGlobales.index(ID)
    return lstfunc[1].vars[idx].tipo
  elif ID in varConstant:
    idT = varConstant.index(ID)
    return lstfunc[0].vars[idT].tipo
  print("ERROR: variable '", ID, "' no definida")
  exit()

def getDir(ID):
    varLocales = list(map(lambda x: x.id ,lstfunc[scope].vars))
    varGlobales = list(map(lambda x: x.id ,lstfunc[1].vars))
    varConstant = list(map(lambda x: x.id ,lstfunc[0].vars))
    if ID in varLocales:
      idx = varLocales.index(ID)
      return lstfunc[scope].vars[idx].dir
    elif ID in varGlobales:
      idx = varGlobales.index(ID)
      return lstfunc[1].vars[idx].dir
    elif ID in varConstant:
      idT = varConstant.index(ID)
      return lstfunc[0].vars[idT].dir
    print("ERROR: variable '", ID, "' no definida")
    exit()



########################################################################
# TOKENS Y PALABRAS RESERVADAS
tokens = [
    'PLUS','MIN','MULT','DIVIDE',
    'ID','EQUAL','GTR','LST',
    'DIFFERENT','FSTP','LSTP','FSTB','LSTB',"LESSEQUAL","GREATEQUAL",
    'CTEINT','CTEFLOAT','COMMA','SEMICOLON', 'STRING',
    'LFTBRACK', 'RGTBRACK','CTECHAR','ISEQUAL','ONEUP','OROP','ANDOP','ONEDOWN'
]
reservadas = {
    'int' : 'INT',
    'float':'FLOAT',
    'program' : 'PROG',
    'print' : 'PRINT',
    'if' : 'IFS',
    'else' : 'ELSES',
    'for' : 'FOR',
    'to' : 'TO',
    'while' : 'WHILE',
    'def' : 'DEFINEFUNC',
    'void' : 'VOID',
    'char' : 'CHAR',
    'main' : 'MAINFUNC',
    'return' : 'RETURNF',
    'mean' : 'MEANT',
    'mode' : 'MODET',
    'median' : 'MEDIANT',
    'sd' : 'SDT',
    'variance' : 'VART',
    'hist' : 'HIST',
    'rand' : "RANDOMF",
    'input' : "INPUT"
}
#Si no comenzamos con "t_" PLY se enoja
t_CTEFLOAT = r'\d+\.\d+'
t_CTEINT = r'\d+'
t_CTECHAR = r'"\[a-zA-Z_]\"'
t_PLUS = r'\+'
t_MIN = r'\-'
t_MULT = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'\='
t_DIFFERENT = r'!='
t_LESSEQUAL = r'<='
t_GREATEQUAL = r'>='
t_ISEQUAL = r'\=\='
t_OROP = r'\|'
t_ANDOP = r'\&'
t_ONEDOWN = r'\-\-'
t_ONEUP = r'\+\+'
t_GTR = r'\>'
t_LST = r'\<'
t_FSTP = r'\('
t_LSTP = r'\)'
t_FSTB = r'\{'
t_LSTB = r'\}'
t_LFTBRACK = r'\['
t_RGTBRACK = r'\]'
t_STRING = r'"([^\\"\n]+|\\.)*"'
t_COMMA = r','
t_SEMICOLON = r';'
# Si no ignoramos los espacios en blanco, el lexer se enoja
t_ignore = r' '
#####################################################################
#Con esto incluimos el diccionario de las palabras reservadas a los tokens, así podemos incluir los statements, prints, tipos, y todo eso :D

tokens = tokens + list(reservadas.values())


# Si no ignoramos los los saltos de linea, el lexer se enoja
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
# Empezamos con un caracter para que pueda ser una variable, luego puede seguir cualquier número de digitos o caracteres.
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reservadas.get(t.value,'ID')
    return t
################################################################



#def t_CTEINT(t):
#  r'\d+'
#  t.value = int(t.value)
#  return t
#def t_CTEFLOAT(t):
#  r'\d+\.\d+'
#  t.value = int(t.value)
#  return t

## tipico error handling PARA EL LEXER
def t_error(t):
    print("caracteres ilegales")
    t.lexer.skip(1)


lex.lex()

#Aquí empieza el parser
#####################################
# INICIALIZACIÓN DEL PROGRAMA
def p_programa(p):
    ''' programa : PROG ID SEMICOLON declare endprog
    '''
######################################
# DECLARACARACIONES DE FUNCIONES
def p_func(p):
        ''' func : vfunc
                  | tfunc
        '''
def p_tipo(p):
    ''' tipo : INT
             | FLOAT
             | CHAR
    '''
    p[0] = p[1]


############# void func
actfunc = ""

def p_vfunc(p):
    ''' vfunc : DEFINEFUNC VOID ID func2list FSTP vfuncaux
    '''
def p_vfuncaux(p):
    ''' vfuncaux : tipo ID var2symtab params2lst vfuncaux2 
                 | vfuncaux2 
    '''
def p_vfuncaux2(p):
    ''' vfuncaux2 : LSTP bloque ENDFunc
                    | COMMA tipo ID var2symtab params2lst vfuncaux2 
    '''


############## type func


def p_tfunc(p):
    ''' tfunc : DEFINEFUNC tipo ID func2list FSTP tfuncaux
    '''
def p_tfuncaux(p):
    ''' tfuncaux : tipo ID var2symtab params2lst tfuncaux2 
                 | tfuncaux2 
    '''
def p_tfuncaux2(p):
    ''' tfuncaux2 : LSTP fbloque ENDFunc
                    | COMMA tipo ID var2symtab params2lst tfuncaux2 
    '''
################################################
### DECLARACIONES DE VARIABLES, ARRAYS, Y SUS CUADRUPLOS
#Creo que dos auxiliares a var son necesarias para los diferentes tipos de output. intenté ponerlo en una cfg por si sola y así fue como lo ví, con var


def p_var(p):
    ''' var : tipo ID var2symtab  varsauxaux
            | tipo ID LFTBRACK CTEINT arr2symtab RGTBRACK SEMICOLON
    '''


def p_varsauxaux(p):
    ''' varsauxaux :  COMMA var
                   |  COMMA LFTBRACK superexpresion RGTBRACK varsauxaux
                   |  SEMICOLON 
    '''



def p_var2symtab(p):
    ''' var2symtab :
    '''
    ID = p[-1]
    localVars = list(map(lambda x: x.id ,lstfunc[scope].vars))
    globalVars = list(map(lambda x: x.id ,lstfunc[1].vars))
    if ID in localVars or ID in globalVars:
      print("Variable ya definida '%s'" % ID)
      exit()
    else:
      lstfunc[scope].vars.append(variable(p[-1],p[-2],whereme(p[-2]),None))
    
def p_arr2symtab(p):
    ''' arr2symtab :
    '''
    ID = p[-3]
    localVars = list(map(lambda x: x.id ,lstfunc[scope].vars))
    globalVars = list(map(lambda x: x.id ,lstfunc[1].vars))
    if ID in localVars or ID in globalVars:
      print("Variable ya definida '%s'" % ID)
      exit()
    else:
      tempDir = whereme(p[-4])
      lstfunc[0].vars.append(variable(p[-1], "int", wheremec("int"),None))
      lstfunc[scope].vars.append(variable(p[-3], p[-4], tempDir,p[-1]))
      for i in range(0,int(p[-1])):
        ID = p[-3] + '[' + str(i) + ']'
        tempDir = whereme(p[-4])
        lstfunc[scope].vars.append(variable(ID, p[-4], tempDir,p[-2]))
#########################################################
#### DECLARACIONES DEL ESQUELETO DEL PROGRAMA
def p_declare(p):
    ''' declare : func declare
                    | var declare
                    | main
    '''



###########################
## CUADRUPLO DE FINALIZACIÓN
def p_endprog(p):
    'endprog : '
    cuadruplos.append(cuadruplo(len(cuadruplos), "EndProg",None, None , None))

###############################################
## DECLARACIÓN DE LA FUNCIÓN MAIN

def p_main(p):
        ''' main : MAINFUNC gotomain bloque

        '''
def p_gotomain(p):
  'gotomain :'
  cuadruplos[0].res = len(cuadruplos)
  global scope 
  lstfunc.append(funcion('main','int',len(cuadruplos)))
  scope = len(lstfunc)-1


####################################
## BLOQUES PARA FUNCIONES, ESTATUTOS LÓGICOS Y MAIN.
## HAY UN BLOQUE ESPECIAL PARA FUNCIONES, EL CUAL INCLUYE "RETURN"

def p_bloque(p):
    ''' bloque : FSTB estatutoaux LSTB
               | FSTB LSTB
    '''
def p_fbloque(p):
    ''' fbloque : FSTB fbloqueaux

    '''
def p_fbloqueaux(p):
    ''' fbloqueaux : returnfunc fbloqueaux
                   | estatuto fbloqueaux
                   | LSTB
    '''
#####################################################
# ESTATUTOS POSIBLES DENTRO DE LOS BLOQUES
def p_estatuto(p):
    ''' estatuto : asignacion
                 | ifstat
                 | escritura
                 | lectura
                 | llamada SEMICOLON
                 | whileloop
                 | forloop
                 | var
                 | counters
                 | histf
                 

    '''
#Hice un estatuto Auxiliar porque necesitaba encontrar una manera de que pudiera haber un loop en bloque sin meter un bracket izquierda
def p_estatutoaux(p):
    ''' estatutoaux : estatuto
                    | estatutoaux estatuto
    '''

########################################################################
#### DECLARACION DE ASIGNACIÓN Y SUS CUADRUPLOS PARA VARIABLE NORMAL Y ARRAY


#A la asignación de agregué que podría igualarse entre otras variables, se me hizo raro que no se pudiera
def p_asignacion(p):
    ''' asignacion : ID ID2LST EQUAL OP2LST superexpresion CuadruploAsignacion SEMICOLON
                   | ID LFTBRACK ID RGTBRACK  EQUAL OP2LST superexpresion CuadruploAsignacionArr SEMICOLON

    '''

def p_CuadruploAsignacion(p):
  'CuadruploAsignacion : '
  ID = p[-5]
  long = len(operadores)- 1 - ''.join(operadores).rfind("(")
  if long > 0:
    if operadores[len(operadores)-1] == '=' :
      tmp1 = variables.pop()
      tipo1 = getType(tmp1)
      tipo2 = getType(ID)
      operador = operadores.pop()
      sintaxis = CuboSemRes(operador,tipo1, tipo2)
      if sintaxis == 'error':
        print("Error de semantica en ", ID)
        exit()
      cuadruplos.append(cuadruplo(len(cuadruplos), operador,getDir(tmp1), None , getDir(ID)))
      variables.pop()

def p_CuadruploAsignacionArr(p):
  'CuadruploAsignacionArr : '
  ID = p[-7]
  if len(operadores)> 0:
    if operadores[len(operadores)-1] == '=' :
      tmp1 = variables.pop()
      variable1 = getDir(tmp1) 
      tipo1 = getType(tmp1)
      tipo2 = getType(ID)
      operador = operadores.pop()
      sintaxis = CuboSemRes(operador,tipo1, tipo2)
      if sintaxis == "error": 
        exit()
      cuadruplos.append(cuadruplo(len(cuadruplos), 'Ver' ,getDir("0"),getDir(getDim(p[-7].split('[')[0])), getDir(p[-5])))  
      global contTemp
      varTemp= "t" + str(contTemp)
      variables.append(varTemp)
      contTemp = contTemp + 1
      tempDir = wheremep("int")
      point = wheremec("int")
      lstfunc[0].vars.append(variable(getDir(p[-7]),"int",point,None))
      lstfunc[scope].vars.append(variable(varTemp, 'int', tempDir,None))
      cuadruplos.append(cuadruplo(len(cuadruplos), 'ARR' ,point, getDir(p[-5]) ,getDir(varTemp)))
      cuadruplos.append(cuadruplo(len(cuadruplos), '=',variable1, None ,  getDir(varTemp)))
      variables.pop()



#####################################################################
########### DECLARACIÓN DE ESTATUTOS LÓGICOS CONDICIONALES



def p_ifstat(p):
    '''ifstat : IFS FSTP superexpresion LSTP Cuadgotofx fbloque updateJump ifstatx


    '''
def p_ifstatx(p):
    '''ifstatx : CuadEndIfstat ELSES fbloque updateJump
                | 

    '''

############## SECCION DE GOTO ##############
def p_go2lst(p) :
  'go2lst : '
  saltos.append(len(cuadruplos))
##################### CICLOS ########################

def p_whileloop(p):
    ''' whileloop : WHILE FSTP go2lst superexpresion LSTP Cuadgotofx bloque CuadEndLoop
    '''

def p_forloop(p):
    ''' forloop : FOR FSTP ID LSTP TO FSTP cte LSTP go2lst CuadgotofFLoop  bloque CuadEndForLoop
    '''

def p_CuadEndLoop(p):
  'CuadEndLoop : '
  global tempSaltos
  tempSaltos = saltos.pop()
  cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTO', None, None ,saltos.pop()))
  cuadruplos[tempSaltos].res = len(cuadruplos)
  
def p_CuadEndForLoop(p):
  'CuadEndForLoop : '
  global tempSaltos
  tempSaltos = saltos.pop()
  cuadruplos.append(cuadruplo(len(cuadruplos), '++', None, None ,getDir(p[-9]) ))
  cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTO', None, None ,saltos.pop()))
  cuadruplos[tempSaltos].res = len(cuadruplos)
##################### Condicionales #####################
saltos = []
tempSaltos = 0


def p_CuadgotofFLoop(p):
  'CuadgotofFLoop : '
  global tempSaltos
  if len(variables) > 0:
    saltos.append(len(cuadruplos))
    contfl = variables.pop()
    global contTemp
    varTemp= "t" + str(contTemp)
    variables.append(varTemp)
    contTemp = contTemp + 1
    tempDir = wheremep("bool")
    lstfunc[scope].vars.append(variable(varTemp, 'bool', tempDir,None))
    cuadruplos.append(cuadruplo(len(cuadruplos), '>', getDir(contfl), getDir(p[-7]) ,tempDir ))
    cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTOF', tempDir, None ,None ))

def p_Cuadgotof(p):
  'Cuadgotof : '
  global tempSaltos
  if len(variables) > 0:
    saltos.append(len(cuadruplos))
    cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTOF', getDir(variables.pop()), None ,None ))

def p_Cuadgotofx(p):
  'Cuadgotofx : '
  print("it me")
  global tempSaltos
  if len(variables) > 0:
    saltos.append(len(cuadruplos))
    cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTOF', getDir(variables.pop()), None ,None ))



def p_CuadEndIfstat(p):
  'CuadEndIfstat : '
  cuadruplos.append(cuadruplo(len(cuadruplos), 'GOTO', None, None ,None))
  saltos.append(len(cuadruplos)-1)
  cuadruplos[saltos.pop()].res = len(cuadruplos)


def p_updateJump(p):
  'updateJump :'
  cuadruplos[saltos.pop()].res = len(cuadruplos)
  
#############################################
###########################################
####### LECTURA Y ESCRITURA
def p_escritura(p):
    ''' escritura : PRINT FSTP prints LSTP SEMICOLON

    '''
def p_prints(p):
    ''' prints : superexpresion CuadruploPRINT
                        | superexpresion CuadruploPRINT COMMA prints
                        | cte CuadruploPRINT
                        | cte CuadruploPRINT COMMA prints

    '''
def p_CuadruploPRINT(p):
  'CuadruploPRINT : '
  gonnaprint = getDir(variables.pop());
  cuadruplos.append(cuadruplo(len(cuadruplos), "PRINT", None, None ,gonnaprint ))

def p_lectura(p):
    ''' lectura : INPUT FSTP ID reading LSTP SEMICOLON

    '''
def p_reading(p):
    ''' reading :

    '''
    ID = p[-1]
    localVars = list(map(lambda x: x.id ,lstfunc[scope].vars))
    globalVars = list(map(lambda x: x.id ,lstfunc[1].vars))
    if ID in localVars or ID in globalVars:
      cuadruplos.append(cuadruplo(len(cuadruplos),"READ", None ,None, getDir(ID)))
      
    else:
      print("Variable no definida '%s'" % ID)
      exit()
#necesitamos de este prints para seguir concatenando

#########################################################################


## Cosas para la symtable

def p_func2list(p):
  'func2list :'
  global scope
  if p[-2] != "void":
    lstfunc.append(funcion(p[-1],p[-2],len(cuadruplos)))
    vmem = whereme(p[-2])
    lstfunc[1].vars.append(variable(p[-1], p[-2], vmem,None))
    scope = len(lstfunc)-1
  else:
    lstfunc.append(funcion(p[-1],p[-2],len(cuadruplos)))
    lstfunc[1].vars.append(variable(p[-1], p[-2], "void",None))
    scope = len(lstfunc)-1


#########################################################################

############################ 
###    Funciones especiales 

def p_specialfunc(p):
    ''' specialfunc : meanf
                    | modef
                    | medianf
                    | sdf
                    | variancef 
                    | randf       
    '''
### mean
def p_meanf(p):
    ''' meanf : MEANT FSTP ID LSTP meancuad         
    '''

def p_meancuad(p):
    'meancuad : '
    if  isinstance(int(getDim(p[-2])), int) and (getType(p[-2]) == 'int' or getType(p[-2]) == 'float' ):
      newvar = "t" + str(contTemp)
      tipaje = wheremet('float')
      lstfunc[scope].vars.append(variable( newvar, 'float',tipaje,None))
      cuadruplos.append(cuadruplo(len(cuadruplos),"MEAN", getDir(p[-2]) ,int(getDim(p[-2])), getDir(newvar)))
      variables.append(newvar)
    else: 
      print("variable no es un array de enteros o flotantes")
      exit()
#### Mode
def p_modef(p):
    ''' modef : MODET FSTP ID LSTP modecuad        
    '''
def p_modecuad(p):
    'modecuad : '
    if  isinstance(int(getDim(p[-2])), int) and (getType(p[-2]) == 'int' or getType(p[-2]) == 'float' ):
      newvar = "t" + str(contTemp)
      tipaje = wheremet('float')
      lstfunc[scope].vars.append(variable( newvar, 'float',tipaje,None))
      cuadruplos.append(cuadruplo(len(cuadruplos),"MODE", getDir(p[-2]) ,int(getDim(p[-2])), getDir(newvar)))
      variables.append(newvar)
    else: 
      print("variable no es un array de enteros o flotantes")
      exit()
############ median
def p_medianf(p):
    ''' medianf : MEDIANT FSTP ID LSTP mediancuad         
    '''
def p_mediancuad(p):
    'mediancuad : '
    if  isinstance(int(getDim(p[-2])), int) and (getType(p[-2]) == 'int' or getType(p[-2]) == 'float' ):
      newvar = "t" + str(contTemp)
      tipaje = wheremet('float')
      lstfunc[scope].vars.append(variable( newvar, 'float',tipaje,None))
      cuadruplos.append(cuadruplo(len(cuadruplos),"MEDIAN", getDir(p[-2]) ,int(getDim(p[-2])), getDir(newvar)))
      variables.append(newvar)
    else: 
      print("variable no es un array de enteros o flotantes")
      exit()
### sdf
def p_sdf(p):
    ''' sdf : SDT FSTP ID LSTP sdfcuad       
    '''
def p_sdfcuad(p):
    'sdfcuad : '
    if  isinstance(int(getDim(p[-2])), int) and (getType(p[-2]) == 'int' or getType(p[-2]) == 'float' ):
      newvar = "t" + str(contTemp)
      tipaje = wheremet('float')
      lstfunc[scope].vars.append(variable( newvar, 'float',tipaje,None))
      cuadruplos.append(cuadruplo(len(cuadruplos),"SDF", getDir(p[-2]) ,int(getDim(p[-2])), getDir(newvar)))
      variables.append(newvar)
    else: 
      print("variable no es un array de enteros o flotantes")
      exit()

def p_variancef(p):
    ''' variancef : VART FSTP ID LSTP variancecuad        
    '''
def p_variancecuad(p):
    'variancecuad : '
    if  isinstance(int(getDim(p[-2])), int) and (getType(p[-2]) == 'int' or getType(p[-2]) == 'float' ):
      newvar = "t" + str(contTemp)
      tipaje = wheremet('float')
      lstfunc[scope].vars.append(variable( newvar, 'float',tipaje,None))
      cuadruplos.append(cuadruplo(len(cuadruplos),"VARIANCE", getDir(p[-2]) ,int(getDim(p[-2])), getDir(newvar)))
      variables.append(newvar)
    else: 
      print("variable no es un array de enteros o flotantes")
      exit()

def p_histf(p):
    ''' histf : HIST FSTP ID LSTP histcuad SEMICOLON       
    '''
def p_histcuad(p):
    'histcuad : '
    if  isinstance(int(getDim(p[-2])), int) and (getType(p[-2]) == 'int' or getType(p[-2]) == 'float' ):
      cuadruplos.append(cuadruplo(len(cuadruplos),"HIST", getDir(p[-2]) ,int(getDim(p[-2])),None ))
    else: 
      print("variable no es un array de enteros o flotantes")
      exit()

def p_randf(p):
    ''' randf : RANDOMF FSTP CTEINT COMMA CTEINT LSTP randcuad        
    '''
def p_randcuad(p):
    'randcuad : '
    print(p[-2])
    if  isinstance(int(p[-2]), int) and isinstance(int(p[-4]), int):
      global contTemp
      newvar = "t" + str(contTemp)
      contTemp +=1
      tipaje = wheremet('int')
      lstfunc[scope].vars.append(variable( newvar, 'int',tipaje,None))
      cuadruplos.append(cuadruplo(len(cuadruplos),"RAND", int(p[-4]) ,int(p[-2]), getDir(newvar)))
      variables.append(newvar)
    else: 
      print("Los parametros solo aceptan ENTEROS")
      exit()



################################################################
### CONTADORES
def p_counters(p):
    ''' counters : ID ONEUP cuadcount SEMICOLON
                  | ID ONEDOWN cuadcount SEMICOLON
    '''

def p_cuadcount(p):
    ''' cuadcount :
    '''
    if getType(p[-2]) == 'int' or  getType(p[-2]) == 'float':
      cuadruplos.append(cuadruplo(len(cuadruplos),p[-1],None,None,getDir(p[-2]) ))
    else:
      print("no puedes usar contadores en variables no numericas")
      exit()
###############################################################
################# EXPRESIONES
def p_superexpresion(p):
    ''' superexpresion : expresion
                | expresion ANDOP OP2LST superexpresion CuadruploAndOr
                | expresion OROP OP2LST superexpresion CuadruploAndOr
                | counters
    '''
def p_expresion(p):
    ''' expresion : exp
                | exp GTR OP2LST exp CuadruploBools
                | exp LST OP2LST exp CuadruploBools
                | exp DIFFERENT OP2LST exp CuadruploBools
                | exp ISEQUAL OP2LST exp CuadruploBools
                | exp LESSEQUAL OP2LST exp CuadruploBools
                | exp GREATEQUAL OP2LST exp CuadruploBools
                
    '''


def p_exp(p):
    ''' exp : termino CuadruploSumaResta
            | termino CuadruploSumaResta expaux
            | ID counters SEMICOLON
    '''

def p_expaux(p):
    '''expaux :  PLUS OP2LST exp
              |  MIN OP2LST exp
    '''

def p_termino(p):
    ''' termino : factor CuadruploMultDiv
            | factor CuadruploMultDiv terminoaux
    '''

def p_terminoaux(p):
    ''' terminoaux : MULT OP2LST termino
                | DIVIDE OP2LST termino
    '''

def p_factor(p):
    ''' factor : FSTP PAR2LST superexpresion LSTP PARPOP
               | CuadruploSumaResta  PLUS OP2LST cte
               | CuadruploSumaResta  MIN OP2LST cte
               | cte
    '''
def p_cte(p):
    ''' cte : ID ID2LST
            | CTEFLOAT FLT2LST
            | CTEINT INT2LST
            | CTECHAR
            | STRING
            | llamada
            | ID LFTBRACK ID RGTBRACK  ARR2LST
            | specialfunc
    '''
    
##########################################################################
#### 

#####################
##### LÓGICA DE RETURN Y PARAMETROS

def p_returnfunc(p):
    ''' returnfunc : RETURNF FSTP returnfuncaux
    '''
def p_returnfuncaux(p):
    ''' returnfuncaux : superexpresion cuadReturn LSTP SEMICOLON
               | STRING cuadReturn LSTB SEMICOLON
    '''
def p_llamada(p):
    ''' llamada : ID era FSTP llamadaaux
    '''
def p_llamadaaux(p):
    ''' llamadaaux : superexpresion sendParam llamadaaux
                  | COMMA superexpresion sendParam llamadaaux
                  | LSTP gosub
    '''
numParam = 1

def p_params2lst(p):
    ''' params2lst :
    '''
    lstfunc[scope].plist.append(p[-3])


def p_sendParam(p):
  'sendParam : '
  global numParam
  if numParam-1 < len(lstfunc[indx].plist):
    actparam = variables.pop()
    if getType(actparam) == lstfunc[indx].plist[numParam-1]:
      varTemp = "p" + str(numParam)
      cuadruplos.append(cuadruplo(len(cuadruplos), "Params",getDir(actparam), None , varTemp))
      numParam += 1
    else: 
      print("LOS TIPOS DE VARIABLES NO SON LOS MISMOS QUE LOS PARAMETROS")
      exit()
  else:
      print("numero incorrecto de variables")
      exit()


def p_ENDFunc(p):
  'ENDFunc : '
  global contTemp, scope
  contTemp = 1
  cuadruplos.append(cuadruplo(len(cuadruplos), "ENDFunc", None, None, None)) 
  scope = 1
  cleanlmemory()

def p_cuadReturn(p):
    "cuadReturn : "
    vc = getDir(variables.pop())
    cuadruplos.append(cuadruplo(len(cuadruplos), "RETURN", None, None, vc))
    cuadruplos.append(cuadruplo(len(cuadruplos), "ENDFunc", None, None, None)) 
    
indx = 0
def p_gosub(p):
    'gosub : '
    funcs = list(map(lambda x: x.id ,lstfunc))
    global indx, numParam, contTemp
    indx = funcs.index(actfunc)
    cuadruplos.append(cuadruplo (len(cuadruplos), "gosub",actfunc, lstfunc[indx].dir , None))
    if numParam-1 == len(lstfunc[indx].plist):
      numParam=1
    else: 
      print("numero incorrecto de variables")
      exit()
    if lstfunc[indx].tipo != "void":
      actVars= list(map(lambda x: x.id ,lstfunc[1].vars))
      actDir = actVars.index(actfunc)
      mydir = getDir(actfunc)
      newvar = "t" + str(contTemp)
      tipaje = wheremet(lstfunc[indx].tipo)
      lstfunc[scope].vars.append(variable( newvar, lstfunc[indx].tipo,tipaje,None))
      cuadruplos.append(cuadruplo(len(cuadruplos),"=", lstfunc[1].vars[actDir].dir ,None, getDir(newvar)))
      variables.append(newvar)
      contTemp += 1
def p_era(p):
    ''' era : 
    '''
    global actfunc
    actfunc = p[-1]
    funcs = list(map(lambda x: x.id ,lstfunc))
    actVars= list(map(lambda x: x.id ,lstfunc[1].vars))
    actDir = actVars.index(p[-1])
    #tempDirccion = lstfunc[indx].vars[actDir].dir
    if actfunc in funcs:
      print(funcs.index(actfunc))
      global indx
      indx = funcs.index(actfunc)
      cuadruplos.append(cuadruplo(len(cuadruplos), "ERA",actfunc, lstfunc[1].vars[actDir].dir , None))
    else: 
      print("Funcion", actfunc, "no definida") 
      exit()

#Error handling para el parser
error_list = []

def p_error(p):
    global valido
    valido = False
    print(p)
    print("Error de sintaxis en '%s'" % p.value)
    exit()
################### Funciones auxiliares para meter las cosas a sus respectivos stacksssssssssss (listas)


def p_SZ2LST(p):
  'SZ2LST :'
  lstfunc[0].vars.append(variable(p[-1], 'int', wheremec('int'),None))

holder = 0
def p_INT2LST(p):
  'INT2LST :'
  global holder
  variables.append(p[-1])
  lstfunc[0].vars.append(variable(p[-1], 'int', wheremec('int'),None))
  p[0] = p[-1]
  holder = p[-1]

def p_CHAR2LST(p):
  'CHAR2LST :'
  global holder
  variables.append(p[-1])
  lstfunc[0].vars.append(variable(p[-1], 'int', wheremec('char'),None))
  p[0] = p[-1]
  holder = p[-1]


def p_FLT2LST(p):
  'FLT2LST :'
  variables.append(p[-1])
  lstfunc[0].vars.append(variable(p[-1], 'float',wheremec('float'),None))

def p_ID2LST(p):
	"ID2LST :"
	variables.append(p[-1])

def p_OP2LST(p):
	"OP2LST :"
	operadores.append(p[-1])

def p_PAR2LST(p):
	"PAR2LST :"
	operadores.append(p[-1])

def p_PARPOP(p):
	"PARPOP :"
	operadores.pop(''.join(operadores).rfind("("))

def p_ARR2LST(p):
  "ARR2LST : "
  cuadruplos.append(cuadruplo(len(cuadruplos), 'Ver' ,getDir("0"),getDir(getDim(p[-4].split('[')[0])),getDir(p[-2]) ))
  global contTemp
  varTemp= "t" + str(contTemp)
  contTemp+=1
  #operador = operadores.pop()
  tempDir = wheremep('int')
  point = wheremec("int")
  lstfunc[0].vars.append(variable(getDir(p[-4]),"int",point,None))
  lstfunc[scope].vars.append(variable(varTemp, 'int', tempDir,None))
  cuadruplos.append(cuadruplo(len(cuadruplos), 'ARR' ,point, getDir(p[-2]) ,getDir(varTemp)))
  variables.append(varTemp)
  contTemp +=1


#Cuadrulos
################# DIRECTORIO DE FUNCIONES
lstfunc = [funcion('const',None,0),funcion('globales',None,0)]
################ DIRECTORIO DE CUADRUPLOS
cuadruplos = [cuadruplo(0,"GOTO","MAIN",None,None)]
################ LISTAS PARA LLEVAR LAS VARIABLES Y OPERADORES

variables =  []
operadores = []
############# ESTA ME AYUDA A TRAER LAS VARIABLES TEMPORALES
contTemp = 1

######################## AQUI VAN LAS CONSTANTES
lstfunc[0].vars.append(variable("0",'int', wheremec("int"),None))




##########################################################
### CUADRUPLOS PARA OPERACIONES ARITMETICAS Y BOOLEANAS


def p_CuadruploMultDiv(p):
  'CuadruploMultDiv :'
  long = len(operadores)- 1 - ''.join(operadores).rfind("(")
  if long > 0:
    global contTemp
    if operadores[len(operadores)-1] == '*' or operadores[len(operadores)-1] == '/' :
      operador = operadores.pop()
      varTemp= "t" + str(contTemp)
      tmp = variables.pop()
      derecho = getDir(tmp)
      rvartype = getType(tmp)
      
      tmp = variables.pop()
      izquierda = getDir(tmp)
      tipolvartype = getType(tmp)
      tipores = CuboSemRes(operador,tipolvartype, rvartype)
      if tipores == 'error':
        print(p)
        print("Error de semantica en '%s'" % p.value)
        exit()
      tmpdir = wheremet(tipores)
      lstfunc[scope].vars.append(variable(varTemp, tipores, tmpdir,None))
      cuadruplos.append(cuadruplo(len(cuadruplos), operador, izquierda, derecho, tmpdir))
      variables.append(varTemp)
      contTemp = contTemp + 1

def p_CuadruploSumaResta(p):
  'CuadruploSumaResta :'
  tipores = CuboSemRes("+", "int", "int")


  long = len(operadores)- 1 - ''.join(operadores).rfind("(")
  if long > 0:
    global contTemp
    if operadores[len(operadores)-1] == '+' or operadores[len(operadores)-1] == '-' :
      operador = operadores.pop()
      varTemp= "t" + str(contTemp)
      tmp = variables.pop()
      derecho = getDir(tmp)
      rvartype = getType(tmp)
      tmp = variables.pop()
      izquierda = getDir(tmp)
      tipolvartype = getType(tmp)
      tipores = CuboSemRes(operador,tipolvartype, rvartype)
      if tipores == 'error':
        print("Error de semantica")
        exit()
      tmpdir = wheremet(tipores)
      lstfunc[scope].vars.append(variable(varTemp, tipores, tmpdir,None))
      cuadruplos.append(cuadruplo(len(cuadruplos), operador, izquierda, derecho, tmpdir))
      variables.append(varTemp)
      contTemp = contTemp + 1


def p_CuadruploBools(p):
  'CuadruploBools :'
  long = len(operadores)- 1 - ''.join(operadores).rfind("(")
  if long > 0:
    global contTemp
    if operadores[len(operadores)-1] == '<' or operadores[len(operadores)-1] == '>' or operadores[len(operadores)-1] == '!=' or operadores[len(operadores)-1] == '==' or operadores[len(operadores)-1] == '>=' or operadores[len(operadores)-1] == '<=' :
      operador = operadores.pop()
      varTemp= "t" + str(contTemp)
      tmp = variables.pop()
      derecho = getDir(tmp)
      rvartype = getType(tmp)
      tmp = variables.pop()
      izquierda = getDir(tmp)
      tipolvartype = getType(tmp)
      tipores = CuboSemRes(operador,tipolvartype, rvartype)
      if tipores == 'error':
        raise ValueError("Error de sintaxis en comparaciones")
      tmpdir = wheremet(tipores)
      print()
      lstfunc[scope].vars.append(variable(varTemp, tipores, tmpdir,None))
      cuadruplos.append(cuadruplo(len(cuadruplos), operador, izquierda, derecho, tmpdir))
      variables.append(varTemp)
      contTemp = contTemp + 1

def p_CuadruploAndOr(p):
  'CuadruploAndOr : '
  long = len(operadores)- 1 - ''.join(operadores).rfind("(")
  if long > 0:
    global contTemp
    if operadores[len(operadores)-1] == '|' or operadores[len(operadores)-1] == '&' :
      operador = operadores.pop()
      varTemp= "t" + str(contTemp)
      tmp = variables.pop()
      derecho = getDir(tmp)
      rvartype = getType(tmp)
      tmp = variables.pop()
      izquierda = getDir(tmp)
      tipolvartype = getType(tmp)
      tipores = CuboSemRes(operador,tipolvartype, rvartype)
      if tipores == 'error':
        raise ValueError("Error de sintaxis en comparaciones")
      tmpdir = wheremet(tipores)
      lstfunc[scope].vars.append(variable(varTemp, tipores, tmpdir,None))
      cuadruplos.append(cuadruplo(len(cuadruplos), operador, izquierda, derecho , tmpdir))
      variables.append(varTemp)
      contTemp = contTemp + 1
###########################################################
#Aquí formamos el parser

yacc.yacc()
 

def getDim(ID):
    varLocales = list(map(lambda x: x.id ,lstfunc[scope].vars))
    varGlobales = list(map(lambda x: x.id ,lstfunc[1].vars))
    varConstant = list(map(lambda x: x.id ,lstfunc[0].vars))
    if ID in varLocales:
      idx = varLocales.index(ID)
      return lstfunc[scope].vars[idx].arrsize
    elif ID in varGlobales:
      idx = varGlobales.index(ID)
      return lstfunc[1].vars[idx].arrsize
    elif ID in varConstant:
      idT = varConstant.index(ID)
      return lstfunc[0].vars[idT].arrsize
    return "None"
    exit()



def getID(ID):
    varLocales = list(map(lambda x: x.dir ,lstfunc[scope].vars))
    varGlobales = list(map(lambda x: x.dir ,lstfunc[1].vars))
    varConstant = list(map(lambda x: x.dir ,lstfunc[0].vars))
    if ID in varLocales:
      idx = varLocales.index(ID)
      return lstfunc[scope].vars[idx].id
    elif ID in varGlobales:
      idx = varGlobales.index(ID)
      return lstfunc[1].vars[idx].id
    elif ID in varConstant:
      idT = varConstant.index(ID)
      return lstfunc[0].vars[idT].id
    return "None"
    exit()



try:
    namef = "p1.txt"
    file = open(namef,'r')
    test = file.read()
    file.close()
except EOFError:
    quit()
yacc.parse(test)
print("Success!")
print("\n")
print("\n")
print("-----------------------------------------------------")
print("\n")
## print(list(map(lambda x: x.id ,lstfunc[scope].vars)))
print("\n")
for index in range(len(cuadruplos)-1):
   print( cuadruplos[index].ident, " ",cuadruplos[index].estatuto, " ",cuadruplos[index].var1, " ",cuadruplos[index].var2, " ", cuadruplos[index].res)
print("\n")
#  print(list(map(lambda x: x.id ,lstfunc[2].vars)))
## print(lstfunc[2].plist)
print(variables)
print(operadores)
print("\n")
print("------------------------------------------------------------------------")
print(saltos)
print("CONSTANTES")
print(list(map(lambda x: x.id ,lstfunc[0].vars)))
print("GLOBALES")
print(list(map(lambda x: x.id ,lstfunc[1].vars)))
print("LOCALES")
print(list(map(lambda x: x.id ,lstfunc[2].vars)))
#print(list(map(lambda x: x.id ,lstfunc[3].vars)))
print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("tempDircciones de variables por scope")
print("CONSTANTES")
print(list(map(lambda x: x.dir ,lstfunc[0].vars)))
print("GLOBALES")
print(list(map(lambda x: x.dir ,lstfunc[1].vars)))
print("LOCALES")
print(list(map(lambda x: x.dir ,lstfunc[2].vars)))
#print(list(map(lambda x: x.dir ,lstfunc[3].vars)))
print("------------------------------------------------------------------------")
print("\n")
print("\n")
for index in range(len(cuadruplos)):
   print( cuadruplos[index].ident, " ",cuadruplos[index].estatuto, " ",getID(cuadruplos[index].var1), " ",getID(cuadruplos[index].var2), " ", getID(cuadruplos[index].res))

vmem = vmem()
print("------------------------------------------------------------------------")
print("\n")
print("\n")
vmach = vmach(lstfunc,cuadruplos)

vmach.Exe(0,"EndProg")
#vmem.colocarValores(lstfunc[0])
#vmem.colocarValores(lstfunc[1])
#vmem.colocarValores(lstfunc[scope])
print("\n")
#vmem.printvm()

print("\n")
