p1 = input()
p2 = input()

p1 = [float(i) for i in p1.split()]
p2 = [float(i) for i in p2.split()]

print("{:.4f}".format(((((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2)))**(1 / 2)))
