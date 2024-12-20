#PEGAR A MÉDIA DE 3 ALUNOS, EM LOOP

contador = 1
notas = []


while contador <= 3:
    try:
        nota = int(input("Digite sua nota: "))
        
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            contador+=1
            
        else:
            print("Digite um valor correto")
        
        
    except:
        print("digite um valor correto")
        
    
        
media = sum(notas) / len(notas)
print(f"Sua média é: {media}")