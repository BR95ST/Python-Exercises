print("[1] adicao")
print("[2] subtracao")
print("[3] divisao")
print("[4] multiplicacao")
escolha = int(input())
while(escolha > 0 and escolha < 5):
    parcela1 = float(input())
    parcela2 = float(input())
    if escolha == 1:
        print(parcela1 + parcela2)
    elif escolha == 2:
        print(parcela1 - parcela2)
    elif escolha == 3:
        print(parcela1 / parcela2)
    elif escolha == 4:
        print(parcela1 * parcela2)
    escolha = int(input())
else:
    print("escolha errada")
