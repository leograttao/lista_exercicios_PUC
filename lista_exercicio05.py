print("Homem digite 1\nMulher digite 2")
sexo = int(input("Qual o seu sexo? "))
h = float(input("Qual sua altura? "))
peso_ideal_homens = (72.7*h)-58
peso_ideal_mulher = (62.1*h)-44.7

if sexo == 1:
    print(f"Seu peso ideal é {peso_ideal_homens}")
elif sexo == 2:
    print(f"Seu peso ideal é {peso_ideal_mulher}")