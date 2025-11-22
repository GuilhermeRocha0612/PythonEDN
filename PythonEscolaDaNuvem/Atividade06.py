"""
Atividade 06 - Práticos

Exercícios:
1 - Gera uma senha aleatória usando caracteres especiais; usuário informa o comprimento.
2 - Gera um perfil de usuário aleatório usando a API Random User Generator (exibe nome, email e país).
3 - Consulta informações de endereço a partir de um CEP usando a API ViaCEP (logradouro, bairro, cidade, estado).
4 - Consulta a cotação de uma moeda em relação ao BRL usando a AwesomeAPI (valor atual, máximo, mínimo, data/hora).

Observação: os exercícios que usam APIs requerem conexão com a internet e a biblioteca `requests`.
Se `requests` não estiver instalada, instale com: `pip install requests`.
"""

import random
import string
from datetime import datetime
import urllib.request
import urllib.error
import json
import ssl
import sys


def fetch_json(url: str, timeout: int = 10):
    """Busca uma URL e retorna o JSON decodificado.

    Lança Exception em caso de erro com mensagem legível.
    """
    try:
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(url, timeout=timeout, context=ctx) as resp:
            charset = resp.headers.get_content_charset() or 'utf-8'
            text = resp.read().decode(charset)
            return json.loads(text)
    except urllib.error.HTTPError as e:
        raise Exception(f"HTTP error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        raise Exception(f"URL error: {e.reason}")
    except Exception as e:
        raise Exception(str(e))


# 1 - Gerar senha aleatória
def gerar_senha(tamanho: int) -> str:
    if tamanho <= 0:
        return ""
    chars = string.ascii_letters + string.digits + string.punctuation
    # Garante variedade se o tamanho for suficiente
    if tamanho >= 4:
        senha = [random.choice(string.ascii_lowercase),
                 random.choice(string.ascii_uppercase),
                 random.choice(string.digits),
                 random.choice(string.punctuation)]
        senha += [random.choice(chars) for _ in range(tamanho - 4)]
        random.shuffle(senha)
        return ''.join(senha)
    else:
        return ''.join(random.choice(chars) for _ in range(tamanho))


# 2 - Perfil aleatório usando Random User Generator
def gerar_perfil_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        data = fetch_json(url)
        user = data.get('results', [{}])[0]
        nome = user.get('name', {})
        first = nome.get('first', '')
        last = nome.get('last', '')
        email = user.get('email', '')
        country = user.get('location', {}).get('country', '')
        full_name = f"{first} {last}".strip()
        print(f"Nome: {full_name}")
        print(f"Email: {email}")
        print(f"País: {country}")
    except Exception as e:
        print(f"Erro ao consultar Random User API: {e}")


# 3 - Consulta ViaCEP
def consultar_cep(cep: str):
    cep_limpo = ''.join(ch for ch in cep if ch.isdigit())
    if len(cep_limpo) != 8:
        print("CEP inválido. Digite 8 dígitos (com ou sem hífen).")
        return

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    try:
        data = fetch_json(url)
        if data.get('erro'):
            print("CEP não encontrado.")
            return

        logradouro = data.get('logradouro', '')
        bairro = data.get('bairro', '')
        localidade = data.get('localidade', '')
        uf = data.get('uf', '')

        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {localidade}")
        print(f"Estado: {uf}")
    except Exception as e:
        print(f"Erro ao consultar ViaCEP: {e}")


# 4 - Consulta cotação via AwesomeAPI
def consultar_cotacao(moeda_codigo: str):
    codigo = moeda_codigo.strip().upper()
    if not codigo:
        print("Código de moeda inválido.")
        return

    pair = f"{codigo}-BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{pair}"
    try:
        data = fetch_json(url)
        key = pair.replace('-', '')  # ex: USDBRL
        info = data.get(key)
        if not info:
            print("Moeda não encontrada na API (verifique o código).")
            return

        bid = info.get('bid')
        high = info.get('high')
        low = info.get('low')
        timestamp = info.get('create_date') or info.get('timestamp')

        print(f"Cotação {codigo}/BRL")
        print(f"Valor atual (bid): {bid}")
        print(f"Máximo (high): {high}")
        print(f"Mínimo (low): {low}")
        print(f"Última atualização: {timestamp}")
    except Exception as e:
        print(f"Erro ao consultar AwesomeAPI: {e}")


def main():
    print("Atividade 06 - Exercícios Práticos")

    # Exercício 1
    print("\n1 - Gerar senha aleatória")
    try:
        tamanho = int(input("Informe o tamanho da senha desejada: "))
    except ValueError:
        print("Entrada inválida. Usando tamanho padrão 12.")
        tamanho = 12

    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")

    # Exercício 2
    print("\n2 - Gerar perfil aleatório (Random User Generator)")
    gerar_perfil_aleatorio()

    # Exercício 3
    print("\n3 - Consulta de CEP (ViaCEP)")
    cep = input("Digite um CEP (ex: 01001-000): ")
    consultar_cep(cep)

    # Exercício 4
    print("\n4 - Consulta de cotação (AwesomeAPI)")
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
    consultar_cotacao(moeda)


if __name__ == '__main__':
    main()
