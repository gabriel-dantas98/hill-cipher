import numpy
import unicodedata
import codecs
from scipy import linalg
from pprint import pprint


def get_value_alphabet(index):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", " "]
    return alphabet[index].upper()

def get_determinante_correspondente(determinante):
    default = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    inversed = [1, 9, 21 ,15, 3, 19, 7, 23, 11, 5, 17, 25]

    return inversed[default.index(determinante)]

def verify_value(value, MOD):

    if value > MOD:
        return abs(value) % MOD
    elif value < 0:
        return MOD - (abs(value) % MOD)
    return abs(value)

chave_origin = numpy.array([[1, 0, 0],
                            [1, 3, 1],
                            [1, 2, 0]])

# VALORES PARA TESTE
chave_test = numpy.array([[2, 4, 5],
                         [9, 2, 1],
                         [3, 17, 7]])

data_test = numpy.array([0, 19, 19])
########

              # SALVADORTMARENA    
criptograma = "SŢÕVŝØOƙóMŢÏEŰá"
MOD = 255

cood_criptograma_divided = [["S", "Ţ", "Õ"], ["V","ŝ","Ø"], ["O", "ƙ", "ó"], ["M", "Ţ", "Ï"], ["E", "Ű", "á"]]

#for i in criptograma:
#    print("Decimal: {} ORD: {} Hex: {}".format(int(hex(ord(i)), 16), ord(i), hex(ord(i))))
#    print("Decimal: {}".format(unicodedata.decimal(i)))

list_to_decimal = [ [ ord(value) for value in trios ] for trios in cood_criptograma_divided ]

print("Matriz em numeros decimais")
pprint(numpy.array(list_to_decimal))

list_to_hex = [ [ hex(ord(value)) for value in trios ] for trios in cood_criptograma_divided ]

#print("Matriz em hexa da palavra cifrada:")
#pprint(list_to_hex)


chave_inversa = [ [ j for j in i ]for i in numpy.linalg.inv(chave_origin)]

print("Chave inversa")
pprint(numpy.array(chave_inversa))

list_calculated = []
for line in list_to_decimal:
    list_calculated.append(numpy.matmul(chave_inversa, line))

print("Matriz calculada com a chave inversa")
pprint(list_calculated)

list_normalized = numpy.array([[ verify_value(value, MOD) for value in line ] for line in list_calculated])

print("Matriz calculada com a chave inversa normalizada com MOD")
pprint(list_normalized)


list_decimals = numpy.matrix.tolist(list_normalized)

decimal_values = [ ]
final_list= [ [decimal_values.append(str(round(char_list))) for char_list in line ] for line in list_decimals]

hex_final_list = [ hex(int(value)) for value in decimal_values]

unicode_char = [ chr(int(value)) for value in decimal_values]

index_alphabet_list = [ verify_value(int(value), 25) for value in decimal_values]

char_alphabet_list = [ get_value_alphabet(int(value)) for value in index_alphabet_list ]
#get_value_alphabet(int(value))

print("Valores decimais: ")
print(" ".join(decimal_values))

print("Valores hex: ")
print(" ".join(hex_final_list))


print("Valores char mod 255: ")
print(" ".join(unicode_char))


print("Valores char conveted mod 25 ")
print(" ".join(char_alphabet_list))

