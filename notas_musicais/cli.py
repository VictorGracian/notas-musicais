from notas_musicais.escalas import escalas
from rich import print
from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

console = Console() 
app = Typer()

@app.command()
def escala(tonica=Argument('c'), tonalidade=Argument('maior')):
    table = Table()

    notas, graus = escalas(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)

    console.print(table)
