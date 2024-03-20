from time import sleep
from modules.pedra_papel_tesoura import jogo

class Main():
    def __init__(self) -> None:
        self.jogo = jogo()
        self.user_points = 0
        self.computador_points = 0
        
    def executar(self):
        self.jogo.conectar()

        input("APERTE ENTER PARA CONTINUAR")

        while True:
            try:
                self.jogo.clear()

                print("[ 1 ] Pedra")
                print("[ 2 ] Papel")
                print("[ 3 ] Tesoura")
                print("[ 4 ] Pontuação")
                print("[ 5 ] Sair")
                escolha = int(input("Digite a opção desejada: "))
                match escolha:
                    case 1 | 2 | 3:
                        usuario = self.jogo.jogador(escolha)
                        escolha_computador = self.jogo.computador()   
                        
                        self.vencedor = self.jogo.jogar(usuario, escolha_computador)

                        print("Jogando...")
                        sleep(1)
                        if self.vencedor == True:
                            self.user_points += 1
                            print(f"""
Você jogou {self.jogo.jogada_jogador}
Computador jogou {self.jogo.jogada_computador}
Você Venceu!!
""")

                        elif self.vencedor == False:
                            self.computador_points += 1
                            print(f""" 
Você jogou: {self.jogo.jogada_jogador}
Computador jogou: {self.jogo.jogada_computador}
Computador Venceu!!!
""")
                        else:
                            print(f"""
Você jogou {self.jogo.jogada_jogador}
Computador jogou {self.jogo.jogada_computador}
Empate!!!""")

                        input("APERTE ENTER PARA CONTINUAR")
                        

                    case 4:
                        print('--------------------------------')
                        print(f"Seu total de pontos acumulados é: {self.user_points}")
                        print(f"O total de pontos do computador é: {self.computador_points}")

                        if self.user_points > self.computador_points:
                            print(f"Você esta {self.user_points - self.computador_points} pontos na frente!")
                        
                        elif self.user_points < self.computador_points:
                            print(f"O Computador esta {self.computador_points - self.user_points} pontos na frente!")

                        else:
                            print("Você e o computador estão com a mesma quantidade de pontos!")
                            
                        print('--------------------------------')
                        input("APERTE ENTER PARA CONTINUAR")
                        

                    case 5:
                        continuar = int(input("""
Deseja mesmo continuar? 
[1] Sim
[2] Não
"""))
                        
                        match continuar:
                            case 2:
                                print("Finalizado!")
                                break

                            case _:
                                print("Opção invalida!")
                                input("APERTE ENTER PARA CONTINUAR")
                                jogo.clear()
            except ValueError:
                print("Digite apenas números!")
                input("Aperte ENTER para continuar")
                
if __name__ == "__main__":
    main = Main()
    main.executar()