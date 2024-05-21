alg = input('digite alguma coisa: ')

print(f'{alg} é numérico ?',alg.isnumeric()) #verifica se é numérico
print(f'{alg} é alfabético?', alg.isalpha()) # verifica se é alfabético
print(f'{alg} é alfanumérico?', alg.isalnum()) # verifica se é alfanumérico
print(f'{alg} está em maiúsculo?', alg.isupper()) # verifica se é maiúsculo 
print(f'{alg} está capitalizado?', alg.istitle()) # verifica se as letras iniciais estão em maiúculas
print(f'{alg} está em minúsculo?', alg.islower()) # verifica se as letras estão em maiúsculas
print(f'{alg} Tem muitos espaços?', alg.isspace()) # verifica se há espaços
