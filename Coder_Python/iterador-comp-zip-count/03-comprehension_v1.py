# comprehension []
# expressão extendida
dobro_ex = []
for i in range(10):
    dobro_ex.append(i * 2)
print(dobro_ex)

# [expressão + for item in list]
dobro = [i * 2 for i in range(10)]
print(dobro)


# [expressão + for item in list + condição ]
dobro_par = [i * 2 for i in range(10) if i % 2 == 0]
print(dobro)


