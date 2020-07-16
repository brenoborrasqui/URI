entrada = input()
entrada = entrada.split()
entrada = [int(i) for i in entrada]

print("{} eh o maior".format(max(entrada)))
