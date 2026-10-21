
import random

def mostrar_menu():
    print("\n--- Menu Principal ---")  #\n - enter (linha nova)
    print("(1) Criar uma turma")
    print("(2) Inserir um aluno na turma")
    print("(3) Listar a turma")
    print("(4) Consultar um aluno por ID")
    print("(8) Guardar a turma em ficheiro")
    print("(9) Carregar uma turma de um ficheiro")
    print("(0) Sair da aplicação")

def criar_turma(turmas):

    nome_turma = input("Introduz o nome da turma a criar (ex: 10ºA): ")

    if nome_turma in turmas:
        print("Essa turma já existe!")
    else:
        turmas[nome_turma] = []
        print(f"Turma '{nome_turma}' criada com sucesso!")
        

def inserir_aluno_na_turma(turmas):
   
   if not turmas:
        print("Ainda não existem turmas criadas. Cria uma turma primeiro (Opção 1).")
   else:     
    print("\nTurmas disponíveis:", list((turmas)))
    nome_turma = input("Em qual turma queres colocar o aluno? ")

    if nome_turma in turmas:
        nome_aluno = input("Introduz o nome do aluno: ")
        id_aluno = input("Introduz o ID do aluno: ")  
        
        # Pedir as notas para preencher a lista [notaTPC, notaProj, notaTeste]
        nota_tpc = float(input("Introduz a nota do TPC: "))
        nota_proj = float(input("Introduz a nota do Projeto: "))
        nota_teste = float(input("Introduz a nota do Teste: "))
                
        # Estrutura exigida: aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        aluno = (nome_aluno, id_aluno, [nota_tpc, nota_proj, nota_teste])
        
        turmas[nome_turma].append(aluno)
        print(f" Aluno '{nome_aluno}' adicionado com sucesso à turma '{nome_turma}' com o ID **{id_aluno}**!")
    else:
        print(" Erro: Essa turma não existe.")
    

def listar_turma(turmas):
    if not turmas:
        print("Ainda não existem turmas criadas. Cria uma turma primeiro (Opção 1).")
    else:    
       print("\nTurmas disponíveis:", list((turmas)))
       nome_turma = input("Que turma queres listar? ")

    if nome_turma in turmas:
       print(f"\n--- Alunos da Turma {nome_turma} ---")
       alunos = turmas[nome_turma]
       
       if not alunos:
            print("Esta turma ainda não tem alunos.")
       else:
            for i, aluno in enumerate(alunos, start=1):
                nome, id_aluno, notas = aluno
                print(f"{i}. ID: {id_aluno} | Nome: {nome} | Notas: {notas}")
    else:
        print("Erro: Essa turma não existe.")

def consultar_aluno_por_id(turmas):
    if not turmas:
        print("Ainda não existem turmas criadas.")
    else:
        id_procurado = input("Introduz o ID do aluno que queres consultar: ")
        encontrado = False

        for nome_turma in turmas:
            if not encontrado:
                alunos = turmas[nome_turma]
                for aluno in alunos:
                    if not encontrado:
                        nome, id_aluno, notas = aluno
                        if id_aluno == id_procurado:
                            print(f"\n Aluno encontrado!")
                            print(f"Nome: {nome}")
                            print(f"Turma: {nome_turma}")
                            print(f"ID: {id_aluno}")
                            print(f"Notas: {notas}")
                            encontrado = True
                      
        if not encontrado:
            print(f"Erro: Nenhum aluno com o ID '{id_procurado}' foi encontrado.")

def guardar_turmas_ficheiro(turmas):
    if not turmas:
        print("Não há turmas para guardar.")
    else:
        nome_ficheiro = input("Introduz o nome do ficheiro para guardar (ex: turmas.txt): ")
        try:
            with open(nome_ficheiro, "w", encoding="utf-8") as f: #w-writing
                for nome_turma in turmas:
                    alunos = turmas[nome_turma]
                    for aluno in alunos:
                        nome, id_aluno, notas = aluno
                        f.write(f"{nome_turma};{id_aluno};{nome};{notas[0]};{notas[1]};{notas[2]}\n")
            print(f"Dados guardados com sucesso no ficheiro '{nome_ficheiro}'!")
        except Exception as e:
            print(f"Erro ao guardar o ficheiro: {e}")


def carregar_turmas_ficheiro(turmas):
    nome_ficheiro = input("Introduz o nome do ficheiro a carregar (ex: turmas.txt): ")
    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f: #r- reading
            for linha in f:
                linha = linha.strip() 
                if linha:
                    partes = linha.split(";") #split-separa (neste caso, ao encontrar ;)
                    if len(partes) == 6: #para identificar uma linha válida com as 3 notas 
                        nome_turma, id_aluno, nome_aluno, n_tpc, n_proj, n_teste = partes
                        
                        if nome_turma not in turmas:
                            turmas[nome_turma] = []
                        
                        aluno_existente = any(a[1] == id_aluno for a in turmas[nome_turma])
                        if not aluno_existente:
                            notas = [float(n_tpc), float(n_proj), float(n_teste)]
                            aluno = (nome_aluno, id_aluno, notas)
                            turmas[nome_turma].append(aluno)
                                
        print(f" Turmas carregadas com sucesso a partir de '{nome_ficheiro}'!")
    except FileNotFoundError:
        print(f" Erro: O ficheiro '{nome_ficheiro}' não foi encontrado.")
    except Exception as e:
        print(f" Erro ao ler o ficheiro: {e}")


def main():
    turmas = {}
    executar = True

    while executar:
        mostrar_menu()
        opcao = input("\nEscolhe uma opção: ")

        if opcao == "1":
            criar_turma(turmas)
        elif opcao == "2":
            inserir_aluno_na_turma(turmas)
        elif opcao == "3":
            listar_turma(turmas)
        elif opcao == "4":
            consultar_aluno_por_id(turmas)
        elif opcao == "8":
            guardar_turmas_ficheiro(turmas)
        elif opcao == "9":
            carregar_turmas_ficheiro(turmas)
        elif opcao == "0":
            print("A sair da aplicação.")
            executar = False
        else:
            print("Opção inválida! Por favor, escolha um número entre 0 e 9, exceto 5, 6 e 7.")


if __name__ == "__main__":
    main()