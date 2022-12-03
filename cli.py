from src.api import aoc
from src.utils import file_operations
from typing import Dict, List
import typer


app = typer.Typer()


@app.command()
def main(day: int, year: int = 2022) -> str:
    day_exists = file_operations.day_exists(day, year)
    if day_exists:
        print("Day already exists!")
        return

    title = aoc.get_title_for_day(day, year)
    print(f"Creating {title}")
    file_operations.create_files_for_day(day, year)


@app.command()
def update_readme():
    print("Updating readme!")


if __name__ == "__main__":
    app()