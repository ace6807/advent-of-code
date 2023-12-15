from pathlib import Path
import shutil

PY_FILE_TEMPLATE_PATH = "./src/day_template.py"

def get_path_str_for_day(day: int, year: int = 2022) -> str:
    return f"./{year}/day{day}"


def create_files_for_day(day: int, year: int = 2022):
    dir_path = get_path_str_for_day(day, year)
    input_file_path = f"{dir_path}/input.txt"
    sample_file_path = f"{dir_path}/sample.txt"
    source_file_path = f"{dir_path}/day{day}.py"
    
    Path(dir_path).mkdir()
    Path(input_file_path).touch()
    Path(sample_file_path).touch()
    shutil.copy(PY_FILE_TEMPLATE_PATH, source_file_path)


def day_exists(day: int, year: int = 2022) -> bool:
    dir_path = get_path_str_for_day(day, year)
    return Path(dir_path).exists()