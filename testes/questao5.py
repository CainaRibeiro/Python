'''faça um programa, contendo subprogramas, que, receba duas strings na entrada, não necessariamente com os mesmos tamanhos, e identificando qual a string de menor tamanho dentre as duas, retorne uma subcadeia da maior string que esteja com o menor número de caracteres diferentes comparada com a menor string. Retorne o número de caracteres distintos, qual a posição que se inicia essa subcadeia com menor número de caracteres distintos e também a string de maior tamanho. Faça tal como os testes abaixo:

Teste:
Entradas:                                   | Saídas
fundamentosdeprogramacao                    | A subcadeia mais próxima tem 0 caracteres distintos e começa na 
prog                                        | posição 14 da cadeia fundamentosdeprogramacao

fundamentosdeprogramacao                    | A subcadeia mais proxima tem 2 caracteres distintos e começa na dfprof                                      | posição 12 da cadeia fundamentosdeprogramacao

prof                                        | A subcadeia mais próxima tem 1 caracteres distintos e começa na programacao                                 | posição 1 da cadeia programacao'''

'''passos
1) 2 inputs || done
2) identificar a menor string || done
3) retornar subcadeia da maior string e retornar a que estiver igual a da menor string 
5) retornar o número de caracteres distintos
6) qual posição se inicia essa subcadeia com menor número de caracteres distintos
7) retornar string de maior tamanho'''


primeiraString, segundaString = input('Digite uma string: '), input('Digite outra string: ')
subcadeia = ''

def retornarString(maiorString, menorString):
    for menorString in maiorString:
        return menorString



if len(primeiraString) > len(segundaString):
    print()
else:
    print()


