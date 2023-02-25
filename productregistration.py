Ai = 0
run = 1
import csv
def programap():
    global run
    opcao()
    
def CadastrodeProduto():    
    arquivo = open("dbproduct.csv", "r", newline='')
    leitor = csv.reader(arquivo)
    dados = list(leitor)
    arquivo.close()
    ID_Produto = input("Digite o id do produto: ")
    nomeproduto = input("\nDigite o nome do produto: ")
    preco = input("\nDigite o preço do produto: R$")
    estoque = input("\nDigite a quatidade do estoque: ")
    unidade = input("\nDigite a unidade: ")
        
    dados.append([ID_Produto, nomeproduto, preco, estoque, unidade])
        
    arquivo = open("dbproduct.csv", "w", newline='')
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)
    arquivo.close()
    op = input("\nDeseja ver os produtos?")
    if(op == "s"):
        Leitura_de_Produto()
        
def Leitura_de_Produto():
    arquivo = open("dbproduct.csv", "r", newline='') 
    listaDeProdutos = arquivo.readlines() 
    for RegistroProduto in listaDeProdutos:
         print(RegistroProduto)
         
def RemoverProdutos():
    arquivo = open("dbproduct.csv", "r", newline='')
    ListaRegistrada = arquivo.readlines()
    arquivo.close()
    nome = input("Deseja deletar?")
    for registro in ListaRegistrada:
            dados = registro.split(",") 
            if(nome == dados[0]):
                ListaRegistrada.remove(registro)
    arquivo = open("dbproduct.csv", "w", newline='')
    for registro in ListaRegistrada:
            arquivo.write(registro)
    arquivo.close
    
def attProduto():
    i = 0
    arquivo = open("dbproduct.csv", "r", newline='')
    ListaRegistrada = arquivo.readlines()
    arquivo.close()
    ID_Produto = input("ID_para_atualizar: ")
    while (i < len(ListaRegistrada)):
        scan = ListaRegistrada[i]
        scan = scan.split(",")           
        if(ID_Produto == scan[0]):
            dados = LerArquivo()
            nomeproduto = input("\nDigite o nome do produto: ")
            preco = input("\nDigite o preço do produto: R$")
            estoque = input("\nDigite a quatidade do estoque: ")
            unidade = input("\nDigite a unidade: ")
        
            dados[i] = ([ID_Produto, nomeproduto, preco, estoque, unidade])
            
            arquivo = open("dbproduct.csv", "w", newline='')
            escritor = csv.writer(arquivo)
            escritor.writerows(dados)
            
        i = i + 1
    arquivo.close()
    return -1
            
def LerArquivo():
    arquivo = open("dbproduct.csv" , "r")
    leitor = csv.reader(arquivo)
    lista_dados = list(leitor)
    arquivo.close()
    return lista_dados
        
def opcao():
    global run
    while run == 1:
        opc = input("(A)dicionar Produto\n Modulo de (V)enda\n (R)emover Produto\n a(T)ualizar\n Ver (P)roduto\n_")    
        if opc == "A":
            CadastrodeProduto()
            pass
        elif opc == "V":
            # TODO Venda de produtos
            pass
        elif opc == "R":
            RemoverProdutos()
            # TODO Remoção de produtos
            pass
        elif opc == "T":
            attProduto()
            # TODO Atualização de produtos
            pass
        elif opc == "P":
            Leitura_de_Produto()
            # TODO Visualização de produtos
            pass
        else:
            print("Opção inválida, finalizando o programa")
            run = -1
    
programap()         
  

