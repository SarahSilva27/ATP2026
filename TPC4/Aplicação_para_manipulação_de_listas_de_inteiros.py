import random


def mostrar_menu():
    print("\n--- Menu Principal ---")
    print("(1) Criar Lista (Números Aleatórios)")
    print("(2) Ler Lista (Introduzidos pelo Utilizador)")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")


def criar_lista_aleatoria():
    quantidade = int(input("Quantos números aleatórios deseja na lista? "))
    nova_lista = [random.randint(1, 100) for _ in range(quantidade)]
    print("Lista criada com sucesso:", nova_lista)
    return nova_lista


def ler_lista_utilizador():
    quantidade = int(input("Quantos números quer introduzir? "))
    nova_lista = []

    for i in range(quantidade):
        numero = int(input(f"Digite o {i+1}º número: "))
        nova_lista.append(numero)

    print("Lista guardada com sucesso:", nova_lista)
    return nova_lista

def calcular_soma(lista):
    if not lista:
        print("Aviso: A lista está vazia.")
    else:
        print(f"Soma dos elementos: {sum(lista)}")


def calcular_media(lista):
    if not lista:
        print("Aviso: A lista está vazia.")
    else:
        media = sum(lista) / len(lista)
        print(f"Média dos elementos: {media}")


def calcular_maior(lista):
    if not lista:
        print("Aviso: A lista está vazia.")
    else:
        print(f"Maior elemento: {max(lista)}")


def calcular_menor(lista):
    if not lista:
        print("Aviso: A lista está vazia.")
    else:
        print(f"Menor elemento: {min(lista)}")


def verificar_crescente(lista):
   crescente = True
       
   for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            crescente = False
   
   if crescente:
       print ("Crescente")
   else:
        print ("Não ordenada")


def verificar_decrescente(lista):
    decrescente = True
    
    for i in range(len(lista) - 1):
        
        if lista[i] < lista[i + 1]:
            decrescente = False

    if decrescente:
        print ("Decrescente")
    else:
        print ("Não ordenada")


def procurar_elemento(lista):
    if not lista:
        print("Aviso: A lista está vazia.")
    else:
        elem = int(input("Qual número deseja procurar: "))
        res = 0 # Começa na posição 0
        encontrou = 0
        for n in lista:
            if elem == n:
                encontrou = 1
                print(f"Encontrado na posição {res}")  
            res = res + 1  
        
        if encontrou != 1: print("Elemento não encontrado")


def main():
    lista = []
    continuar = True

    while continuar:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            lista = criar_lista_aleatoria()
        elif opcao == "2":
            lista = ler_lista_utilizador()
        elif opcao == "3":
            calcular_soma(lista)
        elif opcao == "4":
            calcular_media(lista)
        elif opcao == "5":
            calcular_maior(lista)
        elif opcao == "6":
            calcular_menor(lista)
        elif opcao == "7":
            verificar_crescente(lista)
        elif opcao == "8":
            verificar_decrescente(lista)
        elif opcao == "9":
            procurar_elemento(lista)
        elif opcao == "0":
            print(f"\n A terminar a aplicação. A lista final guardada é: {lista}")
            continuar = False
        else:
            print("Opção inválida! Por favor, escolha um número entre 0 e 9.")


if __name__ == "__main__":
    main()