import conexion

# Crear una instancia del conector de base de datos
conexion_bd = conexion.Connection(host="localhost", user="root", password="", database="proyectointegradorv01")

# Conectar a la base de datos
conexion_bd.connect()

# Leer los dispositivos desde la tabla
dispositivos_tv = conexion_bd.leer_dispositivos_tv()
for nombre_dispositivo in dispositivos_tv:
    print(nombre_dispositivo)
print("Fin tabla dispositivosTV")

# Ingresa datos de dispositivos a la tabla
conexion_bd.ingresar_dispositivos_tv(0,"aparato2", "Inch", 555, 8, "baja", "AC", "ninguna", 1)
print("Datos ingresados a dispositivostv")

# Desconectar de la base de datos
conexion_bd.disconnect()