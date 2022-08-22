print('\n Em python, strings são arrays, então é possível selecionar uma única parte através do método abaixo \n')

a = 'Hello, world!'

print(a[1]);

print('\n Já que strings são arrays, pode-se então utilizar o for em uma string \n');

b = 'banana';

for b in 'banana':
    print(b)

print('\n Para descobrir o length de uma string, pode-se utilizar a função len() \n')

c = 'Loucura com doidera'

print(len(c));

print('\n Você pode verificar se existe uma determinada palavra dentro de uma string através do método IN \n');

d = 'textao de loucura com doidera'

print('textao' in d); #O retorno será um valor booleano (true or false)

print('\n Você pode criar condicionais caso haja uma determinada palavra no texto \n')

if 'textao' in d:
    print('\nsim, textao está presente\n');

print('\nVocê pode também verificar se uma determinada palavra NÃO  está presente em uma string\n')

if 'texto' not in d:
    print('texto, NÃO está presente em d');

print('\n Você pode tirar uma parte da string utilizando o método de SLICING\n');

print(d[0:6]);

print('\n slice a partir do início\n');

print(d[:6]);

print('\nSlice até o final\n')

print(d[1:])

print('\nPara selecionar ao contrário, basta utilizar o índice negativo\n');

print(d[-8:-1]);

print('\nÉ possível modificar as string, tanto para uppercase quanto para lowercase\n');

e, f = 'tudo lowercase', 'TUDO UPPERCASE';

print(e.upper(), f.lower());

print('\na função strip() retira todo espaço em branco desnecessário presente em uma string\n');

g = '\n    esse texto tem espaço desnecessário    ';

print(g);
print(g.strip());

print('\nVocê pode trocar uma letra ou palavra em uma string através da função replace()\n');

h = '\nEssa odeio python\n';

print(h.replace('odeio', 'amo'));

print('\n A função split() é capaz de dividir uma string em substrings, retornando uma lista\n');

i = 'Esse texto , será dividido , onde existe , vírgula';

print(i.split(','))

print('\n Concatenção de strings\n')

print(a + ' ' + c);

print('\nEm python, não podemos combinar números com string de qualquer forma, para isso, utilizamos a função format\n')

j, k = 999, '\nEssa string vai receber um número através da função format() bem aqui {}'

print(k.format(j))

print('\nA função format não tem número limitado de argumentos, mas tem que se atentar a ordem dos mesmos\n')

idade, anoNascimento, diaNascimento = 26, 1996, 20;

l = '\nEu sou Cainã, tenho {} anos, nasci em {} em {} de janeiro\n'

print(l.format(idade, anoNascimento, diaNascimento));

print('\nVocê pode númerar os argumentos para garantir que os mesmo recebam a posição correta\n')

m = '\nEu sou Cainã, tenho {2} anos, nasci em {0} em {1} de janeiro\n'

print(m.format(anoNascimento, diaNascimento, idade));

'''Para acessar mais métodos de strings => https://www.w3schools.com/python/python_strings_methods.asp'''