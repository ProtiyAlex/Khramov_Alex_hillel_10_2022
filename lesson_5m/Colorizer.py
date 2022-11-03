class Colorizer:
    colors = {"pink": '\033[95m',
              "blue": '\033[94m',
              "green": '\033[92m',
              "yellow": '\033[93m',
              "red": '\033[91m',
              "bold": '\033[1m',
              "underline": '\033[4m', }

    def __init__(self, color: str):
        self.color = color.lower()

    def __enter__(self):
        try:
            print(self.colors[self.color], end='')
        except Exception:
            print(f"\033[91m{self.color} no such color Colorizer \033[0m")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('\033[0m', end='')


with Colorizer('red'):
    print('printed in red')
print('printed in default color')
