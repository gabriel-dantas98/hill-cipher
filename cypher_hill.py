import numpy
import unicodedata
import codecs
from scipy import linalg
from pprint import pprint

def verify_value(value, MOD):
    if value > MOD:
        return abs(value) % MOD
    elif value < 0:
        return MOD - (abs(value) % MOD)
    return abs(value)

# Matriz chave para criptografia
origin_key = numpy.array([[1, 0, 0],
                          [1, 3, 1],
                          [1, 2, 0]])
# Criptograma 
cryptogram = "SŢÕVŝØOƙóMŢÏEŰá"

# MOD é a quantidade da valores presentes ta tabela Unicode
_MOD = 255

print("Nosso criptograma: {}".format(cryptogram))

# Criptograma agrupado em grupos de 3 carácteres
agrouped_cryptogram = [["S", "Ţ", "Õ"],
                       ["V", "ŝ", "Ø"], 
                       ["O", "ƙ", "ó"],
                       ["M", "Ţ", "Ï"],
                       ["E", "Ű", "á"]]

print("\nCriptograma seguimentado de acordo com a nossa matriz: ")
pprint(agrouped_cryptogram)

# Inline For para conversão de cada caractere em um valor decimal correspondente
# Onde line é a linha da matriz e value é cada valor indivual da linha da matriz
decimal_agrouped_cryptogram = [ [ ord(value) for value in line ] for line in agrouped_cryptogram ]

print("\nMatriz criptograma convertida em valores decimais: ")
pprint(decimal_agrouped_cryptogram)

# Obtendo inversa da matriz chave atraves da função linalg.inv() do numpy
inverted_key = numpy.linalg.inv(origin_key)

print("\nMatriz chave inversa:")
pprint(inverted_key)
 
list_calculated = []
for line in decimal_agrouped_cryptogram:
    # Multiplicação da matriz inversa com cada linha do criptograma decimal
    list_calculated.append(numpy.matmul(inverted_key, line))

# Convertemos a lista em uma Matriz do Numpy
matrix_calculated_cryptogram = numpy.array( [ [ verify_value(value, _MOD) for value in line ] for line in list_calculated ])

print("\nMatriz criptograma multiplicada pela matriz inversa:")
pprint(matrix_calculated_cryptogram)

# Transformamos a matriz em uma lista unidimensional
list_calculated_cryptogram = matrix_calculated_cryptogram.flatten().astype(numpy.int64)

print("\nLista unidimensinal dos valores decimais dos criptogramas calculados:")
pprint(list_calculated_cryptogram)

# Convertemos a lista de valores decimais decriptografados em uma lista de carácteres correspondentes 
list_char_cryptogram = [ chr(cryptogram) for cryptogram in list_calculated_cryptogram ]

print("\nLista dos carácteres transformados de decimais para char's ou seja unicode:")
pprint(list_char_cryptogram)

# Convertemos a lista em uma única string ;)
decrypted_message_string = "".join(list_char_cryptogram) 

print("\nNossa mensagem decriptografada: {}".format(decrypted_message_string))
