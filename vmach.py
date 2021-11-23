import sys
from toolfncs import *
from vmem import *
import statistics as st



class vmach():
    def __init__(self, funclst, cuadruplos):
        self.funclst = funclst
        self.cuadruplos = cuadruplos
        self.parametros = []
        self.indx = 0
        self.migajita = []
        self.sleeploc = []
        self.sleeptemp = []
        self.direccionRegreso = []
        self.memoriamaster = vmem()
        for i in range(0,len(self.funclst)):
            self.memoriamaster.initVar(self.funclst[i])
        self.mem = self.memoriamaster
        self.recieveParam(self.mem)


    def operaciones(self,cuadrup,mem):
        var1 = mem.getValue(cuadrup.var1)
        var2 = mem.getValue(cuadrup.var2)
        res = cuadrup.res
        estatuto = cuadrup.estatuto
        if cuadrup.var1 >13999:
          print(cuadrup.var1)
          var1 = mem.getValue(var1)
        if cuadrup.var2 >13999:
          var2 = mem.getValue(var2)
        if estatuto == '+':
            valor = var1 + var2
        elif estatuto == '-':
            valor = var1 - var2
        elif estatuto == '*':
            valor = var1 * var2
        mem.updateValue(valor,res)

    def contadores(self,cuadrup,mem):
        var1 = mem.getValue(cuadrup.res)
        estatuto = cuadrup.estatuto
        if cuadrup.res >13999:
          var1 = mem.getValue(var1)
        if estatuto == '++':
            valor = var1 + 1
        elif estatuto == '--':
            valor = var1 - 1
        mem.updateValue(valor,cuadrup.res)
        
    def signoIgual(self,cuadrup,mem):
        #print("holaaaaa",mem.getValue(cuadrup.var1),  mem.getValue(cuadrup.res))
        if int(cuadrup.res) >= 14000:
            valor = mem.getValue(cuadrup.var1)
            dir = mem.getValue(cuadrup.res)
            mem.updateValue(valor, dir)
        elif int(cuadrup.res) < 14000:
            valor = mem.getValue(cuadrup.var1)
            mem.updateValue(valor, cuadrup.res)
        if int(cuadrup.var1) >= 14000:
            var1 = mem.getValue(cuadrup.var1)
            valor = mem.getValue(var1)
            dir = cuadrup.res
            mem.updateValue(valor, dir)

   
    def operacionesLogic(self,cuadrup,mem):
        var1 = mem.getValue(cuadrup.var1)
        var2 = mem.getValue(cuadrup.var2)
        res = cuadrup.res
        estatuto = cuadrup.estatuto
        if cuadrup.var1 >13999:
          var1 = mem.getValue(var1)
        if cuadrup.var2 >13999:
          var2 = mem.getValue(var2)
        if estatuto == '&&':
            value = var1 and var2
        elif estatuto == '||':
            value = var1 or var2
        elif estatuto == '<':
            value = var1 < var2
        elif estatuto == '<=':
            value = var1 <= var2
        elif estatuto == '>':
            value = var1 > var2
        elif estatuto == '>=':
            value = var1 >= var2
        elif estatuto == '!=':
            value = var1 != var2
        elif estatuto == '==':
            value = var1 == var2
        mem.updateValue(value, res)

    def goto(self,cuadrup):
        self.indx = cuadrup.res-1

    def gotoF(self,cuadrup,mem):
        var1 = self.mem.getValue(cuadrup.var1)
        if not var1:
            self.indx = cuadrup.res-1

    def goSub(self,cuadrup):
        x = list(map(lambda x: x.id ,self.funclst))
        indx = x.index(cuadrup.var1)
        begin = cuadrup.var2
        self.migajita.append(self.indx)
        self.sleeptemp.append(self.mem.tVMem)
        self.sleeploc.append(self.mem.lVMem)
        self.mem = vmem()
        self.mem.cVMem = self.memoriamaster.cVMem
        self.mem.gVMem = self.memoriamaster.gVMem
        self.mem.initVar(self.funclst[indx])
        self.recieveParam(self.mem)
        self.Exe(begin,'ENDFunc')
        self.mem.tVMem = self.sleeptemp.pop()
        self.mem.lVMem = self.sleeploc.pop()
        self.indx = self.migajita.pop()


    def imprime(self,cuadrup,mem):
        value = mem.getValue(cuadrup.res)
        if cuadrup.res > 13999:
          print(mem.getValue(value))
        else: 
          print(value)

    def division(self,cuadrup,mem):     
        var2 = mem.getValue(cuadrup.var2)
        if(var2 == 0):
            print('No se puede dividir entre 0')
            quit()
        else:
            var1 = mem.getValue(cuadrup.var1)
            res = cuadrup.res
            valor = var1 / var2
            mem.updateValue(valor,res)

    def era(self, cuadrup):
        self.direccionRegreso.append(cuadrup.var2)
    
    def returns(self,cuadrup,mem):
      if cuadrup.res < 13999:
        value = mem.getValue(cuadrup.res)
        dir = self.direccionRegreso.pop()
        mem.updateValue(value,dir)
      else:
        value = mem.getValue(mem.getValue(cuadrup.res))
        dir = self.direccionRegreso.pop()
        mem.updateValue(value,dir)    

    def veri(self,cuadrup,mem):
        var1 = mem.getValue(cuadrup.var1)
        var2 = mem.getValue(cuadrup.res)
        value = mem.getValue(cuadrup.var2)
        if not (var1<=var2 and value>var2):
            print('Error: index fuera de limite (out of bounce)!!!')
            exit()

    def arrProc(self,cuadrup,mem):
        temp = mem.getValue(cuadrup.var1)
        var1 = temp
        var1 = var1+1
        var2 = mem.getValue(cuadrup.var2)
        value = var1+var2
        mem.updateValue(value,cuadrup.res)



    def sendParam(self,cuadrup,mem):
        valor = mem.getValue(cuadrup.var1)
        tipo = mem.sacarType(cuadrup.var1)
        parametro = params(valor,tipo)
        self.parametros.append(parametro)

    def mean(self,cuadrup,mem):
      lst = []
      for x in range(cuadrup.var2):
        lst.append(mem.getValue(cuadrup.var1+x+1))
      value = st.mean(lst)
      mem.updateValue(value,cuadrup.res)

    def mode(self,cuadrup,mem):
      lst = []
      for x in range(cuadrup.var2):
        lst.append(mem.getValue(cuadrup.var1+x+1))
      value = st.mean(lst)
      mem.updateValue(value,cuadrup.res)
    def median(self,cuadrup,mem):
      lst = []
      for x in range(cuadrup.var2):
        lst.append(mem.getValue(cuadrup.var1+x+1))
      value = st.median(lst)
      mem.updateValue(value,cuadrup.res)

    def sd(self,cuadrup,mem):
      lst = []
      for x in range(cuadrup.var2):
        lst.append(mem.getValue(cuadrup.var1+x+1))
      value = st.stdev(lst)
      mem.updateValue(value,cuadrup.res)

    def variance(self,cuadrup,mem):
      lst = []
      for x in range(cuadrup.var2):
        lst.append(mem.getValue(cuadrup.var1+x+1))
      value = st.variance(lst)
      mem.updateValue(value,cuadrup.res)

    def recieveParam(self, mem):
        self.parametros.reverse()
        cInt = 0
        cFloat = 0
        cBool = 0
        cChar = 0
        while self.parametros:
            tmp = self.parametros.pop()
            valor = tmp.value
            varType = tmp.type
            if varType == 'int':
                dir = 3500 + cInt
                cInt = cInt +1
            elif varType == 'float':
                dir = 4000 + cFloat
                cFloat = cFloat +1
            elif varType == 'bool':
                dir = 4500 + cBool
                cBool= cBool +1
            elif varType == 'char':
                dir = 5000 + cChar
                cChar = cChar +1
            mem.updateValue(valor, dir)


    def Exe(self, inicio, fin):
        self.memoriamaster.cVMem = self.mem.cVMem
        self.memoriamaster.gVMem = self.mem.gVMem
        self.indx = inicio
        while self.cuadruplos[self.indx].estatuto != fin:
            cuadruplonow = self.cuadruplos[self.indx]
            estatuto = cuadruplonow.estatuto
            if estatuto == '+' or estatuto == '-' or estatuto == '*':
                self.operaciones(cuadruplonow,self.mem)
            elif estatuto == '=':
                self.signoIgual(cuadruplonow, self.mem)
            elif estatuto == 'PRINT':
                self.imprime(cuadruplonow, self.mem)
            elif estatuto == '++' or estatuto == '--':
                self.contadores(cuadruplonow,self.mem)
            elif estatuto == '+' or estatuto == '-' or estatuto == '*':
                self.operaciones(cuadruplonow,self.mem)
            elif estatuto == '/':
                self.division(cuadruplonow,self.mem)
            elif estatuto == '&&' or estatuto == '||' or estatuto == '<' or estatuto == '<=' or estatuto == '>' or estatuto == '>=' or estatuto == '!=' or estatuto == '==':
                self.operacionesLogic(cuadruplonow,self.mem)
            elif estatuto == 'ERA':
                self.era(cuadruplonow)
            elif estatuto == 'GOTO':
                self.goto(cuadruplonow)
            elif estatuto == 'GOTOF':
                self.gotoF(cuadruplonow, self.mem)
            elif estatuto == 'Ver':
                self.veri(cuadruplonow, self.mem)
            elif estatuto == 'ARR':
                self.arrProc(cuadruplonow, self.mem)
            elif estatuto == 'gosub':
                self.goSub(cuadruplonow)
            elif estatuto == 'Params':
                self.sendParam(cuadruplonow,self.mem)
            elif estatuto == 'RETURN':
                self.returns(cuadruplonow,self.mem)
            elif estatuto == 'MEAN':
                self.mean(cuadruplonow,self.mem)
            elif estatuto == 'MODE':
                self.mode(cuadruplonow,self.mem)
            elif estatuto == 'MEDIAN':
                self.median(cuadruplonow,self.mem)
            elif estatuto == 'SDF':
                self.sd(cuadruplonow,self.mem)
            elif estatuto == 'VARIANCE':
                self.variance(cuadruplonow,self.mem)
            else:
                print('ERROR, cuadruplo no acceptado: ')
                print(cuadruplonow.estatuto)
                exit()
            self.indx = self.indx + 1
        #self.memoriamaster.printvm()