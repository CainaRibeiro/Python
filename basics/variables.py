print("\nNo python não tem comando para adicionar uma variável\n");

x = 5;

print(x);

print("\nAs variáveis não precissam ser declaradas com algum type específico, o proprio python identifica o type da variável\n");

n = 1;
nome = 'cainã';
media = 3.5;

print(type(n));
print(type(nome));
print(type(media));

print("\nCasting... Caso queira identificar um type específico para uma variável, basta utilizar o CASTING\n");

n1 = float(1);
name = str('caina');
z = int(50);

print(n1);
print(name);
print(z);

print("\nVariáveis são case-sensitive\n");

a = 1;
A = 2;

print(a);
print(A);

print('\nVocê pode adicionar variás variáveis em uma única linha, economizando espaço no código\n');

q, w, e = 'variavel 1', 'variável 2', 3;

print(q);
print(w);
print(e);

print('\nVocê pode atribuir variáveis a itens de uma list ou tuple\n');

frutas = ['maça', 'banana', 'mongo'];

r, t, y = frutas;

print(r);
print(t);
print(y);

print('\nVocê pode utilizar o print para mostrar a saída de informações no python. A função print pode também ser utilizada para demonstrar a saída de diversas variáveis de uma só vez\n');

print(r, t, y);

print('\nVariáveis que estão fora de funções são chamadas de variáveis globais\n');

p = 'toscão';

def variavelGlobal():
    p = 'maneirão'
    print('\npython é ' + p + '\n');

variavelGlobal()

print('\nVocê pode adicionar uma variável local dentro de uma função usando o mesmo nome de uma variável global, o valor da variável só será alterado dentro da função, sendo que a global manterá seu valor original fora da função\n');

print('\n python é ' + p + '\n');

print('\n Você pode transformar uma variável local em global através da keyword global \n');

def localToGlobal():
    global o
    o = 'Esquisito'

localToGlobal()

print('\n Iago é ' + o);