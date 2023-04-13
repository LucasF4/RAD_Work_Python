import sqlite3
import os
import locale

banco = sqlite3.connect('banco_teste.db')
cursor = banco.cursor()

# ---------------------------- COMANDO PARA DELETAR TABELA ---------------------------
#cursor.execute("DROP TABLE pessoas")
#cursor.execute("DROP TABLE conta")
# ---------------------------- COMANDO DE CRIAÇÃO DA TABELA PESSOAS ---------------------------
#cursor.execute("CREATE TABLE pessoas (cpf text, primeiro_nome text, nome_do_meio text, sobrenome text, idade integer, conta text) ")
# ---------------------------- COMANDO DE CRIAÇÃO DA TABELA CONTA ---------------------------
#cursor.execute("CREATE TABLE conta (agencia text, numero text, saldo real, gerente text, titular text)")
# ---------------------------- COMANDO CRIAÇÃO COLUNA CONTA FORMATO DE TEXTO ---------------------------
#cursor.execute("ALTER TABLE pessoas ADD COLUMN conta text"
# ---------------------------- COMANDO DELETA OS DADOS DO BANCO ---------------------------
#cursor.execute("DELETE FROM pessoas")
#cursor.execute("DELETE FROM conta")
#banco.commit()
try:

    numPessoas = cursor.execute("SELECT COUNT(*) FROM pessoas")
    objPessoas = numPessoas.fetchone()
    print(objPessoas[0])
    if objPessoas[0] == 0:
        nomes = open('nomes.txt','r')
        entrada = nomes.readlines()
        #saida = entrada.replace(' ', ',')
        #newNomes = open('nomes2.txt', 'w')
        #newNomes.write(saida)
        for i in entrada:
                dados = i.split()
                cpf, primeiro_nome, nome_do_meio, sobrenome, idade, conta = dados
                cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?, ?)", (dados))
            
                print(i.split()[0] + ' ' + i.split()[1] + ' ' + i.split()[2] + ' ' + i.split()[3] + ' ' + i.split()[4] + ' ' + i.split()[5])
                banco.commit()

        nomes.close()
        #newNomes.close()

    numContas = cursor.execute("SELECT COUNT(*) FROM conta")
    objContas = numPessoas.fetchone()
    print(objContas[0])
    if objContas[0] == 0:
        contas = open('contas.txt','r')
        entrada2 = contas.readlines()
        #saida = entrada.replace(' ', ',')
        #newNomes = open('nomes2.txt', 'w')
        #newNomes.write(saida)
        for i in entrada2:
                dados = i.split()
                agencia, numero, saldo, gerente, titular = dados
                cursor.execute("INSERT INTO conta VALUES (?, ?, ?, ?, ?)", (dados))
            
                print(i.split()[0] + ' ' + i.split()[1] + ' ' + i.split()[2] + ' ' + i.split()[3] + ' ' + i.split()[4] )
                banco.commit()

        contas.close()


except NameError as error:
    print("Ocorreu um erro: " + NameError)


locale.setlocale(locale.LC_ALL, 'Portuguese')

a = 1
while a == 1:
    print('=============================')
    selecionado = str(input("[1] - Pessoas | [2] - Sair\n"))

    if selecionado == '1':
        os.system('cls')
        opcao = str(input('[1] - Listar Pessoas | [2] - Cadastrar Pessoas | [3] - Editar Pessoas | [4] - Deletar Pessoas\n'))

        if opcao == '1':
            os.system("cls")
            clientes = cursor.execute("SELECT * FROM pessoas")
            clientObj = clientes.fetchall()
            arquivo = open('pessoas.txt', 'w')
            for i in clientObj:
                arquivo.write('==========================\n')
                arquivo.write('CPF: ' + str(i[0])+'\n')
                arquivo.write('Nome: ' + i[1]+'\n')
                arquivo.write('Segundo Nome: ' + i[2]+'\n')
                arquivo.write('Sobrenome: ' + i[3]+'\n')
                arquivo.write('Idade: ' + str(i[4])+'\n')
                arquivo.write('Conta: ' + str(i[5])+'\n')
            arquivo.close()
            print("Arquivo Gerado!")

        if opcao == '2':
            os.system("cls")
            primeiro = str(input("Primeiro Nome: "))
            segundo = str(input("Segundo Nome: "))
            sobrenome =str(input("SobreNome: "))
            cpf = str(input("CPF: "))
            idade = str(input("Idade: "))
            conta = str(input("Conta: "))
            try:
                cursor.execute("INSERT INTO pessoas VALUES ('"+cpf+"', '"+primeiro+"', '"+segundo+"', '"+sobrenome+"', "+idade+", '"+conta+"')")
                print("Inserido")
                banco.commit()
            except:
                print("Problemas na inserção.")
        
        if opcao == '3':
            os.system("cls")
            whereCPF = str(input("Qual o CPF da pessoa que você deseja editar as informações?\n"))
            select = cursor.execute("SELECT * FROM pessoas WHERE cpf = "+whereCPF)
            selectObj = select.fetchone()
            if selectObj == None:
                print('Nenhuma pessoa cadastrada com esse CPF')
            else:
                print('====== TODOS OS DADOS DEVERÃO SER REPETIDOS ======')
                primeiro = str(input('Primeiro Nome: '))
                segundo = str(input('Segundo Nome: '))
                sobrenome = str(input('Sobrenome: '))
                cpf = str(input('CPF: '))
                idade = str(input("Idade: "))
                conta = str(input("Conta: "))
                try:
                    cursor.execute("UPDATE pessoas SET primeiro_nome = '"+primeiro+"', nome_do_meio = '"+segundo+"', sobrenome = '"+sobrenome+"', idade = "+idade+", cpf = "+cpf+", conta = '"+conta+"' ")
                    banco.commit()
                except NameError as error:
                    print('Problemas na atualização no cadastro', error)
        if opcao == '4':
            os.system("cls")
            whereCPF = str(input("Qual o CPF da pessoa que você deseja deletar as informações?\n"))
            select = cursor.execute("SELECT * FROM pessoas WHERE cpf = "+whereCPF)
            selectObj = select.fetchone()
            if selectObj == None:
                print('Nenhuma pessoa cadastrada com esse CPF')
            else:
                cursor.execute("DELETE FROM pessoas WHERE cpf = " + whereCPF)
                banco.commit()
                print("Usuário Deletado com sucesso.")

    if selecionado == '2':
        a = 2

#banco.commit()
