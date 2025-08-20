from os import system, name


def clear() -> None:
    if name == "nt":
        system("cls")
    else:
        system("clear")
