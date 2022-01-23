# data = {'Items': {'_id': 1, 'capability': 'cap1'}}
data = {'Items': [{'capability': 'cap1'}, {'capability': ''}]}
print('Testes:::')
teste = (data.get('Items'))
print(teste)
# print(teste.get('capability'))
# print(teste['capability'])

# for el in teste:
#     print('for')
#     print(el)

print('----testes---')

for user in teste:
    # print(user)
    # print(user.get('capability'))
    user['capability'] = user.get(
        'capability') if user.get('capability') else 'any'
    print('user:::')
    print(user)
