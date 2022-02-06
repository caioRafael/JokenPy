from colorama import Fore
import os
import random

#jogardor manda uma posição
#randomicamente a cpu manda uma posição

#o jogo verifica quem ganhou 
#score+1 para quem ganhou 

class Jokenpo:
    def __init__(self):
        self.playerScore = 0
        self.cpuScore = 0

        self.playerMove = 0
        self.cpuMove = 0

        self.plays = ["Pedra","Papel","Tesoura"]

        self.endGame = "n"
        self.endOptions = ["s","n"]

        self.jokenpo()

    def startPlays(self):
        self.playerMove = int(input(Fore.RED+"Faça sua jogada: "))
        while self.playerMove > 2:
            print(Fore.YELLOW+"jogada invalida")
            self.playerMove = int(input(Fore.RED+"Faça sua jogada: "))
        self.cpuMove = random.randint(0,2)
    
    def verifyVictory(self):
        if self.playerMove == self.cpuMove:
            print("Empate")
        elif self.playerMove == 0 and self.cpuMove == 2:
            print("Vitoria do jogador")
            self.playerScore += 1
        elif self.playerMove == 2 and self.cpuMove == 0:
            print("Vitoria do computador")
            self.cpuScore += 1
        elif self.playerMove == 2 and self.cpuMove == 1:
            print("Vitoria do jogador")
            self.playerScore += 1
        elif self.playerMove == 1 and self.cpuMove == 2:
            print("Vitoria do computador")
            self.cpuScore += 1
        elif self.playerMove == 1 and self.cpuMove == 0:
            print("Vitoria do jogador")
            self.playerScore += 1
        elif self.playerMove == 0 and self.cpuMove == 1:
            print("Vitoria do computador")
            self.cpuScore += 1

    def end(self):
        self.endGame = input("Deseja finalizar o jogo? s/n: ")
        while True:
            if self.endGame in self.endOptions:
                break
            else:
                print("Opção invalida")
                self.endGame = input("Deseja finalizar o jogo? s/n: ")

    def jokenpo(self):
        while self.endGame != 's':
            os.system("clear")
            print(Fore.RESET+"Pontuação:")
            print(Fore.RESET+"Jogador: "+Fore.GREEN+f"{self.playerScore}")
            print(Fore.RESET+"Computador: "+Fore.MAGENTA+f"{self.cpuScore}")
            print(Fore.GREEN+"---Jokenpô---")
            for i in range(0,3):
                print(Fore.BLUE + f"{i} - {self.plays[i]}")
            self.startPlays()
            print(Fore.RESET+"Jogador: "+Fore.MAGENTA+self.plays[self.playerMove])
            print(Fore.RESET+"Computador: "+Fore.MAGENTA+self.plays[self.cpuMove])
            self.verifyVictory()
            self.end()

if __name__ == "__main__":
    Jokenpo()