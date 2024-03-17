a = int(input("Digite o valor de A(Tem que ser diferente de 0): "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
formula = b**2-4*a*c

if formula > 0:
    print("Existem duas raizes positivas")
elif formula == 0:
    print("Existem duas raizes reais iguais")
else:
    print("Existem duas raizes imaginarias conjugadas")