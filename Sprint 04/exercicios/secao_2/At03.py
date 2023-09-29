from functools import reduce

def calcula_saldo(lancamentos):
    saldo = lambda saldopositivo, v: saldopositivo + v[0] if v[1] == 'C' else saldopositivo - v[0]
    mapeamento = map(lambda x: x[0], lancamentos)
    saldoFinal = reduce(saldo, lancamentos, 0)
    return saldoFinal


