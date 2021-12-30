from collections import Counter

ArrayA = ["A", "A", "B", "C", "C", "C", "D"]
# retorna um dict:
print(Counter(ArrayA))
# Retorna uma tupla:
print(Counter(ArrayA).most_common())
print(Counter(ArrayA).most_common(2))
