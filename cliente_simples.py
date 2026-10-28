import requests

url = "http://127.0.0.1:8000/saudacao"

dados = {"nome": input("Seu nome: ")}
resposta = requests.post(url, json=dados)
print(resposta.status_code)

print(resposta.json()["mensagem"])

url2 = "http://127.0.0.1:8000/dobro"
n = float(input("Numero: "))
r = requests.post(url2, json={"numero": n})
print(r.json()["resultado"])