# Importa a biblioteca para fazer requisições HTTP
import requests

# URL da API
url = "http://localhost:3333/"

# Faz uma requisição GET
response = requests.get(url)

# Exibe o código de status da resposta
print(response.status_code)

# Exibe os cabeçalhos da resposta
# print(response.headers)

# Exibe o conteúdo em bytes
# print(response.content)

# Exibe a resposta como JSON (somente se a resposta for JSON)
print(response.json())

# Exibe a resposta como texto (HTML, JSON em texto, XML, etc.)
print(response.text)