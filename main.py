# Define a função MMQ que implementa o método dos mínimos quadrados
def MMQ(x, y):
  # Calcula a quantidade de elementos nas listas x e y
  n = len(x)

  # Calcula a soma dos elementos das listas x e y
  soma_x = sum(x)
  soma_y = sum(y)

  # Calcula a soma dos quadrados dos elementos de x
  soma_x2 = sum([xi * xi for xi in x])

  # Calcula a soma dos produtos dos elementos correspondentes de x e y
  soma_xy = sum([xi * yi for xi, yi in zip(x, y)])

  # Cálculo da inclinação (m) e interceptação (b) da reta
  m = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
  b = (soma_y - m * soma_x) / n

  # Retorna a inclinação e a interceptação
  return (m, b)

# Define a função que imprime a equação da reta
def printarResultado (x, y, n_exercicio):
  # Chama a função MMQ para calcular a inclinação e a interceptação
  inclinacao, interceptacao = MMQ(x, y)
  print(f"Exercicio {n_exercicio}:")
  # Verifica se a interceptação é negativa para imprimir corretamente o sinal
  if interceptacao < 0:
    print("A equação da reta é: y = {:.2f}x - {:.2f}".format(inclinacao, abs(interceptacao)))
  else:
    print("A equação da reta é: y = {:.2f}x + {:.2f}".format(inclinacao, interceptacao))

# Exercício 1
# Define listas de pontos x e y
x1 = [1.0, 1.1, 1.3, 1.5, 1.9, 2.1]
y1 = [1.84, 1.96, 2.21, 2.45, 2.94, 3.18]

# Chama a função para imprimir o resultado para o primeiro conjunto de pontos
printarResultado(x1, y1, 1)

# Exercício 2
# Define outro conjunto de pontos x e y
x2 = [4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
y2 = [102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72]

# Chama a função para imprimir o resultado para o segundo conjunto de pontos
printarResultado(x2, y2, 2)


