import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexión exitosa")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Desconexión")

    def leer_dispositivos_tv(self):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "SELECT * FROM dispositivostv"
                cursor.execute(query)
                dispositivos = cursor.fetchall()
                cursor.close()
                return dispositivos
            else:
                print("No se pudo conectar a la base de datos")
        except mysql.connector.Error as error:
            print("Error al leer dispositivos de TV:", error)

    def ingresar_dispositivos_tv(self, Id_DispositivosTV, Nombre_dispositivo, Unidad_de_medida, Precio, Stock, Capacidad, Alimentacion, Observacion, Id_Estado):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "INSERT INTO dispositivostv (Id_DispositivosTV, Nombre_dispositivo, Unidad_de_medida, Precio, Stock, Capacidad, Alimentacion, Observacion, Id_Estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (Id_DispositivosTV, Nombre_dispositivo, Unidad_de_medida, Precio, Stock, Capacidad, Alimentacion, Observacion, Id_Estado)
                cursor.execute(query, values)
                self.connection.commit()
                cursor.close()
                print("Datos insertados correctamente")
            else:
                print("No se pudo conectar a la base de datos")
        except mysql.connector.Error as error:
            print("Error al ingresar dispositivos de TV:", error)

# Crear una instancia del conector de base de datos
conexion_bd = Connection(host="localhost", user="root", password="", database="proyectointegradorv01")

# Conectar a la base de datos
conexion_bd.connect()

# Leer los dispositivos desde la tabla
dispositivos_tv = conexion_bd.leer_dispositivos_tv()
for nombre_dispositivo in dispositivos_tv:
    print(nombre_dispositivo)
print("Fin tabla dispositivosTV")

# Ingresa datos de dispositivos a la tabla
conexion_bd.ingresar_dispositivos_tv(0,"Televi", "Inch", 333, 5, "alta", "AC", "ninguna", 1)
print("Datos ingresados a dispositivostv")

# Desconectar de la base de datos
conexion_bd.disconnect()