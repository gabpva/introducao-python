def soma(a:float, b:float, *args)->float:
    valores = [a, b] + list(args)
    return sum(valores)

print(soma(11,1,1,2,2,2,2,2,3,3,12,4,1234,12,431,23,1))
