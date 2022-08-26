'''Faça um programa, contendo subprogramas, que, recursivamente, calcule a potência de um número inteiro na base b elevado ao expoente inteiro exp. Para tal, faça as seguintes etapas:
a) Receba dois valores de entrada:
b)Utilizando subprograma, verifique se os elementos são inteiros. Se alguma das entradas não for do tipo inteiro, então retorne dizendo especificamente qual entrada não foi inteira. Se ambas as entradas não forem do tipo inteiro, então retorne dizendo que ambas as entradas não são do formato correto.
c) Se ambos os elementos da entrada forem do tipo inteiro, utilizando chamadas recursivas, obtenha o valor de b^exp

Testes: 

Entradas                                | Saídas
3 : i                                   | Expoente i não está no formato devido
3 : 4                                   | 3 elevado a 4 é iagual a 81
b : 3                                   | Base b não está no formato devido
b : e                                   | Base b e expoente e não estão no formato devid:'''

base, expoente = input('Adicione uma base que pertença aos inteiros:'), input('Adicione um expoente que pertença aos inteiros:')

def expoenencicao(base, expoente):
    if base.isnumeric() != True and expoente.isnumeric() != True:
        print('A base b e expoente e não estão no formato devido')
    elif base.isnumeric() != True:
        print('Base b não está no formato devido')
    elif expoente.isnumeric() != True:
        print('Expoente i não está no formato devido')
    else:
        print(base , 'elevado a,' , expoente , 'é igual a ', int(base)**int(expoente))

print(expoenencicao(base, expoente))