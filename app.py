# -*- coding: UTF-8 -*-

import re

def listar(nomes):
    print 'Listando nomes: '
    for nome in nomes:
        print nome

def cadastrar(nomes):
    print('Digite o nome: ')
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
   print 'Qual nome você gostaria de remover?'
   nome = raw_input()
   nomes.remove(nome)

def alterar(nomes):
    print 'Qual nome você gostaria de alterar?'
    nome = raw_input()
    if(nome in nomes):
        print 'Digite o novo nome: '
        novo_nome = raw_input
        nomes[nomes.index(nome)] = novo_nome
    else:
        print 'Nome inexistente' 

def procurar_regex(nomes):
    print 'Digite o nome a procurar:'
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print resultados

def procurar(nomes):
    print 'Digite nome a procurar:'
    nome_a_procurar = raw_input()

    if(nome_a_procurar in nomes):
        print 'O nome já existe'
    else:
        print 'Nome inexistente'

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print('Digite 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para pesquisar e 0 para terminar')
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            remover(nomes)

        if(escolha == '4'):
            alterar(nomes)

        if(escolha == '5'):
            procurar_regex(nomes)
menu()