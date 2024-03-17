idade = int(input("Qual sua idade(anos)? "))
peso = float(input("Qual o seu peso(kg)? "))

if idade > 15 and peso <= 120:
    print("Você está  liberado a andar na montanha russa")
elif idade <= 15 and peso > 120:
    print("Você está proibido a andar na montanha russa")
    