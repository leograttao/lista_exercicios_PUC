numero = int(input("Digite um número para ver se é par ou ímpar: "))
p = numero%2 == 0

if p:
    print("É par")
    print(f"Se sobra {numero%2} é par")
else:
    print("É ímpar")
    print(f"Se sobra {numero%2} é ímpar")