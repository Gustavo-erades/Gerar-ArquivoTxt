def inserir_aluno():
    print("\n-- Inserção de aluno --\n")
    nome=str(input("Nome do aluno: "))
    mat=int(input("Número de Matrícula do(a) %s: "%nome))
    with open ("Alunos.txt","a+") as f:
        f.write(nome+"-"+str(mat)+"\n")
    f.close()
    
def excluir_aluno():
    print("\n-- Deleção de aluno --\n")
    antigo=input("Nome do aluno a ser deletado: ")
    with open ("Alunos.txt","r+") as f:
        linhas=f.readlines()
        f.seek(0)
        for l in linhas:
            if(l.startswith(antigo)):
                f.write("")
            else:
                f.write(l)
        f.truncate()
    print("Deleção feita com sucesso :)")

def editar_aluno():
    print("\n-- Edição de aluno --\n")
    antigo=input("Nome do aluno para edição: ")
    nome=str(input("Nome do novo aluno: "))
    mat=int(input("Número de Matrícula do(a) %s: "%nome))
    atualizacao= f"{nome}-{mat}\n"
    with open ("Alunos.txt","r+") as f:
        linhas=f.readlines()
        f.seek(0)
        for l in linhas:
            if(l.startswith(antigo)):
                f.write(atualizacao)
            else:
                f.write(l)
        f.truncate()
    print("Registro atualizado com sucesso!")

def listar_alunos():
    print("\n-- Listagem de aluno --\n")
    with open ("Alunos.txt","r",encoding="UTF-8") as f:
        print(f.read())
    f.close()

def menu():
    print("**********************")
    print("* 1 -> Inserir aluno *")
    print("* 2 -> Excluir aluno *")
    print("* 3 -> Editar alunos *")
    print("* 4 -> Listar alunos *")
    print("* 5 ->   Encerrar    *")
    print("**********************")

def logica():    
    match opcao:
        case 1:
            inserir_aluno()
        case 2:
            excluir_aluno()
        case 3:
            editar_aluno()
        case 4:
            listar_alunos()
        case 5:
            print("Fim :)")
            exit()
        case _:
            print("Opção inválida!")
menu()
opcao=int(input("Opção escolhida: "))
logica()        
while(opcao!=5):
    resp=str(input("Deseja continuar (S/N)? "))
    if(resp=="S" or resp=="s"):
        menu()
        opcao=int(input("Opção escolhida: "))
        logica()
    else:
        print("Fim :)")
        exit()
