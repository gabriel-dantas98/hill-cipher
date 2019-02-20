# Desafio Cybersecurity - 4ECA-D3 

Desafio proposto em aula foi decriptar um criptograma utilizando a Cifra de Hill.

### Instalando e executando
- Confira antes se você já possui o Python 3 e o PIP instalados em sua máquina.


Em seguida:
```
pip install -r requirements.txt
python3 cypher_hill.py
```


O criptograma foi:
#### SŢÕVŝØOƙóMŢÏEŰá

E a chave de criptografia foi:
```
[ 1 , 0 , 0 ] 
[ 1 , 3 , 1 ] 
[ 1 , 2 , 0 ]
```

Então seguimos o seguinte processo:
 
#### 1° Passo: 
- Já que estamos falando de uma Matriz 3x3 devemos dividir nosso criptograma em conjuntos de 3 caracteres, tendo assim:

```
["S", "Ţ", "Õ"]
["V", "ŝ", "Ø"]
["O", "ƙ", "ó"]
["M", "Ţ", "Ï"]
["E", "Ű", "á"]
```

#### 2° Passo:
- Uma vez que temos nossa matriz de caracteres agrupados, convertemos cada elemento por um valor decimal para que possamos realizar os calculos.
Nós utilizamos a função _ord()_ do Python para obter o valor decimal de um _char_.

```Python
decimal_agrouped_cryptogram = [ [ ord(value) for value in line ] for line in agrouped_cryptogram ]
```

#### 3° Passo:
- Para realizarmos a decriptação da mensagem precisamos da inversa da nossa matriz chave, para isso utilizamos uma função _linalg.env()_ do _numpy_ .

```Python
inverted_key = numpy.linalg.inv(origin_key)
```
#### 4° Passo:
- Com a nossa matriz chave inversa realizamos a multiplicação por **cada linha** da nossa matriz de criptogramas utilizando a função _matmutl_ do _numpy_ e geramos uma lista com os valores calculados.

```Python
list_calculated = []
for line in decimal_agrouped_cryptogram:
    # Multiplicação da matriz inversa com cada linha do criptograma decimal
    list_calculated.append(numpy.matmul(inverted_key, line))
```

#### 5° Passo:
- Agora que calculamos os nossos novos valores decimais, precisamos verificar se eles estão dentro do nosso intervalo possivel para conseguir decriptalos em carácteres novamente.
Para isso temos uma função _verify_value_() que verifica se o valor está dentro do intervalo ou seja ser de 0 a 255, tratando o valor caso esteja fora desse intervalo.
Com o resultado criamos uma nova matriz com todos os valores normalizados.

```Python
matrix_calculated_cryptogram = numpy.array( [ [ verify_value(value, _MOD) for value in line ] for line in list_calculated ])
```
#### 6° Passo:
- Com os valores decimais normalizados agora é só correr para o abraço! Ou seja, podemos encontrar os carácteres correspondentes para cada valor decimal.
Para conseguir isso, primeiro transformamos a matriz de valores em uma lista unidimensional utilizando a função _flatten().astype(numpy.int64)_.

```Python
# Transformamos a matriz em uma lista unidimensional
list_calculated_cryptogram = matrix_calculated_cryptogram.flatten().astype(numpy.int64)
```

#### 7° Passo:
- Para transformarmos a lista de valores decimais em carácteres e finalmente vermos a nossa frase decriptada usamos a função nativa do Python _chr()_ que recebe um valor decimal e retorna o seu carácter correspondente.
Em seguida para termos uma melhor visualização da frase usamos a função _join()_ para unirmos todos os carácteres da lista em uma unica string e sucesso!
Para saber o resultado execute o nosso script e veja! :D 
```Python
# Convertemos a lista de valores decimais decriptografados em uma lista de carácteres correspondentes 
list_char_cryptogram = [ chr(cryptogram) for cryptogram in list_calculated_cryptogram ]

# Convertemos a lista em uma única string ;)
decrypted_message_string = "".join(list_char_cryptogram) 
```










