import os
from random import choice
from time import sleep

class jogo:
    def __init__(self) -> None:
        None
        
    def menu(self):
        print("---------------------------")
        print("----------- Jogo ----------")
        print("---------------------------")
        
    def clear(self):
        os.system("clear")
        self.menu()
        
    def conectar(self):
        self.clear()
        print("Conectando ao jogo...")
        sleep(1)
        self.clear()
        print("Conectado")

    def jogador(self, choice):
        if choice == 1:
            self.jogada_jogador = "Pedra"
            return self.jogada_jogador
        elif choice == 2:
            self.jogada_jogador = "Papel"
            return self.jogada_jogador
        else:
            self.jogada_jogador = "Tesoura"
            return self.jogada_jogador

    def computador(self):

        opcoes = ["Pedra","Papel","Tesoura"]

        self.jogada_computador = choice(opcoes)

        return self.jogada_computador
    
    def jogar(self, user, computador):
        if user == computador:
            return "Empate"
    
        elif computador == "Pedra" and user == "Tesoura" or computador == "Papel" and user == "Pedra" or computador == "Tesoura" and user == "Papel":
            return False

        else:
            return True