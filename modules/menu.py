import modules.conectBD as Conect
import modules.options as Options

import tkinter
import customtkinter

def start():
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

    customtkinter.set_appearance_mode("light")  
    customtkinter.set_default_color_theme("dark-blue")  

    app = customtkinter.CTk()
    app.geometry("1920x1080")
    app.title('Animal Bet')

    def close_window():
        con.commit()
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")
        app.destroy()

    # Tela Inicial
    button0 = customtkinter.CTkButton(master=app, text="Cadastrar-se", command= lambda: Options.select( num=0))
    button0.place(x=10, y=10)

    button1 = customtkinter.CTkButton(master=app, text="Entrar", command=lambda: Options(1))
    button1.place(x=160, y=10)

    button2 = customtkinter.CTkButton(master=app, text="Listar Todos os Galos", command=lambda: Options(2))
    button2.place(x=310, y=10)

    button3 = customtkinter.CTkButton(master=app, text="Cadastrar Galo", command=lambda: Options(3))
    button3.place(x=460, y=10)

    button4 = customtkinter.CTkButton(master=app, text="Aposentar Galo", command=lambda: Options(4))
    button4.place(x=610, y=10)

    button5 = customtkinter.CTkButton(master=app, text="Criar Batalha", command=lambda: Options(5))
    button5.place(x=760, y=10)

    button6 = customtkinter.CTkButton(master=app, text="Sair", command=lambda: close_window())
    button6.place(x=910, y=10)

        
    app.mainloop()

