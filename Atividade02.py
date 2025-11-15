from time import sleep

#Conversor de Moedas 

print("Bem-vindo ao conversor de moedas!")
real = float(input("Digite o valor que deseja converter em Reais: R$ "))
escolhaDolarOuEuro = input("Você deseja converter para Dólares (D) ou Euros (E)? ").upper()

if escolhaDolarOuEuro == 'D':
    taxaCambioDolar = float(input("Digite a taxa de câmbio atual do Dólar (R$ por US$): "))
    dolares = real / taxaCambioDolar
    print(f"O valor em Dólares é: US$ {dolares:.2f}!")
elif escolhaDolarOuEuro == 'E':
    taxaCambioEuro = float(input("Digite a taxa de câmbio atual do Euro (R$ por €): "))
    euros = real / taxaCambioEuro
    print(f"O valor em Euros é: € {euros:.2f}!")
else:
    print("Opção inválida! Por favor, escolha 'D' para Dólares ou 'E' para Euros.")

# Calculadora de Descontos

sleep(4)

print("Vamos calcular o preço com desconto!")

nomeProduto = input("Digite o nome do produto: ")
precoOriginal = float(input("Digite o preço original do produto:(em R$) "))
percentualDesconto = float(input("Digite o percentual de desconto (%): "))
valorDesconto = (percentualDesconto / 100) * precoOriginal
precoComDesconto = precoOriginal - valorDesconto
print(f"O preço de {nomeProduto} com {percentualDesconto}% de desconto é R$ {precoComDesconto:.2f} !")

#Calculadora de Média Escolar 

sleep(5)

print("Vamos calcular a média escolar de um aluno!")

nomeAluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média do aluno {nomeAluno} é: {media:.2f} !")
if media >= 7.0:
    print("Parabéns! O aluno está aprovado.")
else:
    print("O aluno está reprovado. Melhor sorte na próxima vez!")

#Calculadora de Consumo de Combustível 

sleep(4)
print("Vamos calcular o consumo de combustível do seu veículo!")
distanciaPercorrida = float(input("Digite a distância percorrida (em km): "))
combustivelConsumido = float(input("Digite a quantidade de combustível consumido (em litros): "))
consumoMedio = distanciaPercorrida / combustivelConsumido
print(f"Durante a viagem de {distanciaPercorrida} km, o consumo médio foi de {consumoMedio:.2f} km/l !")