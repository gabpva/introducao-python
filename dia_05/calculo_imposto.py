#%%
def calc_imposto(preco:float, tx_base: float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

# %%

imposto_geral = {
    "municipio": 0.01,
    "estadual": 0.005,
    "federal": 0.001
}

#%%
print(calc_imposto(100, 0.03, municipio=0.01, estadual=0.005, federal=0.001))

print(calc_imposto(100, 0.03, **imposto_geral))
