print("Se você estuda na PUCPR digite - 1\nSe vocÊ estuda na UNICAMP digite - 2")

universidade = int(input("Em qual universidade você estuda? "))
n1 = float(input("Qual foi sua nota na matéria 1? "))
n2 = float(input("Qual foi sua nota na matéria 2?"))
media = (n1+n2)/2

if universidade == 1 and media >= 7:
    print("Aprovado")
elif universidade == 1 and 4 <= media < 7:
    print("Em exame")
elif universidade == 1 and media < 4:
    print("Reprovado")

if universidade == 2 and media >= 5:
    print("Aprovado")
elif universidade == 2 and media < 5:
    print("Em exame")