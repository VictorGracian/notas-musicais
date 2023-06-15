"""
AAA - 3A - 3A

Arange -  Act - Assets!
Arrumar - Agir -  Garantir!
"""
from pytest import raises

from notas_musicais.escalas import ESCALAS, NOTAS, escalas


def test_escalas_notas_minusculas():
    # Arrumar
    tonica = 'a'
    tonalidade = 'maior'

    # Agir
    result = escalas(tonica, tonalidade)

    # Assert
    assert result


def test_mensagem_erro():
    tonica = 'X'
    tonalidade = 'menor'

    mensagem_erro = f'Essa nota não existe, tente uma dessas , {NOTAS}'

    with raises(ValueError) as error:
        escalas(tonica, tonalidade)

    assert mensagem_erro == error.value.args[0]


def test_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_erro = f'Essa escala não foi implementada, tente uma dessas {list(ESCALAS.keys)}'

    with raises(KeyError) as error:
        escalas(tonica, tonalidade)

    assert mensagem_erro == error.value.args[0]