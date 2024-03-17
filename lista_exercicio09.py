idade = int(input("Digite sua idade: "))
ano_trabalho = int(input("Digite quanto anos você você possui de tempo de serviço: "))

if idade >= 65 or ano_trabalho >= 30 or idade >= 60 and ano_trabalho >= 25:
    print("Pode aposentar")
else:
    print("Não pode se aposentar")