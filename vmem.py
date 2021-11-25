from toolfncs import *


###############################################################
################## 
# esta clase sirve para guardar las variables en base a su tipo

class memVal():
    def __init__(self,BaseIntMem,BaseFloatMem,BaseBoolMem,BaseCharMem):
        self.intHolder = []
        self.boolHolder = []
        self.charHolder = []
        self.floatHolder = []
        self.BaseIntMem = BaseIntMem
        self.BaseFloatMem = BaseFloatMem
        self.BaseBoolMem = BaseBoolMem
        self.BaseCharMem = BaseCharMem

    def printme(self):
      print("-MEMORIA ENTEROS")
      print(self.intHolder)
      print("-MEMORIA FLOTANTES")
      print(self.floatHolder)
      print("-MEMORIA BOOLEANOS")
      print(self.boolHolder)
      print("-MEMORIA CHARS")
      print(self.charHolder)
################################################
### Obtiene el valor que hay dentor de una dirección.
### se usa la variable base y la variable que se le mandó como parametro
### se resta la base con el parametro y se obtiene la casilla con el valor
    def getValue(self,dir):
    #    print(dir,self.BaseIntMem,self.BaseIntMem)
        if dir < self.BaseFloatMem:
            return self.intHolder[dir-self.BaseIntMem]
        elif dir < self.BaseBoolMem:
           # print(dir, self.BaseFloatMem+1)
            return self.floatHolder[dir-self.BaseFloatMem]
        elif dir < self.BaseCharMem:
            return self.boolHolder[dir-self.BaseBoolMem-1]
        else: return self.charHolder[dir-self.BaseCharMem]
################# Devuelve el tipo en base a su valor
    def getType(self,dir):
        if dir < self.BaseFloatMem :
            return 'int'
        elif dir < self.BaseBoolMem:
            return 'float'
        elif dir < self.BaseCharMem:
            return 'bool'
        else:
            return 'rad'

#############################
###### Actualiza el valor de la casilla
###### de la misma manera en que se obtiene el valor
    def updateValue(self,value,dir):
       # print(dir,self.BaseIntMem,value)
        if dir < self.BaseFloatMem:
            if len(self.intHolder) > dir-self.BaseIntMem:
                self.intHolder[dir-self.BaseIntMem] = int(value)
            else:
                self.intHolder.append(int(value))
        elif dir < self.BaseBoolMem:
            if len(self.floatHolder) > dir-self.BaseFloatMem:
                self.floatHolder[dir-self.BaseFloatMem] = float(value)
            else:
                self.floatHolder.append(float(value))
        elif dir < self.BaseCharMem:
            if len(self.boolHolder) > dir-self.BaseBoolMem:
                self.boolHolder[dir-self.BaseBoolMem] = value
            else:
                self.boolHolder.append(value)
        else:
            if len(self.charHolder) > dir-self.BaseCharMem:
                self.charHolder[dir-self.BaseCharMem] = value
            else:
                self.charHolder.append(value)

##############################################################
#### esta clase sirve para guardar las variables en base a su scope
#### hay un objeto por memoria
class vmem():
    def __init__(self):
        self.gVMem = memVal(1000, 1500, 2000, 2500)
        self.lVMem = memVal(3500, 4000, 4500, 5000)
        self.tVMem = memVal(6000, 7000, 8000, 9000)
        self.cVMem = memVal(10000, 11000, 12000, 13000)
        self.pVMem = memVal(14000, 15000, 16000, 17000)

    def getValue(self,dir):
        if dir < 3500:
            return self.gVMem.getValue(dir)
        elif dir < 6000:
            return self.lVMem.getValue(dir)
        elif dir < 10000:
            return self.tVMem.getValue(dir)
        elif dir < 14000:
            return self.cVMem.getValue(dir)
        elif dir < 18000:
            return self.pVMem.getValue(dir)
######################################
#### actualiza los valores de la memoria. UpdateValue recibe la dirección donde se 
#### va a actualizar y el valor con el que se va a actualizar
    def updateValue(self,value,dir):
        if dir < 3500:
            self.gVMem.updateValue(value,dir)
        elif dir < 6000:
            self.lVMem.updateValue(value,dir)
        elif dir < 10000:
            self.tVMem.updateValue(value,dir)
        elif dir < 14000:
            self.cVMem.updateValue(value,dir)
        elif dir < 18000:
            self.pVMem.updateValue(value,dir)


#########################################################################
###### Obtiene el tipo de la dirección. Se manda a llamar los valores de memoria
    def getType(self,dir):
        if dir < 3500:
           return self.gVMem.getType(dir)
        elif dir < 6000:
           return self.lVMem.getType(dir)
        elif dir < 10000:
           return self.tVMem.getType(dir)
        elif dir < 14000:
           return self.cVMem.getType(dir)
        elif dir < 18000:
           return self.pVMem.getType(dir)


####################### ##########
#### aqui alojamos a las variables :D recibe una función y aloja sus variables en memoria
    def initVar(self,funcion):
        if funcion.id != 'const':
            for i in range(0, len(funcion.vars)):
              if funcion.vars[i].dir != "void":
                self.updateValue(999999999, funcion.vars[i].dir)
              else: pass
        else:
            for i in range(0, len(funcion.vars)):
              self.updateValue((funcion.vars[i].id), funcion.vars[i].dir)


 
    def printvm(self):
      print("*MEMORIA GLOBAL")
      print(self.gVMem.printme())
      print("*MEMORIA LOCAL")
      print(self.lVMem.printme())
      print("*MEMORIA CONSTANTES")
      print(self.cVMem.printme())
      print("*MEMORIA TEMPORALES")
      print(self.tVMem.printme())
      print("------------")
