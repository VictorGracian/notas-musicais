from pytest import mark
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_retornar():
    result = runner.invoke(app)
    assert result.exit_code == 0

@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_conter_notas(nota):
    result = runner.invoke(app)
    assert nota in result.stdout

@mark.parametrize('nota', ['F', 'F', 'A', 'A#', 'C', 'D', 'E'])
def test_conter_notas_fa(nota):
    result = runner.invoke(app, 'F')
    assert nota in result.stdout

@mark.parametrize('nota', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_conter_graus(nota):
    result = runner.invoke(app)
    assert nota in result.stdout
