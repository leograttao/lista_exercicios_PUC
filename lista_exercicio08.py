idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não é eleitor")
elif idade >= 16 and idade < 18 or idade > 65:
    print("Eleitor facultativo")
elif idade >= 18 and idade <= 65:
    print("Eleitor obrigatório")
