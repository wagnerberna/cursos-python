# packing nomeado
# **kwargs (argumentos nomeados converte em dicionário)
# posicao : piloto
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f"{posicao} -> {piloto}")


resultado_f1(primeiro="Senna", segundo="Hamilton", terceiro="vettel")

# unpacking nomeado
def resultado2_f1(primeiro, segundo, terceiro):
    print(f"1 -> {primeiro}")
    print(f"2 -> {segundo}")
    print(f"3 -> {terceiro}")


podium = {"segundo": "Hamilton", "primeiro": "Senna", "terceiro": "vettel"}
# desempacota o dicionário e passa como param. nomeado.
resultado2_f1(**podium)
