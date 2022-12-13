import mysql.connector as _sql

table_name = "PassengerDetails"
con = _sql.connect(host="localhost", user="root", passwd="root", database="airline_booking")

if not con.is_connected():
    print("Unsucessful")

cursor = con.cursor()

try:
    cursor.execute("CREATE TABLE PassengerDetails (ID int not null auto_increment, Name VARCHAR(255), From_city VARCHAR(255), To_city VARCHAR(255), Date VARCHAR(255), Passengers VARCHAR(255), primary key (ID))")
except _sql.errors.ProgrammingError:
    pass

def add_passengers(details):
    cursor.execute(f'''INSERT INTO {table_name} (Name, From_city, To_city, Date, Passengers) VALUES('{details["Name"]}', '{details["From"]}', '{details["To"]}', '{details["Start_Date"]}', '{details["Travellers"]}')''')
    con.commit()