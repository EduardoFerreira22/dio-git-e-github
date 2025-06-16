"""
Em alguns momentos é necessário converter o tipo de uma variável para manipular de forma diferente.
Por exemplo:
Variáveis do tipo string, que armazenam números e precisamos fazer algumas operações matemáticas
com esse valor.
"""

#Valor inteiro
preco = 10
print(preco)
#10


# Valor sendo convertido para número float
preco = float(preco)
print(preco)
#10.0

# Quando faço uma divisão o valor é retornado já convertido como float
preco = 10 / 2
print(preco)
#5.0

#Convertendo Strings para números
preco = "10.50"
idade = "31"

print(float(preco))
# 10.50

print(int(idade))
# 31