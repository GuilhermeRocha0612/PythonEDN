"""
Atividade 05 - Quatro exercícios

1 - Função que calcula a gorjeta com base no valor da conta e porcentagem.
2 - Verificador de palíndromo (ignora espaços e pontuação). Retorna "Sim" ou "Não".
3 - Calcula desconto e preço final, formata para 2 casas e interage com o usuário.
4 - Calcula quantos dias um indivíduo está vivo a partir da data de nascimento.
"""

from datetime import date, datetime


# 1 - Calcular gorjeta
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100.0)


# 2 - Verificar palíndromo
def eh_palindromo(texto: str) -> bool:
    # Normaliza: remove caracteres não alfanuméricos e transforma em minúsculas
    s = ''.join(ch.lower() for ch in texto if ch.isalnum())
    return s == s[::-1]


# 3 - Cálculo de desconto e preço final
def calcular_desconto(valor: float, porcentagem_desconto: float) -> float:
    return valor * (porcentagem_desconto / 100.0)


def preco_final(valor: float, porcentagem_desconto: float) -> float:
    desconto = calcular_desconto(valor, porcentagem_desconto)
    return valor - desconto


# 4 - Quantos dias vivo
def dias_vivo(data_nascimento: date, hoje: date = None) -> int:
    if hoje is None:
        hoje = date.today()
    delta = hoje - data_nascimento
    return delta.days


def main():
    print("Atividade 05 - Exercícios")

    # Exercício 1 - Gorjeta
    print("\n1 - Calculadora de gorjeta")
    try:
        valor = float(input("Valor total da conta (ex: 120.50): "))
        perc = float(input("Porcentagem de gorjeta desejada (ex: 10 para 10%): "))
    except ValueError:
        print("Entrada inválida. Use números (ex: 120.50 e 10).")
    else:
        gorjeta = calcular_gorjeta(valor, perc)
        print(f"Gorjeta (R$): {gorjeta:.2f}")

    # Exercício 2 - Palíndromo
    print("\n2 - Verificador de palíndromo")
    texto = input("Digite uma palavra ou frase: ")
    if eh_palindromo(texto):
        print("Sim")
    else:
        print("Não")

    # Exercício 3 - Desconto e preço final
    print("\n3 - Cálculo de desconto e preço final")
    try:
        preco = float(input("Preço do produto (ex: 59.90): "))
        perc_desconto = float(input("Porcentagem de desconto (ex: 15 para 15%): "))
    except ValueError:
        print("Entrada inválida. Use números para preço e porcentagem.")
    else:
        valor_desconto = calcular_desconto(preco, perc_desconto)
        novo_preco = preco_final(preco, perc_desconto)
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Preço final após desconto: R$ {novo_preco:.2f}")

    # Exercício 4 - Dias vivo
    print("\n4 - Quantos dias você está vivo")
    print("Informe sua data de nascimento.")
    print("Formato aceito: DD/MM/AAAA (ex: 21/11/1990)")
    data_str = input("Data de nascimento: ")
    try:
        dt = datetime.strptime(data_str, "%d/%m/%Y").date()
        hoje = date.today()
        if dt > hoje:
            print("Data de nascimento não pode ser no futuro.")
        else:
            dias = dias_vivo(dt, hoje)
            anos = dias // 365
            print(f"Você está vivo(a) há {dias} dias (~{anos} anos).")
    except ValueError:
        print("Data inválida. Use o formato DD/MM/AAAA.")


if __name__ == "__main__":
    main()
