print('Métodos e funções de listas no python. Listas são usadas para guardar diversos itens em apenas uma variável\n');

print('list é apenas uma dos 4 data types usados para guardar informações. As outras três são a tuple, set e dictionary. Todas com diferentes qualidades e usabilidade\n')

print('lists são criadas usando colchete [], em inglês \'saquare brackets\'\n')

print('Exemplo de criação de lista\n')

frutas = ['maçã', 'banana', 'cereja']
print(frutas)

print('\n lists possuem ordem, são mutáveis e aceitam valores duplicados\n\n list items são indexados, o primeiro valor possui o índice [0], o segundo [1] e assim por diente.\n')


print('As lists possuem ordem definida e geralmente não mudam(existem métodos que podem mudar a posição de um valor dentro da lista), quando novos itens são adicionados a list, esses itens são colocados no final da lista \n ')

print('PERMITE DUPLICATAS \n\n  Como lists são indexadas, as mesmas podem conter valores repetidos\n')

frutas = ['maçã', 'banana', 'cereja', 'maçã', 'cereja']

print(frutas)

print('LIST LENGTH\n\n Para saber quantos itens existem numa lista, utilize a função len()\n')

print('O número de itens não lista é: ', len(frutas))

print('\nListas, podem ser de qualquer tipo:\n')

list1, list2, list3 = ['maçã', 'banana'], [1, 5, 7, 9, 3], [True, False, True, True]

print('Lista de strings: ',list1,'\n\n', 'Lista de números inteiros: ',list2,'\n\n', 'Lista Bool: ',list3)

print('\nListas podem receber valores data types diferentes na mesma lista:\n')

list4 = ['abc', 34, False, True, 'Teste']

print(list4)

print('\nListas são definidas como objetos do tipo list (<class \'list\') \n')

print(type(list4))

print('\nVocê também pode utilizar o list() constructor para criar uma nova lista: ')

frutas = list(('maçã', 'banana'))

print('\nUtilizando o list construcor(utilizando 2 parênteses) o objeto será do tipo list: ',type(frutas))

print('\nMODOS DE ACESSO\n\n As listas são indexadas, de modo que você consegue acessar os itens dentro da lista através de seus índices: ', list4[1], list4[3])

print('\nÍNDICE NEGATIVO\n\n Utilizando o index de forma negativa, conseguimos acessar os últimos valores de uma lista: ', list4[-1])

listaGrande = ['maçã', 'banana', 'cereja', 'laranja', 'kiwi', 'melão', 'manga']

print('\nRANGE DE ÍNDICES\n\n Você consegue retirar um determinado range de dentro de uma lista, criando assim, uma nova lista com os valores escolhidos: ', listaGrande[2:5])

print('\nPara utilizar um range que pegue o valor do início até outro determinado valor, não é necessário colocar o primeiro índice[0], basta deixar em branco e escolher o valor do término do range. EX: ', listaGrande[:4], '\n\nO mesmo é verdadeiro para o oposto(a partir do último valor). EX: ', listaGrande[4:])

print('\nÍNDICE NEGATIVO COM RANGE\n\n Você pode fazer a mesma coisa com índices negativos. EX: ', listaGrande[-4:-1])

print('\nCHECAGEM DE EXISTÊNCIA DE ITEM EM LISTAS\n\nBasta utilizar a keyword IN. EX: ')

if 'maçã' in frutas:
    print('\nSim, existe maçã na variável frutas\n')

print('Também é possível verificar se algum determinado item não está presente na lista. EX: \n')

if 'chocolate' not in frutas:
    print('Chocolate não está presente na variável frutas\n')

