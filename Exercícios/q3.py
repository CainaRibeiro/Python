combustivel, distancia = int(input('Qual foi a quantidade de combustível gasto: ')), int(input('Qual foi a distância percorrida pelo automóvel: '))

consumo = distancia / combustivel

print('A distância percorrida foi ', distancia,'km, e o gasto de combustível foi de', combustivel, 'L, com isso, sabemos que a média de consumo é %.1f' %consumo, 'km/L')
