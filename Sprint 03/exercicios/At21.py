class Passaro:
    def __init__(self, voar, emitirSom):
        self.voar = voar
        self.emitirSom = emitirSom

class Pato(Passaro):
    def __init__(self, voar, emitirSom):
        super().__init__(voar, emitirSom)
    pass

class Pardal(Passaro):
    def __init__(self, voar, emitirSom):
        super().__init__(voar, emitirSom)
    pass

Pat = Pato('Voando', 'Quack Quack')
Par = Pardal('Voando', 'Piu Piu')
print('Pato')
print(f'{Pat.voar}...')
print(f'Pato emitindo som...')
print(f'{Pat.emitirSom}')
print('Pardal')
print(f'{Par.voar}...')
print(f'Pardal emitindo som...')
print(f'{Par.emitirSom}')