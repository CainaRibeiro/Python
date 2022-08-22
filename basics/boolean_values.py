print('Valores booleanos são os que retornam True ou False\n')

print(10 > 9)
print(10 < 9)
print(10 == 9)

print('\nA condicional if, retorna valores True(se o parâmetro for verdadeiro) ou False(se não for verdadeiro)\n')

a, b = 200, 10;

if a < b:
    print('retorna True\n')
else:
    print('retorna False\n')

print('\nA função bool() retornar valores booleanos para strings, números, listas e tuples. No entanto poucos valores vão receber False. No caso dos números, apenas o 0 retorna false. Apenas strings vazias retornam False e o mesmo acontece com listas e tuples\n')

print(bool('abc'), bool(1), bool(['abc', 'efg']), bool(''), bool(0), bool([]), bool({}), bool(()))

print('\nFunções podem retornar valores booleanos\n')

def funcaoTeste():
    return True

print(funcaoTeste())

print('\nVocê pode usar como parâmetro de uma condicional, uma função que retorne valores booleanos\n')

if funcaoTeste():
    print('retornou true')
else:
    print('retornou false')