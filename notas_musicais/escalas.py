NOTAS = 'C C# D D# E E# F F# G G# A A# B B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica, tonalidade):
    """
    GERA UMA ESCALA A PARTIR DE UMA TONICA E UMA TONALIDADE

    Parameters:
        Tonica: Nota que sera a tonica da escala
        Tonalidade: Tonalidade da escala

    >>> escalas('C','maior')
    {'notas':['C','D','E','F','G','A','B'], 'graus':['I','II','III','IV','V','VI','VII']}

    >>> esalas('A','maior')
    {'notas':['A','B','C','D','E','F','G'], 'graus':['I','II','III','IV','V','VI','VII']}
    """
    intervalos = ESCALAS[tonalidade]
    tonica_pos = NOTAS.index(tonica)
    temp = []

    for intervalo in intervalos:
        nota = tonica_pos + intervalo
        temp.append(NOTAS[intervalo])

    return {'notas': temp, 'graus':['I','II','III','IV','V','VI','VII']}
