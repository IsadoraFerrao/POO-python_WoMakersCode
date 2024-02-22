# Escopo Global
variavel_global = 10

def minha_funcao():
    # Escopo Local
    variavel_local = 5
    print(variavel_global)  # Variável global acessível dentro da função
    print(variavel_local)

minha_funcao()
print(variavel_global)  # Variável global acessível fora da função
#print(variavel_local)  # Isso geraria um erro, pois variável_local não está acessível fora da função
