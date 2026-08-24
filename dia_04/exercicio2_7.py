estoque = {
    "Maçã": 1.5,
    "Banana": 2.75,
    "Uva": 1.9,
    "Pera": 1.25,
    "Laranja": 0.65,
    "Limão": 1.25,
    "Goiaba": 2.15,
    "Abacaxi": 3.2,
    "Jaca": 5.8
}

while True:
    escolha = input("0 - Escolher Fruta\t1 - Ver Frutas\t2 - Sair\t")
    if escolha == "2":
        break
    if escolha == "1":
        for i in estoque:
            print(i)
    if escolha == "0":
        fruta = input("Digite o nome da fruta\t")
        try:
            print("O valor da", fruta, "é: R$",estoque[fruta])
        except:
            print("Nome incorreto")
    else:
        print("Não é uma opção\t")