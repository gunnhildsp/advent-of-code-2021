from pathlib import Path


THIS_DIR = Path(__file__).parent
DATA_DIR = THIS_DIR / "data"


def read_file_as_int(day):
    file_path = DATA_DIR / f"{day}.txt"
    with open(file_path) as file:
        lines = file.readlines()
    return [int(line.strip()) for line in lines]
