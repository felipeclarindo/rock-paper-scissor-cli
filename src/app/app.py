from time import sleep
from .modules.rock_paper_scissor import Jogo
from .utils.utils import clear


class App:
    def __init__(self) -> None:
        self.jogo = Jogo()
        self.user_points = 0
        self.computer_points = 0

    def menu(self):
        clear()
        print("---------------------------------------")
        print("------- Pedra, Papel e Tesoura --------")
        print("---------------------------------------")

    def run(self):
        self.jogo.conectar(self.menu)

        input("APERTE ENTER PARA CONTINUAR")

        while True:
            try:
                self.menu()
                print("[ 1 ] Jogar")
                print("[ 2 ] Pontuação")
                print("[ 3 ] Sair")
                escolha = int(input("Digite a opção desejada: "))
                match escolha:
                    case 1:
                        while True:
                            self.menu()
                            print("[ 1 ] Pedra")
                            print("[ 2 ] Papel")
                            print("[ 3 ] Tesoura")
                            escolha = int(input("Digite sua jogada: "))
                            match escolha:
                                case 1 | 2 | 3:
                                    usuario = self.jogo.jogador(escolha)
                                    escolha_computador = self.jogo.computador()

                                    self.vencedor = self.jogo.jogar(
                                        usuario, escolha_computador
                                    )
                                    self.menu()
                                    print("Jogando...")
                                    sleep(1)
                                    self.menu()
                                    if self.vencedor == True:
                                        self.user_points += 1
                                        print(f"Você jogou: {self.jogo.jogada_jogador}")
                                        print(
                                            f"Computador jogou: {self.jogo.jogada_computador}"
                                        )
                                        print("Você Venceu!!")
                                    elif self.vencedor == False:
                                        self.computer_points += 1
                                        print(f"Você jogou: {self.jogo.jogada_jogador}")
                                        print(
                                            f"Computador jogou: {self.jogo.jogada_computador}"
                                        )
                                        print("Computador Venceu!!!")
                                    else:
                                        print(f"Você jogou: {self.jogo.jogada_jogador}")
                                        print(
                                            f"Computador jogou: {self.jogo.jogada_computador}"
                                        )
                                        print("Empate!!!")
                                    input("APERTE ENTER PARA CONTINUAR")
                                    self.menu()
                                    voltar = str(input("Deseja voltar ao menu? "))
                                    if voltar.lower() in ["sim", "ss", "s"]:
                                        break
                                    else:
                                        continue
                                case _:
                                    print("Digite uma jogada válida!")
                                    input("Aperte ENTER para continuar")

                    case 2:
                        self.menu()
                        print("--------------------------------")
                        print("----------- Pontuação ----------")
                        print("--------------------------------")
                        print(f"Seu total de pontos é: {self.user_points}")
                        print(
                            f"O total de pontos do computador é: {self.computer_points}"
                        )

                        if self.user_points > self.computer_points:
                            print(
                                f"Você esta {self.user_points - self.computer_points} pontos na frente!"
                            )

                        elif self.user_points < self.computer_points:
                            print(
                                f"O Computador esta {self.computer_points - self.user_points} pontos na frente!"
                            )

                        else:
                            print(
                                "Você e o computador estão com a mesma quantidade de pontos!"
                            )

                        print("--------------------------------")
                        input("APERTE ENTER PARA CONTINUAR")

                    case 3:
                        self.menu()
                        sair = str(input("Deseja mesmo sair? "))
                        if sair.lower() in ["sim", "ss", "s"]:
                            self.menu()
                            print("Programa Finalizdo!")
                            break
                        else:
                            continue

            except ValueError:
                print("Digite apenas números!")
                input("Aperte ENTER para continuar")
