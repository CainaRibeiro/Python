n1,n2,n3 = int(input('n1: ')),int(input('n2: ')), int(input('n3: ')) 

numeros = [n1,n2,n3]
tamanhoLista = len(numeros)

numeros.sort(reverse=True)

print(tamanhoLista)

print('Maior: ', numeros[0], '\nIntermediário: ', numeros[1], '\nMenor: ',numeros[tamanhoLista-1])
