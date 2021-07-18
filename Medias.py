Boletim = []
while True:
    AlunosReprovados = 0
    AlunosExame = 0
    AlunosAprovados= 0
    MeninosAprovados = 0
    MeninasAprovadas = 0
    MeninosExame= 0
    MeninasExame= 0
    MeninosReprovados = 0
    MeninasReprovadas = 0
    nome = str(input("Insira um nome: ")).strip().upper()
    sexo = str(input("Insira seu sexo [M/F]: ")).strip().upper()

    while sexo != 'M' and sexo != 'F':
        print('Sexo Inválido')
        sexo = str(input("Corriga o Sexo Informando M ou F: ")).strip().upper()

    nota1 = float(input("Insira a nota 1: "))
    while nota1 < 0 or nota1 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota1 = float(input("Insira a nota 1: "))

    nota2 = float(input("Insira a nota 2: "))
    while nota2 < 0 or nota2 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota2 = float(input("Insira a nota 2: "))

    nota3 = float(input("Insira a nota 3: "))
    while nota3 < 0 or nota3 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota3 = float(input("Insira a nota 3: "))

    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        status = "Aprovado"
    elif media < 7 and media >= 4:
        status = "Exame"
    else:
        status = "Reprovado"

    Boletim.append([nome, sexo, [nota1, nota2, nota3], media, status])

    resposta = str(input("Quer continuar? [S/N]")).strip().upper()
    if resposta in 'N':
        break

for i in range(0, len(Boletim), 1):

    if Boletim[i][4] == "Reprovado":
        AlunosReprovados += 1
        if Boletim[i][1 ] in 'F':
            MeninasReprovadas += 1
        else:
            MeninosReprovados += 1

    elif Boletim[i][4] == "Exame":
        AlunosExame += 1
        if Boletim[i][1] in 'F':
           MeninasExame+= 1
        else:
            MeninosExame+= 1

    elif Boletim[i][4] == "Aprovado":
       AlunosAprovados+= 1
       if Boletim[i][1] in 'F':
         MeninasAprovadas += 1
       else:
         MeninosAprovados += 1

print('----------Total de Alunos Cadastrados----------------')
TotalAlunos = AlunosAprovados +AlunosExame +AlunosReprovados
print('O Total De Alunos É: '+str(TotalAlunos))

print("Taxa Geral dos Alunos: ")
percentualAprovados = (AlunosAprovados/len(Boletim))*100
print('Alunos aprovados:  {:.2f} %'.format(percentualAprovados))

PercentualExame = (AlunosExame/len(Boletim))*100
print('Alunos para exame: {:.2f} %'.format(PercentualExame))

PercentualReprovado = (AlunosReprovados/len(Boletim))*100
print('Alunos reprovados: {:.2f} %'.format(PercentualReprovado))

print('-----------Estatistica por sexo--------------')
print('______________Alunas_________________')

print('Alunas aprovadas:'+str(MeninasAprovadas))

print('Alunas para exame:'+str(MeninasExame))

print('Alunas reprovadas:'+str(MeninasReprovadas))

print('______________Alunos_________________')

print('Alunos aprovados: '+str(MeninosAprovados))

print('Alunos para exame: '+str(MeninosExame))

print('Alunos reprovados: '+str(MeninosReprovados))



