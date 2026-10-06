import random

turn = int(input("Quem começa (0 - PC | 1 - Tu): "))

if(turn == 0):
    turnPC = 0
elif(turn == 1):
    turnPC = 1
else:
    print("Opção não suportada")

def pc_play(total):
    
    if(total >= 90):
        guess = 100-total
        total = 100
        print("O PC chegou a 100 com o número " + str(guess))
    else:
        guess = random.randint(1,10)
        total = total + guess
        print("O pc jogou o número " + str(guess) + " somando a um total de " + str(total))
        player_play(total)

def player_play(total):
    guess = int(input("Insira um número de 1 a 10: "))
    if(total + guess > 100):
        print("Maior que 100, mudança de vez para o PC")
        pc_play(total)
    elif(total + guess == 100):
        print("Ganhaste!!")
        total = 100
    else:
        total = total + guess
        print(total)
        pc_play(total)

if(turnPC == 0):
    pc_play(0)
elif(turnPC == 1):
    player_play(0)
