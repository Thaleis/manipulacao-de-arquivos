while True:
    print("Aluno, digite seu nome:")
    nome = input("- ")
    print("Aluno, digite sua primeira nota:")
    nota1 = input("- ")
    print("Aluno, digite sua segunda nota:")
    nota2 = input("- ")
    print("Aluno, digite sua terceira nota:")
    nota3 = input("- ")
    with open("notas.txt", "a") as dados:
        dados.write(f"{nome}: \n {nota1} \n {nota2} \n {nota3} \n")
