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

# Função para calcular os ângulos do triângulo usando a Lei dos Cossenos
def calcular_angulos(a, b, c):
    angulo_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angulo_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angulo_C = 180 - angulo_A - angulo_B  # A soma dos ângulos internos é sempre 180°
    return angulo_A, angulo_B, angulo_C

# Função para identificar o tipo de triângulo com base nos ângulos
def tipo_triangulo_angulos(angulo_A, angulo_B, angulo_C):
    if 90 in (round(angulo_A), round(angulo_B), round(angulo_C)):
        return "Retângulo"
    elif all(angulo < 90 for angulo in (angulo_A, angulo_B, angulo_C)):
        return "Acutângulo"
    else:
        return "Obtusângulo"

#Pergunta para saber os lados.
while True:
    try:
        pergunta_lados = int(input("Quantos lados tem a sua forma geométrica? 3, 4 ou 0? "))
        if pergunta_lados in [0, 3, 4]:
            break  # Entrada válida, sai do loop
        else:
            print("Por favor, insira 0, 3 ou 4.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

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
    while True:
        try:
            A = float(input("Qual o tamanho do lado A? "))
            B = float(input("Qual o tamanho do lado B? "))
            C = float(input("Qual o tamanho do lado C? "))
            if A > 0 and B > 0 and C > 0:
                break  # Se todos os valores forem positivos, o loop é encerrado
            else:
                print("Os lados do triângulo precisam ser valores maiores que zero.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

    if validar_triangulo(A, B, C):  # Usando a função para validar o triângulo
        perimetro = A + B + C
        print("Sua forma é um triângulo!")
        print(f"O Perímetro é {perimetro:.1f}")
        
        # Identificando o tipo de triângulo pelos lados
        tipo_triangulo = identificar_triangulo(A, B, C)
        print(f"Esse triângulo é {tipo_triangulo}")

        # Calculando e exibindo a área
        area_triangulo = calcular_area_triangulo(A, B, C)
        print(f"A área do triângulo é {area_triangulo:.2f}")

        # Calculando e exibindo os ângulos
        angulo_A, angulo_B, angulo_C = calcular_angulos(A, B, C)
        print(f"Os ângulos do triângulo são: A = {angulo_A:.2f}, B = {angulo_B:.2f}, C = {angulo_C:.2f}")

        # Identificando o tipo de triângulo pelos ângulos
        tipo_angulos = tipo_triangulo_angulos(angulo_A, angulo_B, angulo_C)
        print(f"O triângulo é {tipo_angulos}")
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