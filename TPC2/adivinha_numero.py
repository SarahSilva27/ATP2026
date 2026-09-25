import random

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



