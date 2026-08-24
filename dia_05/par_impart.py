numero = float(input("Informe o número que deseja descobrir se é par ou impar\t"))

def par_impar(x:float)->str:
    if x % 2 == 0:
        return "Par"
    else:
        return "Impar"

print("O numero", numero, "é:", par_impar(numero))