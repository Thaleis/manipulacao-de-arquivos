def leitura():
    print("Aluno, digite seu nome:")
    nome = input("- ")
    print(f"{nome}, digite sua primeira nota:")
    nota1 = input("- ")
    print(f"{nome}, digite sua segunda nota:")
    nota2 = input("- ")
    print(f"{nome}, digite sua terceira nota:")
    nota3 = input("- ")
    with open("notas.txt", "a") as dados:
        dados.write(f"{nome}: \n {nota1} \n {nota2} \n {nota3} \n")
    with open("notas.txt", "r") as leitura:
        ler = leitura.read()
        print(ler)


with open("notas.txt", "w") as esvaziar:
        esvaziar.write("")
print("Digite a quantidade de alunos da turma")
qtd_alunos = int(input("-"))
for i in range(qtd_alunos):
    leitura()