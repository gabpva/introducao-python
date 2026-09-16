# %%%
import json
import requests
from tqdm import tqdm
# %%

ceps = [
    "85603388",
    "85601260",
    "01519000",
    "21870370",
    "58038200"
]

url = "https://viacep.com.br/ws/{cep}/json/"

dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())
dados

# %%
print(dados)

with open("ceps.json","w", encoding="utf-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

print("fim")