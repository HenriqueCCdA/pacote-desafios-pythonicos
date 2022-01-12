"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++

def lendo_arquivo(filename):
    with open(filename) as file:
        lines = file.readlines()

    return lines

def conta_palavras(lines):
    count_words = dict()
    for line in lines:
        words = line.split()
        for word in words:
            try:
                count_words[word.lower()] +=1
            except:
                count_words[word.lower()] = 1

    return count_words

def dicicionario_para_lista_de_tuplas(count_words):
    return [(chave, valor) for chave, valor in count_words.items()]


def conta_palavras_arquivo(filename):
    lines = lendo_arquivo(filename)

    count_words = conta_palavras(lines)

    count_words_list = dicicionario_para_lista_de_tuplas(count_words)

    return count_words_list


def print_words(filename):

    count_words_list = conta_palavras_arquivo(filename)
    count_words_list = sorted(count_words_list, key=lambda x: x[1], reverse=True)

    for word, count in count_words_list:
        print(word, count)


def print_top(filename):

    count_words_list = conta_palavras_arquivo(filename)
    count_words_list = sorted(count_words_list, key=lambda x: x[1], reverse=True)

    for word, count in count_words_list[:19]:
        print(word, count)


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
