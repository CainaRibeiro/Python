print('\nO python usa diversos operadores e não vou listar todos. O link abaixo fornecerá informação mais detalhada\n')

print('https://www.w3schools.com/python/python_operators.asp\n')

a, b, c, d, e = 20, 15, 40, 50, 20

print('\nAdição =>', (a + b), '\nSubtração =>', (a - b), '\nMultiplicação =>', (a * b), '\nDivisão =>', (a / b), '\nMódulo =>', (a % b), '\nExponenciação =>', (a ** b), '\nFloor division =>', (a // b))

print('\nOperadores de comparação\n')

print('\nIgual =>', (a==b), '\nDiferente(not equal) =>', (a != b), '\nMaior que =>', (a > b), '\nMenor que', ( a < b), '\nMaior ou igual a =>', (a >= b), '\nMenor ou igual =>', (a <= b))

print('\nOperadaores lógicos\n')

print('\nAND, retorna TRUE se todos os valores forem TRUE\n')

if a > b and b < c:
    print('Se TODOS forem verdades, então essa string será retornada\n')
else:
    print('senão, essa será retornada\n')

print('\nOR, retorna true se ALGUM dos parâmetros forem true\n')

if a < b or d > c:
    print('É necessário apenas um parâmetro verdadeiro para retornar true\n')
else:
    print('Caso todos forem False, então essa string será retornada\n')

print('NOT, reverte o resultado dos parâmetros, true vira false, false vira true\n')

if not(a > b and b < c):
    print('Se TODOS forem verdades, então essa string será retornada\n')
else:
    print('senão, essa será retornada(Essa string só foi retornada devido ao NOT no início do parâmetro)\n')

print('Operador de identidade\n')

print('IS retorna TRUE se os duas variáveis forem do mesmo objeto, enquanto IS NOT retorna TRUE se as duas variáveis não forem do mesmo objeto\n')

print(a is b, a is e, a is not b)

print('\nMembership Operators, é usado para testar se uma determinada saquência está presente em um objeto\n')

f, g, h = 'Python é loucura com doidera', 'doidera', '30'

print(g in f)#O primeiro caso retorna TRUE porque doidera está presente na variável f 
print(h not in f)#No segundo caso retorna TRUE porque 30 NÃO está presente na variável f