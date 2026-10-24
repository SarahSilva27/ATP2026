
def mostrar_menu():
    print("\n--- Menu Principal ---")
    print("(1) Criar Tabela Meteorológica")
    print("(2) Guardar Tabela no Ficheiro")
    print("(3) Carregar Tabela do Ficheiro")
    print("(4) Imprimir Tabela")
    print("(5) Temperatura média de cada dia")
    print("(6) Temperatura mínima mais baixa da Tabela")
    print("(7) Amplitude térmica de cada dia")
    print("(8) Dia com valor máximo de precipitação")
    print("(9) Dias com precipitação superior a p")
    print("(10) Maior número consecutivo de dias com precipitação abaixo de p")
    print("(11) Gráficos de temperatura mínima, máxima e de pluviosidade")
    print("(0) Sair")

def criar_tabela_meteorologica():
    tab_meteo = []
    print("\n--- 1. Criar Tabela Meteorológica ---")
    print("Insira os dados meteorológicos. Escreva 'n' quando quiser parar.")

    continuar = True
    while continuar:
        novo = input("\nDeseja adicionar um novo registo? (s/n): ").strip().lower()
        
        if novo == "s":
            print("\nIntrodução da Data:")
            ano = int(input("  Ano (ex: 2026): "))
            mes = int(input("  Mês (1-12): "))
            dia = int(input("  Dia (1-31): "))
            data = (ano, mes, dia)
                
            temp_min = float(input("Temperatura Mínima (°C): "))
            temp_max = float(input("Temperatura Máxima (°C): "))
            precipitacao = float(input("Precipitação (mm): "))
                
            tab_meteo.append((data, temp_min, temp_max, precipitacao))
            print("-> Registo adicionado com sucesso!")
    
        elif novo == "n":
            continuar = False
        else:
            print("Por favor, responda apenas com 's' (sim) ou 'n' (não).")
            
    return tab_meteo  # <-- CORRIGIDO: Devolve a tabela criada

def guardaTabMeteo(t):
    with open("meteorologia.txt", "w", encoding="utf-8") as f: # <-- CORRIGIDO: Nome do ficheiro unificado
            for registo in t:
                data, temp_min, temp_max, precipitacao = registo
                ano, mes, dia = data
                
                linha = f"{ano}|{mes}|{dia},{temp_min},{temp_max},{precipitacao}\n"
                f.write(linha)
    
    print("Dados guardados com sucesso em meteorologia.txt!")

def carregar_tabela_ficheiro():
    res = []
    with open("meteorologia.txt", "r", encoding="utf-8") as f: # <-- CORRIGIDO
        for linha in f:
            campos = linha.strip().split(",")
            novadata = campos[0].split("|")
            
            data = (int(novadata[0]), int(novadata[1]), int(novadata[2]))
            tmin = float(campos[1])
            tmax = float(campos[2])
            prec = float(campos[3])
            
            res.append((data, tmin, tmax, prec)) # <-- CORRIGIDO: Sintaxe do tuplo corrigida
            
    print("Tabela carregada com sucesso do ficheiro!")
    return res


def imprimir_tab_meteo(tab_meteo):
    if not tab_meteo:
        print("Ainda não existem registos meteorológicos. Cria a tabela primeiro (Opção 1).")
    else:
        print(f"\n--- Tabela Meteorológica ({len(tab_meteo)} registos) ---")
        for i, registo in enumerate(tab_meteo, start=1):
            data, temp_min, temp_max, precipitacao = registo
            ano, mes, dia = data
            print(f"{i}. Data: {ano}|{mes}|{dia} , Mín: {temp_min}°C , Máx: {temp_max}°C , Precipitação: {precipitacao} mm")


def medias(tabMeteo): 
    if not tabMeteo:
        print("A tabela está vazia.")
        return
    for registo in tabMeteo:
        Data, tmin, tmax, _ = registo
        print(f"Data: {Data} | Média: {(tmax + tmin) / 2:.2f}°C")


def minMin(tabMeteo):
    if not tabMeteo:
        print("A tabela está vazia.")
        return
    minima = tabMeteo[0][1]
    for registo in tabMeteo[1:]:
        if minima > registo[1]:
            minima = registo[1]
    print(f"Temperatura mínima mais baixa: {minima}°C")


def amplTerm(tabMeteo1):
    if not tabMeteo1:
        print("A tabela está vazia.")
        return
    for registo in tabMeteo1:
        Data, tmin, tmax, _ = registo
        print(f"Data: {Data} | Amplitude: {(tmax - tmin):.2f}°C")   


def maxChuva(tabMeteo):
    if not tabMeteo:
        print("A tabela está vazia.")
        return
    maxChuva1 = tabMeteo[0][3]
    maxData = tabMeteo[0][0]
    for data, _, _, chuva in tabMeteo[1:]:
        if maxChuva1 < chuva:
            maxChuva1 = chuva 
            maxData = data
    print(f"O dia com valor máximo de precipitação foi: {maxData} com precipitação de: {maxChuva1} mm")


def diasChuvosos(tabMeteo, p):
    res = []
    for data, _, _, chuva in tabMeteo:
        if chuva > p:
            res.append((data, chuva))
    return res 

def diasComChuvaSuperiorP(TabMeteo):
    if not TabMeteo:
        print("A tabela está vazia.")
        return
    p_str = input("Introduza o valor limite de precipitação (mm): ")
    p = float(p_str)

    resultado = diasChuvosos(TabMeteo, p)

    if not resultado:
        print(f"Não existem dias com precipitação superior a {p} mm.")
    else:
        print(f"\n--- Dias com precipitação superior a {p} mm ---")
        for data, chuva in resultado:
            ano, mes, dia = data
            print(f"Data: {ano}|{mes}|{dia} , Precipitação: {chuva} mm")


def maior_dias_abaixo_de_p(tabMeteo, p):
    max_consecutivos = 0
    atual_consecutivos = 0
    
    for data, _, _, chuva in tabMeteo:
        if chuva < p:
            atual_consecutivos += 1
            if atual_consecutivos > max_consecutivos:
                max_consecutivos = atual_consecutivos
        else:
            atual_consecutivos = 0  
            
    return max_consecutivos

def maiorNdeDiasConsecutivosAbaixoP(tabMeteo):
    if not tabMeteo:
        print("A tabela está vazia.")
        return
    p_str = input("Introduza o valor limite de precipitação (mm): ")
    p = float(p_str)

    resultado = maior_dias_abaixo_de_p(tabMeteo, p)

    if resultado == 0:
        print(f"Não existem quaisquer dias com precipitação abaixo de {p} mm.")
    else:
        print(f"O maior número consecutivo de dias com precipitação abaixo de {p} mm foi de: {resultado} dias.")

def grafico_texto_meteorologia(tabMeteo):
    if not tabMeteo:
        print("A tabela meteorológica está vazia. Não há dados para mostrar.")
        return

    print("\n--- Gráfico de Precipitação (por dia) ---")
    print("Cada '#' representa aprox. 1 mm de precipitação.\n")

    for registo in tabMeteo:
        data, _, _, precipitacao = registo
        ano, mes, dia = data
        data_str = f"{ano}|{mes}|{dia}"
        
        num_barras = int(max(0, precipitacao))
        barra = "#" * num_barras
        
        print(f"{data_str} | {barra} ({precipitacao} mm)") # <-- CORRIGIDO: Parêntese corrigido

    print("\n--- Legenda de Temperaturas (Máx / Mín) ---")
    for registo in tabMeteo:
        data, tmin, tmax, _ = registo
        ano, mes, dia = data
        data_str = f"{ano}|{mes}|{dia}"
        print(f"{data_str} -> Máx: {tmax}ºC | Mín: {tmin}ºC")

def main():
    tabela = []  # <-- CORRIGIDO: Inicializado como lista em vez de dicionário {}
    executar = True

    while executar:
        mostrar_menu()
        opcao = input("\nEscolhe uma opção: ")

        if opcao == "1":
           tabela = criar_tabela_meteorologica()  # <-- CORRIGIDO: Guarda o retorno
        elif opcao == "2":
            guardaTabMeteo(tabela)
        elif opcao == "3":
            tabela = carregar_tabela_ficheiro()   # <-- CORRIGIDO: Guarda o retorno
        elif opcao == "4":
            imprimir_tab_meteo(tabela)
        elif opcao == "5":
            medias(tabela)
        elif opcao == "6":
            minMin(tabela)
        elif opcao == "7":
            amplTerm(tabela)
        elif opcao == "8":
            maxChuva(tabela)
        elif opcao == "9":
            diasComChuvaSuperiorP(tabela)
        elif opcao == "10":
            maiorNdeDiasConsecutivosAbaixoP(tabela)
        elif opcao == "11":
            grafico_texto_meteorologia(tabela)
        elif opcao == "0":
            print("A sair da aplicação.")
            executar = False
        else:
            print("Opção inválida! Por favor, escolha um número válido do menu.")

if __name__ == "__main__":
    main()