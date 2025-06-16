"""
A função  builtin input é utilizada quando queremos ler dados de entrada 
padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para
o usuário na saída padrão (tela). A função lê a entrada, converte para string
e retorna o valor.
"""

nome = input("Iforme o seu nome: ")
idade = input("Informe a sua Idade: ")

print(nome, idade) #Imprime o valor das variáveis no termianl

#com o end= é possível atribuir algo à finalização do print e \n faz uma quebra de linha
print(nome, idade, end='...\n')

#Sep= permite adicionar alguma coisa à os espaços em branco entre as palavras.
print(nome,idade, sep='_')

# O print por padrão já adiciona a quebra de linha