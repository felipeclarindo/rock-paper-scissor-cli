import os
from random import choice
from time import sleep
from ..utils.utils import clear


class Jogo:
    def __init__(self) -> None:
        pass

    def menu(self) -> None:
        print("---------------------------")
        print("----------- Jogo ----------")
        print("---------------------------")

    def clear(self) -> None:
        os.system("clear")
        self.menu()

    def conectar(self, menu: callable) -> None:
        menu()
        print("Iniciando o jogo...")
        sleep(1)
        menu()
        print("Jogo iniciado")

    def jogador(self, choice) -> None:
        if choice == 1:
            self.jogada_jogador = "Pedra"
            return self.jogada_jogador
        elif choice == 2:
            self.jogada_jogador = "Papel"
            return self.jogada_jogador
        else:
            self.jogada_jogador = "Tesoura"
            return self.jogada_jogador

    def computador(self) -> None:

        opcoes = ["Pedra", "Papel", "Tesoura"]

        self.jogada_computador = choice(opcoes)

        return self.jogada_computador

    def jogar(self, user, computador) -> None:
        if user == computador:
            return "Empate"

        elif (
            computador == "Pedra"
            and user == "Tesoura"
            or computador == "Papel"
            and user == "Pedra"
            or computador == "Tesoura"
            and user == "Papel"
        ):
            return False

        else:
            return True
