# %%

nome_arquivo = "/home/gabpva/projects/cursos/teomewhy/introdução-python/dia_07/historia.txt"

open_file = open(nome_arquivo)

print(open_file)
# %%

conteudo = open_file.read()
print(conteudo)
# %%

open_file.close()


# %%

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
# %%
print(conteudo)
# %%
