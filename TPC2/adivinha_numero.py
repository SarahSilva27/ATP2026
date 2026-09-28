
import random

print ("Bem Vindo ao Jogo- Adivinha o número!")
print ("1- Tu adivinhas")
print ("2- Computador adivinha")

modo= input ("Escolha o modo (1 ou 2): "). strip()

if modo == "1":

 num_secreto = random.randint(0,100)


 N = int(input("Diga um número: "))
 t = 1

 if N == num_secreto: 
    print ("Acertou em " + str(t) + " tentativas!")
 elif N > num_secreto:
    print ("O número que pensei é menor.")
 else:
    print ("O número que pensei é maior.")

 while N != num_secreto:
    N = int(input("Diga um número: "))
    t = t+1
    if N == num_secreto: 
        print ("Acertou em " + str(t) + " tentativas!")
    elif N > num_secreto:
        print ("O número que pensei é menor.")
    else:
        print ("O número que pensei é maior.")


elif modo== "2":
     num_secreto= int (input("Escolhe um número: "))
     N= -1
     lim_inf= -1
     lim_sup=101
     tent= 0
     
     while N!= num_secreto:
        N = random.randint (lim_inf+1,lim_sup-1)
        print(N)
        tent= tent + 1

        if (N>num_secreto):
            lim_sup= N 
        else:
            lim_inf= N
     print ("Acertou em " + str (tent) + " tentativas.")

 



