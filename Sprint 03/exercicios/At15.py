class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
    def liga(self):
        self.ligada = True
    def desliga(self):
        self.ligada = False
    def esta_ligada(self):
        return self.ligada

    
VarBool = True
lamp = Lampada(VarBool)
lamp.liga()
print(f'A lampada está ligada?{lamp.ligada}')
lamp.desliga()
print(f'A lampada ainda está ligada?{lamp.ligada}')

