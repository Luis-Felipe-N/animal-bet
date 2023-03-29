import mysql.connector

#Menu principal que lista as opções, chama funções e executa comandos SQL.
def select(num):

    #Pega a opção do usuário
    op = int(num)

    #Estrutura semelhante ao Switch Case da Linguagem C
    match op:
        
        case 0:
            nomeCadastro = input('\nDigite o Nome do Usuário: ')
            email = input('Digite o email: ')
            cpf = float(input('Digite o CPF: '))
            senha = input('Digite a senha: ')

            podeCadastrar = VerificaPessoa(nomeCadastro)
            podeCadastrar = VerificaPessoa(email)
            podeCadastrar = VerificaPessoa(cpf)

            if podeCadastrar:
                sql = "INSERT INTO usuarios (nome, email, cpf, senha, saldo, cargo) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (nomeCadastro, email, cpf,senha, 0, 1)
                self.cursor.execute(sql, values)
                self.con.commit()
                print(f'O Produto {prod} foi inserido com sucesso.')
                return 
            else:
               print(f'ERROR: Produto {prod} já existe, se quiser, você pode alterar a quantidade.')
               return 
            
        #Inserir Produto
        case 1:
            prod = input('\nDigite o Nome do Produto: ')
            quant = int(input('Digite a Quantidade: '))

            if VerificaProduto(prod):
                sql = "INSERT INTO produtos (descricao, quantidade) VALUES (%s, %s)"
                values = (prod, quant)
                cursor.execute(sql, values)
                con.commit()
                print(f'O Produto {prod} foi inserido com sucesso.')
                return 
            else:
               print(f'ERROR: Produto {prod} já existe, se quiser, você pode alterar a quantidade.')
               return 
        #Listar todos os produtos
        case 2:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            rs = cursor.fetchall()

            print(f'\nTemos {len(rs)} produto(s):\n')
            for r in rs:
                
                print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            return

        #Adicionar ao estoque de produto existente
        case 3:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            rs = cursor.fetchall()

            print(f'\nTemos {len(rs)} produto(s):\n')
            for r in rs:
                
                print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            
            prod = input('\nDigite o produto que deseja aumentar a quantidade:')
            quant = int(input('Digite a Quantidade: '))

            #Se adicionar quantidade negativa o cabloco vai cair aqui.    
            while quant <= 0:
                print('Digite um valor maior que 0.')
                quant = int(input('Digite a Quantidade: '))

            if VerificaProduto(prod):
               print(f'ERROR: Produto {prod} não existe.')
            
            else:
                sql = (f'UPDATE produtos SET quantidade = quantidade + {quant} where descricao = "{prod}"')
                cursor.execute(sql)
                con.commit()
        
        #Retirar do estoque de produto existente
        case 4:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            rs = cursor.fetchall()

            print(f'\nTemos {len(rs)} produto(s):\n')
            for r in rs:
                
                print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            
            prod = input('\nDigite o produto que deseja diminuir a quantidade:')
            quant = int(input('Digite a Quantidade: '))

            #Se adicionar quantidade negativa o cabloco vai cair aqui.    
            while quant <= 0:
                print('Digite um valor maior que 0.')
                quant = int(input('Digite a Quantidade: '))

            if VerificaQuantidade(prod,quant):
                sql = (f'UPDATE produtos SET quantidade = quantidade - {quant} where descricao = "{prod}"')
                cursor.execute(sql)
                con.commit()
            
            else:
                print(f'ERROR: Quantidade do Produto {prod} excedida.')


        #Excluir Produto
        case 5:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            rs = cursor.fetchall()

            print(f'\nTemos {len(rs)} produto(s):\n')
            for r in rs:
                
                print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            
            prod = input('\nDigite o produto que deseja excluir:')

            if VerificaProdutoExcluir(prod):
               print(f'ERROR: Produto {prod} não existe.')
            else:
                sql = (f'DELETE FROM produtos Where descricao = "{prod}"')
                cursor.execute(sql)
                con.commit()

def VerificaPessoa(pessoa):
    sql = "SELECT * FROM usuarios"
    self.cursor.execute(sql)
    rs = self.cursor.fetchall()

    for r in rs:
        if pessoa == r[1] or pessoa == r[2] or pessoa == r[3] :
            return False
    return True