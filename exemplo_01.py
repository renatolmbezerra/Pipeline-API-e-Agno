import requests

def extrair():
    """
    Extrai o preço atual do Bitcoin em reais.
    """
    # URL da API do Coinbase
    url = "https://api.coinbase.com/v2/prices/spot?currency=BRL"

    # Fazendo a requisição GET para a API
    response = requests.get(url)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Retornando o preço atual do Bitcoin em reais
        return response.json()["data"]["amount"]
    else:
        # Retornando None em caso de erro
        return None

def transformar():
    """
    Transforma o preço do Bitcoin em reais para um número float.
    """
    # Chamando a função extrair para obter o preço
    preco = extrair()

    # Verificando se o preço foi obtido com sucesso
    if preco is not None:
        # Convertendo o preço para float e retornando
        return float(preco)
    else:
        # Retornando None em caso de erro
        return None
    

print(extrair())  
