def inserir_aluno():
    nome=str(input("Nome do aluno: "))
    mat=int(input("Número de Matrícula do(a) %s: "%nome))
    with open ("Alunos.txt","a+") as f:
        f.write(nome+"-"+str(mat)+"\n")
    f.close()
    
def excluir_aluno():
    with open ("Alunos.txt","w+") as f:
        f.write("")
    f.close()

def editar_aluno():
    with open ("Alunos.txt","r") as f_ler:
        print("Alunos já cadastrados: \n"+f_ler.read())
    f_ler.close()
    with open ("Alunos.txt","w+") as f:
        nome=str(input("Nome do aluno: "))
        mat=int(input("Número de Matrícula do(a) %s: "%nome))
        f.write(nome+"-"+str(mat)+"\n")
    f.close()

def listar_alunos():
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
