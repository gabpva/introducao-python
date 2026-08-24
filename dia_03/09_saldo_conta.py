trig = 0
saldo = 0

while trig == 0:

    entrada = input("Digite o saldo")
    try:
        entrada = float(entrada)
    except ValueError:
        pass
    if type(entrada) == float:
        saldo = saldo + entrada
    else:
        print(saldo)
        trig = trig + 1