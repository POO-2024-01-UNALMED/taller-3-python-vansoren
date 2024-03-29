class TV:
    numTV=0
    def __init__(self,marca,estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._volumen=1
        self._precio=500
        TV.numTV+=1

    def getMarca(self):
        return self._marca
    
    def setMarca(self,marca):
        self._marca=marca

    def setCanal(self,canal):
        if self._estado and canal<121 and canal>0:
            self._canal=canal

    def getCanal(self):
        return self._canal
    
    def setVolumen(self,volumen):
        if self._estado and volumen>=0 and volumen<8:
            self._volumen=volumen

    def getVolumen(self):
        return self._volumen
    
    def setPrecio(self,precio):
        self._precio=precio

    def getPrecio(self):
        return self._precio
    
    def setControl(self,control):
        self._control=control

    def getControl(self):
        return self._control

    @classmethod
    def setNumTV(cls,numTV):
        TV.numTV=numTV
    
    def getNumTV():
        return TV.numTV
    
    def turnOn(self):
        self._estado=True
    
    def turnOff(self):
        self._estado=False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado and self._canal<120:
            self._canal+=1
    
    def canalDown(self):
        if self._estado and self._canal>1:
            self._canal-=1

    def volumenUp(self):
        if self._estado and self._volumen<7:
            self._volumen+=1

    def volumenDown(self):
        if self._estado and self._volumen>0:
            self._volumen-=1
    