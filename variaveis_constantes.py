"""
Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer
da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com 
um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.
"""

age = 31
name = "Eduardo"
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')


#é possível também atribuir várias variáveis na mesma linha
#Assim também como é possível alterar o valor de uma vaiável
age, name = (32, 'Carlos')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')


"""
CONSTANTES
Assim como as variáveis, constantes são utilizadas para armazenar valores.
Uma contante nasce com um valor e permanece com ele até o final da execução do 
programa, ou seja, o valor é imutável.


PYTHON NÃO TEM CONSTANTES
Em python usamos a convenção que diz ao programador que a variável é uma constante.
Para fazer isso, você deve criar a variável com o nome todo em letras maíusculas:

"""
#Exemplos de constantes:

ABS_PATH = 'C:\Users\eduar\OneDrive\Área de Trabalho\Cursos de programação\DIO - Santander Bootcamp 2025 - Back-End com Python'
DEBUG = True
STATES = [
    'AL',
    'PE',
    'PB',
    'RN',
    'CE'
]

AMOUNT = 30.2

"""
Boas práticas

- O padrão de nomes deve ser snake case.
- Escolha nomes sugestivos.
- Nome de constantes todo em maíusculo.

"""

