# %%

nome_arquivo = "historia_02.txt"

txt = "usususuususususu"

with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)
# %%

txt = "conteudo adicional"

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)
# %%
