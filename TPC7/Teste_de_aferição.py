
#TPC1- ESPECIFICAR AS SEGUINTES LISTAS EM COMPREENSÃO:

#a) Lista formada pelos elementos que não são comuns às duas listas:

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = [i for i in lista1 if i not in lista2] + [i for i in lista2 if i not in lista1]
print (ncomuns)

# b) Lista formada pelas palavras do texto compostas por mais de 3 letras:

texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = [str for str in texto.split() if len(str)>3]
print (lista)

# c) Lista formada por pares do tipo (índice, valor) com os valores da lista dada:

lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(i + 1, lista[i]) for i in range (len(lista))]
print (listaRes) 

#TPC2- À SEMELHANÇA DO QUE FOI FEITO NAS AULAS, REALIZAR AS SEGUINTES TAREFAS:

# a) Especifique uma função que dada uma string e uma substring não vazia, calcula  o número de vezes em que a substring aparece na string, sem que haja sobreposição de substrings:

def strCount(s, subs):

    count=0
    i=0
    strCount_s= len(s)
    strCount_subs= len(subs)

    while i <= strCount_s - strCount_subs:
        if s [i: i + strCount_subs] == subs:
            count += 1 
            i += strCount_subs
        else:
            i += 1
    
    return count

print(strCount("catcowcat", "cat")) # --> 2
print(strCount("catcowcat", "cow")) # --> 1
print(strCount("catcowcat", "dog")) # --> 0

# b) Especifique uma função que recebe uma lista de números inteiros positivos e devolve o menor produto que for possível calcular multiplicando os 3 menores inteiros da lista:

def produtoM3(lista):
    lista_ordenada= sorted (lista)
    return lista_ordenada[0] * lista_ordenada[1] * lista_ordenada[2]

print(produtoM3([12,3,7,10,12,8,9]))
# Resultado esperado: 168 = 3 * 7 * 8

# c) Especifique uma função que dado um número inteiro positivo, repetidamente adiciona os seus dígitos até obter apenas um dígito que é retornado como resultado:

# Input: 38
# Output: 2
# Explicação: 3 + 8 = 11, 1 + 1 = 2.

# Input: 777
# Output: 3
# Explicação: 7 + 7 + 7 = 21, 2 + 1 = 3.

def reduxInt(n):
    while n >= 10:
        soma=0
        for digito in str(n):
            soma += int (digito)
        n= soma 

    return n

print (reduxInt(544))
print (reduxInt(6789))

# d) Especifique uma função que recebe duas strings, `string1` e `string2`, e devolve o índice da primeira ocorrência de `string2` em `string1`, caso não ocorra nenhuma vez a função deverá retornar `-1`:

# Invocação: indexOf("Hoje está um belo dia de sol!", "belo")
# Resultado: 13

# Invocação: indexOf("Hoje está um belo dia de sol!", "chuva")
# Resultado: -1

def myIndexOf(s1, s2):
    tam1= len(s1)
    tam2= len (s2)

    if tam2== 0:
        return 0
    
    for i in range (tam1 - tam2 + 1): #não vale a pena procurar a partir de 9 (0 a 10) se a palavra tem 3 caracteres
        if s1[i: i + tam2] == s2: # ex- s1= "carta", se s2= "ta", s1[3 : 3 + 2] vamos extrair s1[3:5]
            return i
    return -1

print(myIndexOf("Hoje está um belo dia de sol!", "belo"))  # Resultado: 13 #inclui espaços
print(myIndexOf("Hoje está um belo dia de sol!", "chuva")) # Resultado: -1


#TPC3- A REDE SOCIAL

#Considere o seguinte exemplo:

MyFaceBook = [
    {
        'id': 'p1', 
        'conteudo': 'A tarefa de avaliação é talvez a mais ingrata das tarefas...', 
        'autor': 'jcr', 
        'dataCriacao': '2023-07-20', 
        'comentarios': [
            {'comentario': 'Completamente de acordo...', 'autor': 'prh'},
            {'comentario': 'Mas há quem goste...', 'autor': 'jj'}
        ]
    },
    {
        'id': 'p2', 
        'conteudo': 'Segundo post de exemplo', 
        'autor': 'prh', 
        'dataCriacao': '2023-07-21', 
        'comentarios': [
            {'comentario': 'Exatamente!', 'autor': 'jcr'}
        ]
    }
]

# a) `quantosPost`, que indica quantos posts estão registados:

def quantosPost(redeSocial):
    return len(redeSocial)
print("Total de posts:", quantosPost(MyFaceBook))

# b)  `postsAutor`, que devolve a lista de posts de um determinado autor:

def postsAutor(redeSocial, autor):
    return [post for post in redeSocial if post['autor'] == autor]
print("Posts do jcr:")
for post in postsAutor(MyFaceBook, 'jcr'):
    print(post)
print()

# c) `autores`, que devolve a lista de autores de posts ordenada alfabeticamente:

def autores(redeSocial):
    lista_autores = []
    for post in redeSocial:
        if post ["autor"] not in lista_autores:
            lista_autores.append(post["autor"])
    lista_autores.sort()
    return lista_autores 
print("Autores ordenados:", autores(MyFaceBook))

# d) `insPost`, que acrescenta um novo post à rede social a partir dos parâmetros recebidos e devolve a nova rede social. 
    
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    if len(redeSocial) == 0:
        novo_id = "p1"
    else:
        # Extrai o número de cada id existente para encontrar o maior
        max_num = max(int(post['id'][1:]) for post in redeSocial)
        novo_id = f"p{max_num + 1}"
        
    novo_post =  {'id': novo_id,
                 'conteudo': conteudo,
                 'autor': autor,
                 'dataCriacao': dataCriacao,
                 'comentarios': comentarios}
    
    redeSocial.append(novo_post)
    return redeSocial

MyFaceBook = [
    {
        'id': 'p1',
        'conteudo': 'A tarefa de avaliação é talvez a mais ingrata das tarefas...',
        'autor': 'jcr',
        'dataCriacao': '2023-07-20',
        'comentarios': [
            {'comentario': 'Completamente de acordo...', 'autor': 'prh'},
            {'comentario': 'Mas há quem goste...', 'autor': 'jj'}
        ]
    },
    {
        'id': 'p2',
        'conteudo': 'Segundo post de exemplo',
        'autor': 'prh',
        'dataCriacao': '2023-07-21',
        'comentarios': [
            {'comentario': 'Exatamente!', 'autor': 'jcr'}
        ]
    },
    {
        'id': 'p3',
        'conteudo': 'Tirei uma boa nota a ATP!',
        'autor': 'SS',
        'dataCriacao': '15.11.26',
        'comentarios': [{'comentario': 'Parabéns!', 'autor': 'jcr'}]
    }
]

print("Rede social inicial:")
for post in MyFaceBook:
    print(f"- {post['id']} | autor: {post['autor']} | data: {post['dataCriacao']}")
    print(f"  Conteúdo: {post['conteudo']}")
    print(f"  Comentários: {len(post['comentarios'])}")
    for comentario in post['comentarios']:
        print(f"    * {comentario['autor']}: {comentario['comentario']}")
print()

# e)  `remPost`, que remove um post da rede, correspondente ao `id` recebido.

def remPost(redeSocial, id):
    return [post for post in redeSocial if post['id'] != id]

MyFaceBook = remPost(MyFaceBook, "p3")
print("Rede social após remover o post p3:")
for post in MyFaceBook:
    print(f"- {post['id']} | autor: {post['autor']}")
print()

# f) `postsPorAutor`, que devolve uma distribuição de posts por autor.

def postsPorAutor(redeSocial):
    distribuicao = {}
    for post in redeSocial:
        autor = post['autor']
        if autor in distribuicao:
            distribuicao[autor] += 1
        else:
            distribuicao[autor] = 1
    return distribuicao

print("Distribuição por autor:")
for autor, total in postsPorAutor(MyFaceBook).items():
    print(f"- {autor}: {total} post(s)")
print()

# g) `comentadoPor`, que recebe um autor e devolve a lista de posts comentados por esse autor.

def comentadoPor(redeSocial, autor):
    posts_comentados = []
    for post in redeSocial:
        for comentario in post['comentarios']:
            if comentario["autor"] == autor:
                if post not in posts_comentados:
                    posts_comentados.append(post)
    return posts_comentados

print("Posts comentados por jcr:")
for post in comentadoPor(MyFaceBook, "jcr"):
    print(f"- {post['id']} | {post['autor']}: {post['conteudo']}")
print()