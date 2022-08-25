from testes.questao1 import isNumber


numero1, numero2 = int(input("Escolha um número: ")), int(input('Escolha outro número:'))


def testeLogico(numero, idade):
    if(numero > idade):
        return True
    else:
        return False

def funcaoTeste(numero, idade):
    if testeLogico(numero, idade) == True:
        print('Teste deu positivo')
    else:
        print('Teste deu merda')

print(funcaoTeste(numero1, numero2))



n1 = float(50.5124142)

print('Esse número vai sair com duas casas decimais %.2f' % n1)

