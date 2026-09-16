# %%

arquivo = r"./exercício_extra/2026_EmendasParlamentares_PorDocumento.csv"

dados = []

with open(arquivo, encoding="latin1") as open_file:
    cabecalho = open_file.readline().strip().split(";")

    for linha in open_file:
        valores = linha.strip().split(";")

        registro = {}

        for i in range(len(cabecalho)):
            registro[cabecalho[i].strip('"')] = valores[i].strip('"')

        dados.append(registro)
# %%

emendas = {}

for registro in dados:
    codigo = registro["Código da Emenda"]

    empenhado = float(
        registro["Valor Empenhado"].replace(",",".")
    )

    pago = float(
        registro["Valor Pago"].replace(",",".")
    )

    if codigo not in emendas:
        emendas[codigo] = {}
        emendas[codigo]["empenhado"] = 0
        emendas[codigo]["pago"] = 0

    emendas[codigo]["empenhado"] += empenhado
    emendas[codigo]["pago"] += pago

# %%

for codigo in emendas:
    empenhado = emendas[codigo]["empenhado"]
    pago = emendas[codigo]["pago"]

    if empenhado > 0:
        execucao = (pago / empenhado) * 100
    else:
        execucao = None

    emendas[codigo]["execucao"] = execucao

# %%

maior_execucao = 0
maior_codigo = None

for codigo in emendas:
    execucao = emendas[codigo]["execucao"]

    if execucao is not None and execucao > maior_execucao:
        maior_execucao = execucao
        maior_codigo = codigo

print("Código:", maior_codigo)
print("Execução:", maior_execucao)