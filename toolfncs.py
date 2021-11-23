class params():
    def __init__(self, value, type):
        self.value = value
        self.type = type


class variable:
    def __init__(self, id, tipo, dir,arr):
        self.id = id
        self.tipo = tipo
        self.dir = dir
        self.arrsize = arr

class funcion:
    def __init__(self, id, tipo, dir):
        self.id = id
        self.tipo = tipo
        self.dir = dir
        self.vars = []
        self.plist = []
        self.vmemory = 999999999

class DirFunc:
    def __init__(self):
        self.funclist = []

class cuadruplo:
    def __init__(self, ident, estatuto, var1, var2, res):
        self.ident = ident
        self.estatuto = estatuto
        self.var1 = var1
        self.var2 = var2
        self.res = res   
