# %%

def f(x):
    resultado = 1 + x
    return resultado
# %%
f(10)

# %%

def juros_compostos(i:float,t:int,iv:float)->float:
    """juros_compostos serve para calcular o retorno financeiro a partir de um aporte.
    Deve-se considerar: 
    i:
        taxa 
    t:
        tempo
    iv:
        aporte inicial

    Ademais importante resaltar que taxa e tempo devem ser equivalentes, ex: se a taxa é ao mês, o período deve ser em meses.
    """

    return iv * t ** i

juros_compostos(i=4, t=1.13, iv=1000)

# %%
