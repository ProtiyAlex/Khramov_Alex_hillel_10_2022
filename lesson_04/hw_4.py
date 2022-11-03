from pathlib import Path

from pympler.asizeof import asizeof

LESSON_04_DIR = Path(__file__).parent
SOURSE_FILENAME = LESSON_04_DIR / "sourse.txt"
ROCKYOU_FILENAME = LESSON_04_DIR / "rockyou.txt"


def filter_lines(filename: Path, pattern: str):
    with open(filename, encoding="utf-8") as f:
        while True:
            line = f.readline().strip("\n")
            if not line:
                break
            if pattern in line.lower():
                yield line


def save_to_file(filename: Path, data: list):
    with open(filename, "w", encoding="utf-8") as f:
        data = map(lambda x: x + "\n", data)
        f.writelines(data)


def info(data):
    print(f"size: {asizeof(data) / 1024} KB")
    print(f"number of lines: {len(data)}")


def main():
    search_parameter = input("Enter the search parameter: ")
    source = list(filter_lines(ROCKYOU_FILENAME, search_parameter))
    save_to_file(SOURSE_FILENAME, source)
    info(source)


if __name__ == "__main__":
    main()
