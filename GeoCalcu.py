import math #Estou importando a biblioteca

# Função para calcular a área e circunferência de um círculo
def calcular_circulo(raio):
    area = math.pi * (raio ** 2)
    circunferencia = 2 * math.pi * raio
    return area, circunferencia

# Função para validar se os lados formam um triângulo
def validar_triangulo(a, b, c):
    return (a + b > c) and (b + c > a) and (c + a > b)

# Função para identificar o tipo de triângulo
def identificar_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or c == a:
        return "Isósceles"
    else:
        return "Escaleno"

# Função para calcular a área de um triângulo com base nos lados (fórmula de Herão)
def calcular_area_triangulo(a, b, c):
    s = (a + b + c) / 2  # Calcula o semiperímetro
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Fórmula de Herão
    return area

#Pergunta para saber os lados.
pergunta_lados = int(input("Quantos lados tem a sua forma geometrica? 3, 4 ou 0? "))

#Circulo
if pergunta_lados == 0:
    pergunta_A = input("Sua forma é redonda? sim? ").strip().lower() # é para garantir que a entrada vai ser informada corretamente, não importa como se escreva
    if pergunta_A == 'sim':
        print("Você tem um circulo como forma!")
        raio = float(input("Qual o raio do círculo? "))
        # Usando a função para calcular
        area_circulo, circunferencia = calcular_circulo(raio)
        print(f"A área do círculo é {area_circulo:.2f} e a circunferência é {circunferencia:.2f}")

#Triangulo
elif pergunta_lados == 3:
    A = float(input("Qual o tamanho do lado A? "))
    B = float(input("Qual o tamanho do lado B? "))
    C = float(input("Qual o tamanho do lado C? "))

    if validar_triangulo(A, B, C):  # Usando a função para validar o triângulo
        perimetro = A + B + C
        print("Sua forma é um triângulo!")
        print(f"O Perímetro é {perimetro:.1f}")
        tipo_triangulo = identificar_triangulo(A, B, C)  # Identificando o tipo de triângulo
        print(f"Esse triângulo é {tipo_triangulo}")

        # Calculando e exibindo a área
        area_triangulo = calcular_area_triangulo(A, B, C)
        print(f"A área do triângulo é {area_triangulo:.2f}")
    else:
        print("Os valores fornecidos não formam um triângulo válido.")

#retangulo ou quadrado
elif pergunta_lados == 4:
    largura = float(input("Qual a largura? "))
    comprimento = float(input("Qual o comprimento? "))
    perimetro2 = 2*(largura+comprimento)
    print(f"Você tem um retângulo de perimetro {perimetro2:.1f}")
    if largura == comprimento:
        print("Todos os lados são iguais. Você tem um quadrado!")
#Isso aqui é para informar o usuario sobre um número invalido.
else:
    print("Esse número é invalido, tente os informados!!!")