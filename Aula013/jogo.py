from funcoes import roladados
from time import sleep
continuar = "s"
computador = 0
eu = 0
while continuar == "s":
    print("Bem Vindo ao Jogo")
    print("Você começa!!!")
    jogada_pc = roladados()
    sleep(2)
    print(f"Você tirou {jogada_pc}. Agora é Minha Vez:")
    jogada_eu = roladados()
    sleep(2)
    print(f"Eu tirei {jogada_eu}")
    if jogada_pc > jogada_eu:
        print("PARABÉNS! Você Ganhou!")
        computador += 1
    elif jogada_pc == jogada_eu:
        print("Nós Empatamos!")
    else:
        print("Eu ganhei!!!")
        eu += 1
    continuar = input("Você quer continuar? Digite S para Sim e N para não.").lower()


print("O Jogo Terminou. O resultado da partida foi\n"
      f"Computador {computador} x Eu {eu}!!!")


