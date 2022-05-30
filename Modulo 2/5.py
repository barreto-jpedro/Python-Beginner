# 5. Escreva um programa Python para inserir um elemento no início de um determinado 
# DicionárioOrdenado. 
# DicionárioOrdenado original: 
# DicionárioOrdenado ([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')]) 
# Insira um elemento no início do referido DicionárioOrdenado: 
# DicionárioOrdenado atualizado: 
# DicionárioOrdenado ([('color4', 'Orange'), ('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')]) 


def adiciona_item_na_posicao_0_do_dicionario(original_dict, novo_item):
    dicionario_ordenado = {}    
    novo_item.update(original_dict)
    dicionario_ordenado = novo_item    
    return dicionario_ordenado


dicionario_original = {
    'color1':'Red',
    'color2': 'Green',
    'color3': 'Blue'
    }

novo_item_do_dicionario = {'color4':'Orange'}

dicionario_ordenado = adiciona_item_na_posicao_0_do_dicionario(dicionario_original,novo_item_do_dicionario)

print(dicionario_ordenado)