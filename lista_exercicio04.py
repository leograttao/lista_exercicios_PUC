media = int(input("Qual foi sua media? "))

if media >= 7:
    print("Estudante aprovado")
elif media >= 4 and media < 7:
    print("Estudante em recuperação")
else:
    print("Estudante reprovado")