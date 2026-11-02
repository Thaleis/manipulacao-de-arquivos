with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()

aluno_atual = None
notas= []

for linha in linhas:
    linha = linha.strip()
    if not linha:
        continue

    if linha.endswith(":"):
        if aluno_atual and notas:
            media = sum(notas) / len(notas)
            if media > 7:
                status = 'Aprovado'
            elif media < 7 and media >= 5:
                status = 'Em recuperaçao'
            else:
                status = 'Reprovado'
            print(f"Media de {aluno_atual}: {media:.2f}. {status}")
        aluno_atual =linha[:-1]
        notas = []
    else:
        notas.append(float(linha))
if aluno_atual and notas:
    media = sum(notas) / len(notas)
    if media > 7:
        status = 'Aprovado'
        with open('aprovados.txt', 'w') as aprovado:
            aprovado.write(f'{aluno_atual}')
    elif media < 7 and media >= 5:
        status = 'Em recuperaçao'
        with open('exame.txt', 'w') as exame:
            exame.write(f'{aluno_atual}')
    else:
        status = 'Reprovado'
        with open('reprovados.txt', 'w') as reprovado:
            reprovado.write(f'{aluno_atual}')
    print(f"Media de {aluno_atual}: {media:.2f}. {status}")