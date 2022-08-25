'''Faça um programa uma ou mais linhas. A última linha lida será vazia. Com exceção da última, cada uma das demais contém um número de ponto flutuante cada. Calcule e escreva na saída padrão a soma de todos os números lidos e a média dos números lidos, ambos com dupla precisão. Caso a primeira linha lida seja vazia, escreva na saída padrão a mensagem: "Nenhuma linha lida com conteúdo, portanto não há soma nem média!
Entradas:                       |                   Saída:
vazio                           |Nenhuma linha lida com conteúdo, portanto não há soma nem média!
10                              |Soma dos números: 50.00
20                              |Média dos números: 12.50
12                              |
8                               |
"'''
numero1, numero2, numero3, numero4 = input('Escolha 4 números:'), input(), input(), input();


if (numero1 == ''):
    print('Nenhuma linha lida com conteúdo, portanto não há soma nem média!')
else:
    soma = float(numero1) + float(numero2) + float(numero3) + float(numero4);
    media = soma / 4;
    print('Soma dos números:', soma);
    print('média dos números:%.2f' % media);

