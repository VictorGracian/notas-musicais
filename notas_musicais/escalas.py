NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    GERA UMA ESCALA A PARTIR DE UMA TONICA E UMA TONALIDADE

    Parameters:
        Tonica: Nota que sera a tonica da escala
        Tonalidade: Tonalidade da escala

    Returns:
        Um dicionario com as notas da escala e os graus

    Raises:
        ValueError: Caso a nota tonica não seja valida
        KeyError:  Caso a tonalidade não exista

    Examples:
        >>> escalas('C','maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('a','maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas {NOTAS}')
    except KeyError:
        raise KeyError(
            f'Essa escala não foi implementada, tente uma dessas {list(ESCALAS.keys())}'
        )
    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
