entrada = input()
entrada = entrada.split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

pi = 3.14159

print("TRIANGULO: {:.3f}".format((A * C) / 2))

print("CIRCULO: {:.3f}".format(pi * (C**2)))

print("TRAPEZIO: {:.3f}".format(((A + B) * C) / 2))

print("QUADRADO: {:.3f}".format(B**2))

print("RETANGULO: {:.3f}".format(A * B))
