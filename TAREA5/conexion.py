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
            
    def modificar_dispositivos_tv(self, Id_DispositivosTV, Nuevo_Precio):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "UPDATE dispositivostv SET Precio = %s WHERE Id_DispositivosTV = %s"
                values = (Nuevo_Precio, Id_DispositivosTV)
                cursor.execute(query, values)
                self.connection.commit()
                cursor.close()
                print("Datos modificados correctamente")
            else:
                print("No se pudo conectar a la base de datos")
        except mysql.connector.Error as error:
            print("Error al modificar dispositivos de TV:", error)

    def eliminar_dispositivos_tv(self, Id_DispositivosTV):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "DELETE FROM dispositivostv WHERE Id_DispositivosTV = %s"
                values = (Id_DispositivosTV,)
                cursor.execute(query, values)
                self.connection.commit()
                cursor.close()
                print("Datos eliminados correctamente")
            else:
                print("No se pudo conectar a la base de datos")
        except mysql.connector.Error as error:
            print("Error al eliminar dispositivos de TV:", error)