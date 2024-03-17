temperatura = int(input("Qual a temperatura neste momento(em Celsius)? "))

if temperatura < 15:
    print("Está frio !!")
elif temperatura > 25:
    print("Está calor !")
else:
    print("Temperatura agradável !")