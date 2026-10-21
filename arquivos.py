media = 0
print("Digite a quantidade de alunos da turma")
alunos = int(input("- "))

for i in range(alunos):
     while True:
                print(f"{ i + 1}° aluno, digite seu nome:")
                n1 = input("- ")
                with open("notas.txt", "w") as nome:
                    nome.write(f"{n1}\n")                
                print("Digite sua nota 1:")
                n1 = float(input("- "))
                with open("notas.txt", "a") as nota:
                    nota.write(f"{n1}\n")
                print("Digite sua nota 2:")
                n2 = float(input("- "))
                with open("notas.txt", "a") as nota:
                    nota.write(f"{n2}\n")
                print("Digite sua nota 3:")
                n3 = float(input("- "))
                with open("notas.txt", "a") as nota:
                    nota.write(f"{n3}\n")
                with open("notas.txt", "r") as notas:
                    for nt in notas:
                        media = 0
                        media = media + nt
                    media_final = media / 3
                    with open("notas.txt", "w") as nome:
                                        nome.write(f"{n1}\n")  
                print(f"Média final:{media_final: .2f}.")
                if media_final >= 7:
                    print("Parabéns, você foi aprovado.")
                    with open("aprovados.txt", "a") as aprovado:
                        aprovado.write(f"{media_final}\n")
                elif media_final < 7 and media_final >= 5:
                    print("Você está em prova final, boa sorte.")
                    with open("medias.txt", "a") as media:
                        media.write(f"{media_final}\n")
                elif media_final < 5:
                    with open("reprovados.txt", "a") as reprovado:
                        print("Infelizmente você foi reprovado")
                        reprovado.write(f"{media_final}\n")
                break

       

            


            



           


    
