class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("1- Cargar Monopatin Tabla 1")
            print("2- Cargar Monopatin tabla 2")
            print("3- Modificar datos de un Monopatin")
            print("4- Borrar Monopatin")
            print("5- Cargar disponibilidad de Monopatines")
            print("6- Ver listado")
            print("7- Cargar Historico")
            print("8- Buscar por fecha")

            
            
            print("0- Salir de menu")
            nro = int(input("Por favor ingrese un número:"))
            if nro == 1:
                marca = input("Por favor ingrese la marca del monopatin: ")
                precio = input("Por favor ingrese el precio del monopatin: ")
                cantidad = input("Por favor ingrese la cantidad de monopatines: ")
                disponibilidad = input("Por favor ingrese la disponibilidad del monopatin: ")
                nuevo_monopatin_1 = Monopatin_1(marca,precio,cantidad,disponibilidad)
                nuevo_monopatin_1.cargar_monopatin1()
            if nro == 2:
                modelo = input("Por favor ingrese el modelo del monopatin: ")
                marca = input("Por favor ingrese la marca del monopatin: ")
                potencia = input("Por favor ingrese la potencia del monopatin: ")
                precio = input("Por favor ingrese el precio del monopatin: ")
                color = input("Por favor ingrese el color del monopatin: ")
                fechaUltimoPrecio = datetime.now()
                nuevo_monopatin_2 = Monopatin_2(modelo,marca,potencia,precio,color,fechaUltimoPrecio)
                nuevo_monopatin_2.cargar_monopatin_2()

            if nro ==3:
                marca = input("Por favor ingrese el nombre de la marca: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                monopatin_a_modificar=Monopatin_1(marca,precio)
                monopatin_a_modificar.modificar_monopatin_1() 
            if nro ==4:
                marca = input("Por favor ingrese el nombre de la marca: ")
                monopatin_a_eliminar=Monopatin_1(marca)
                monopatin_a_eliminar.eliminar_monopatin_1(); 
            if nro==5:
                marca= input("Por favor ingrese el nombre de la marca: ")
                modificar_dispo = Monopatin_1(marca)
                modificar_dispo.modificar_disponibilidad()
            if nro==6:
                lista_automovil=Monopatin_1(marca,precio,cantidad,disponibilidad)
                lista_automovil.listar_monopatines_1()
            if nro==7:
                historico = Monopatin_2(modelo,marca,potencia,precio,color,fechaUltimoPrecio)
                historico.cargar_historico()
            if nro==8:
                fecha= input("Por favor ingrese la fecha a filtrar: ")
                buscar_fecha = Monopatin_2(modelo,marca,potencia,precio,color,fecha)
                buscar_fecha.buscar_por_fecha() 

            if nro==0:
                print("Programa cerrado con éxito!")
                break

    def crearTablas(self):
        conexion = Conexiones() 
        conexion.abrirConexion() 
        conexion.miCursor.execute("DROP TABLE IF EXISTS MONOPATIN_2")
        conexion.miCursor.execute("CREATE TABLE MONOPATIN_2 (id_monopatin INTEGER PRIMARY KEY , modelo  VARCHAR(30),  marca  VARCHAR(30), potencia  VARCHAR(30),  precio FLOAT NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATE)")  
        conexion.miCursor.execute("DROP TABLE IF EXISTS MONOPATIN_HISTORICO")
        conexion.miCursor.execute("CREATE TABLE MONOPATIN_HISTORICO (id_monopatin INTEGER PRIMARY KEY , modelo  VARCHAR(30),  marca  VARCHAR(30), potencia  VARCHAR(30),  precio FLOAT NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME)")  
        conexion.miCursor.execute("DROP TABLE IF EXISTS MONOPATIN_1")
        conexion.miCursor.execute("CREATE TABLE MONOPATIN_1 (id_monopatin INTEGER PRIMARY KEY ,  marca  VARCHAR(30),  precio FLOAT NOT NULL, cantidad VARCHAR(30),disponibilidad VARCHAR(30),UNIQUE(marca))")      
        conexion.miConexion.commit()     
        conexion.cerrarConexion() 
    