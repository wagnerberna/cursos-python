from unicodedata import normalize

name = ' Wágner Bérnâ '

clean_name = name.lower().strip()
clean_name = normalize('NFKD', clean_name).encode('ASCII', 'ignore').decode('utf-8')

print(clean_name)
