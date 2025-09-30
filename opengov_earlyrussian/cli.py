import json
import typer
from rich.console import Console
from rich.table import Table
from opengov_earlyrussian.core.alphabet import AlphabetTeacher
from opengov_earlyrussian.core.cases import CasesTeacher
from opengov_earlyrussian.core.verbs import VerbConjugator
from opengov_earlyrussian.core.transliteration import Transliterator

app = typer.Typer(help="OpenGov-EarlyRussian CLI")
console = Console()


@app.command()
def alphabet(row: str = typer.Argument("iotated")) -> None:
    """Display Russian alphabet rows."""
    teacher = AlphabetTeacher()
    result = teacher.get_row(row)
    console.print(json.dumps(result, ensure_ascii=False, indent=2))


@app.command()
def decline(noun: str, gender: str, animate: bool = False) -> None:
    """Decline a Russian noun through all cases."""
    teacher = CasesTeacher()
    result = teacher.decline_noun(noun, gender, animate)

    table = Table(title=f"Declension: {noun} ({gender})")
    table.add_column("Case", style="cyan")
    table.add_column("Form", style="green")

    for case, form in result.items():
        table.add_row(case, form)

    console.print(table)


@app.command()
def conjugate(verb: str, tense: str = "present") -> None:
    """Conjugate a Russian verb."""
    conjugator = VerbConjugator()
    result = conjugator.conjugate(verb, tense)

    table = Table(title=f"Conjugation: {verb} ({tense})")
    table.add_column("Person", style="cyan")
    table.add_column("Form", style="green")

    if "forms" in result:
        for person, form in result["forms"].items():
            table.add_row(person, form)

    console.print(table)


@app.command()
def translit(text: str) -> None:
    """Transliterate Latin text to Russian."""
    transliterator = Transliterator()
    result = transliterator.to_russian(text)
    console.print(f"[bold green]{result}[/bold green]")


@app.command()
def version() -> None:
    """Show version information."""
    from opengov_earlyrussian import __version__

    console.print(f"OpenGov-EarlyRussian v{__version__}")


if __name__ == "__main__":
    app()
