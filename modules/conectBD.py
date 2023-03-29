import mysql.connector

#conexão com banco de dados
def Conectar():
    con = mysql.connector.connect(
        host='db-mysql-nyc1-36095-do-user-13841202-0.b.db.ondigitalocean.com',
        port=25060,
        database='animal_bet',
        user='doadmin',
        password='AVNS_Sw91S0--yIZ2lLIByJh')
    
    return con

  