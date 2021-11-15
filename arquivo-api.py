import pip._vendor.requests
import json

while True:
    identi = input('Insira o código da moeda que você pretende converter (USD, EUR, etc.): ').upper()
    valreal = float(input('Insira a quantidade de dinheiro você possui, em R$: '))


    cotacoes = pip._vendor.requests.get("https://economia.awesomeapi.com.br/json/all")
    cotacoes = cotacoes.json()
    cotacao = float(cotacoes[identi]['bid'])

    print(' ')
    print('Cotação atual do {}: {:.2f}'.format(identi, cotacao))

    valabso = valreal/cotacao

    print('Convertendo R${:.2f} em {}, o valor total convertido fica: {} {:.3f}.'.format(valreal, identi, identi, valabso))
    print(' ')

    x = int(input('Gostaria de rodar o programa novamente? \n - Se sim, digite "1". \n - Se não, digite "2". \n'))
    if x == 2:
        break

