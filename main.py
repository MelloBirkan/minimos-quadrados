def MMQ(x, y):
  n = len(x)

  soma_x = sum(x)
  soma_y = sum(y)

  soma_x2 = sum([xi * xi for xi in x])
  soma_xy = sum([xi * yi for xi, yi in zip(x, y)])

  # Cálculo da inclinação (m) e interceptação (b)
  m = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
  b = (soma_y - m * soma_x) / n

  return (m, b)


# Exemplo de uso
x = [1.0, 1.1, 1.3, 1.5, 1.9, 2.1]
y = [1.84, 1.96, 2.21, 2.45, 2.94, 3.18]

m, b = MMQ(x, y)

print("A equação da reta é: y = {:.2f}x + {:.2f}".format(m, b))
