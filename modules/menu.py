import modules.conectBD as Conect

import tkinter
import customtkinter

#Conectar com o banco de dados:
con = Conect.Conectar()

#Se conectado:
if con.is_connected():
    print(f'Conectado: {con.is_connected()}')
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

#Menu principal que lista as opções, chama funções e executa comandos SQL.
def Options(num):
    print(f'\n0- Cadastrar-se')
    print(f'1- Entrar')
    print(f'2- Listar Todos os Galos')
    print(f'3- Cadastrar Galo')
    print(f'4- Aposentar Galo')
    print(f'5- Criar Batalha')
    print(f'6- Sair\n')

    #Pega a opção do usuário
    op = int(num)

    #Estrutura semelhante ao Switch Case da Linguagem C
    # match op:

    #     #Inserir Produto
    #     case 1:
    #         prod = input('\nDigite o Nome do Produto: ')
    #         quant = int(input('Digite a Quantidade: '))

    #         if VerificaProduto(prod):
    #             sql = "INSERT INTO produtos (descricao, quantidade) VALUES (%s, %s)"
    #             values = (prod, quant)
    #             cursor.execute(sql, values)
    #             con.commit()
    #             print(f'O Produto {prod} foi inserido com sucesso.')
    #             return 
    #         else:
    #            print(f'ERROR: Produto {prod} já existe, se quiser, você pode alterar a quantidade.')
    #            return 
    #     #Listar todos os produtos
    #     case 2:
    #         sql = "SELECT * FROM produtos"
    #         cursor.execute(sql)
    #         rs = cursor.fetchall()

    #         print(f'\nTemos {len(rs)} produto(s):\n')
    #         for r in rs:
                
    #             print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
    #         return

    #     #Adicionar ao estoque de produto existente
    #     case 3:
    #         sql = "SELECT * FROM produtos"
    #         cursor.execute(sql)
    #         rs = cursor.fetchall()

    #         print(f'\nTemos {len(rs)} produto(s):\n')
    #         for r in rs:
                
    #             print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            
    #         prod = input('\nDigite o produto que deseja aumentar a quantidade:')
    #         quant = int(input('Digite a Quantidade: '))

    #         #Se adicionar quantidade negativa o cabloco vai cair aqui.    
    #         while quant <= 0:
    #             print('Digite um valor maior que 0.')
    #             quant = int(input('Digite a Quantidade: '))

    #         if VerificaProduto(prod):
    #            print(f'ERROR: Produto {prod} não existe.')
            
    #         else:
    #             sql = (f'UPDATE produtos SET quantidade = quantidade + {quant} where descricao = "{prod}"')
    #             cursor.execute(sql)
    #             con.commit()
        
    #     #Retirar do estoque de produto existente
    #     case 4:
    #         sql = "SELECT * FROM produtos"
    #         cursor.execute(sql)
    #         rs = cursor.fetchall()

    #         print(f'\nTemos {len(rs)} produto(s):\n')
    #         for r in rs:
                
    #             print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            
    #         prod = input('\nDigite o produto que deseja diminuir a quantidade:')
    #         quant = int(input('Digite a Quantidade: '))

    #         #Se adicionar quantidade negativa o cabloco vai cair aqui.    
    #         while quant <= 0:
    #             print('Digite um valor maior que 0.')
    #             quant = int(input('Digite a Quantidade: '))

    #         if VerificaQuantidade(prod,quant):
    #             sql = (f'UPDATE produtos SET quantidade = quantidade - {quant} where descricao = "{prod}"')
    #             cursor.execute(sql)
    #             con.commit()
            
    #         else:
    #             print(f'ERROR: Quantidade do Produto {prod} excedida.')


    #     #Excluir Produto
    #     case 5:
    #         sql = "SELECT * FROM produtos"
    #         cursor.execute(sql)
    #         rs = cursor.fetchall()

    #         print(f'\nTemos {len(rs)} produto(s):\n')
    #         for r in rs:
                
    #             print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            
    #         prod = input('\nDigite o produto que deseja excluir:')

    #         if VerificaProdutoExcluir(prod):
    #            print(f'ERROR: Produto {prod} não existe.')
    #         else:
    #             sql = (f'DELETE FROM produtos Where descricao = "{prod}"')
    #             cursor.execute(sql)
    #             con.commit()

    #     case 6:
    #         con.commit()
    #         cursor.close()
    #         con.close()
    #         print("Conexão ao MySQL foi encerrada")
    #         exit()

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1920x1080")
app.title('Animal Bet')

def close_window():
    app.destroy()
# Use CTkButton instead of tkinter Button
button0 = customtkinter.CTkButton(master=app, text="Cadastrar-se", command= lambda: Options(0))
button0.place(relx=0.5, rely=0.5, anchor=tkinter.N)

button1 = customtkinter.CTkButton(master=app, text="Entrar", command=lambda: Options(1))
button1.place(relx=0.5, rely=0.5, anchor=tkinter.N)

button2 = customtkinter.CTkButton(master=app, text="Listar Todos os Galos", command=lambda: Options(2))
button2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button3 = customtkinter.CTkButton(master=app, text="Cadastrar Galo", command=lambda: Options(3))
button3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button4 = customtkinter.CTkButton(master=app, text="Aposentar Galo", command=lambda: Options(4))
button4.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button5 = customtkinter.CTkButton(master=app, text="Criar Batalha", command=lambda: Options(5))
button5.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button6 = customtkinter.CTkButton(master=app, text="Sair", command=lambda: close_window())
button6.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    
app.mainloop()

