# Bruna Barbour Fernandes - RA: 23007950

print ("AGENDA TABAJARA")
ag = {}
Opcao = -1

for i in ag:
    print(i," ",ag[i])


while(Opcao != 0):
    print("_"*30)
    print("Cadastrar - 1")
    print("Listar - 2")
    print("Consultar - 3")
    print("Sair - 0")
    opcao = int(input("Insira sua opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        fonec = int(input("Digite o telefone celular: "))
        fonef = int(input("Digite o telefone fixo: "))

        aux={ nome: [fonec, fonef]}
        ag.update(aux)
        print ("\n")
        print("Cadastrado!")
        print ("\n")

    if opcao == 2:
        for i in ag:
            print(i," ",ag[i])
    
    if opcao == 3:
        nome = input("Digite o nome de consulta: ")
        for i in ag:
            if i == nome:
                print(i," ",ag[i])