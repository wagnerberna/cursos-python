# hashMap["chave"] - (Dict)

# Instanciando a classe Dict
employee_registry = {}

# Inserindo dados
# objeto[chave] = valor
employee_registry[14] = "Wagner"
employee_registry[23] = "Aline"
employee_registry[10] = "Cris"
employee_registry[9] = "Isa"
print(employee_registry)

# Alterando o nome do id 10
# objeto[chave] = novo_valor
employee_registry[9] = "Isadora"
print(f"Novo valor do id 10, após a atualização: {employee_registry[9]}")
