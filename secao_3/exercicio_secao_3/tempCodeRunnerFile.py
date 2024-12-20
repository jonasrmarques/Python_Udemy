try:
    horario = int(input("Digite a sua hora"))
    if(horario <= 11 and horario >= 0):
        print("Bom dia")
    elif(horario <= 17 and horario >= 12 ):
        print("Boa tarde")
    elif(horario <= 23 and horario >= 18):
        print("Boa noite")
    else:
        print("Digite uma hora válida")
except:
    print("Digite apenas a hora, somente a hora")