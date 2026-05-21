import os
import shutil


class ConsoleUtils:

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def gotoxy(x, y):
        print(f"\033[{y};{x}H", end="")

    @staticmethod
    def print_header(text):
        print(f"\n{text}\n")

    @staticmethod
    def get_console_size():
        return shutil.get_terminal_size((80, 24))

    @staticmethod
    def center_text(text, width=None):

        if width is None:
            width = ConsoleUtils.get_console_size().columns

        return text.center(width)

    @staticmethod
    def print_box(title, lines, symbol="═"):

        # ancho fijo (ajústalo si quieres)
        box_width = 60

        # borde superior
        print(f"╔{symbol * (box_width - 2)}╗")

        # título
        if title:

            print(
                f"║ {title.center(box_width - 4)} ║"
            )

            print(
                f"╠{symbol * (box_width - 2)}╣"
            )

        # contenido
        for line in lines:

            if len(line) > box_width - 4:
                line = line[:box_width - 7] + "..."

            padding = box_width - len(line) - 4

            print(
                f"║ {line}{' ' * padding} ║"
            )

        # borde inferior
        print(f"╚{symbol * (box_width - 2)}╝")
