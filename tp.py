class ProgramaPrincipal:

    def menu(self):
        while True:
            # menu de opciones
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
                #Se pide ingresar por pantalla los datos a insertar en la primer tabla MONOPATIN_1
                marca = input("Por favor ingrese la marca del monopatin: ")
                precio = input("Por favor ingrese el precio del monopatin: ")
                cantidad = input("Por favor ingrese la cantidad de monopatines: ")
                disponibilidad = input("Por favor ingrese la disponibilidad del monopatin: ")
                #Se pasan por parámetro
                nuevo_monopatin_1 = Monopatin_1(marca,precio,cantidad,disponibilidad)
                #Se llama a la función que inserta el registro
                nuevo_monopatin_1.cargar_monopatin1()
            if nro == 2:
                #Se pide ingresar por pantalla los datos a ensertar en la segunda tabla MONOPATIN_2
                modelo = input("Por favor ingrese el modelo del monopatin: ")
                marca = input("Por favor ingrese la marca del monopatin: ")
                potencia = input("Por favor ingrese la potencia del monopatin: ")
                precio = input("Por favor ingrese el precio del monopatin: ")
                color = input("Por favor ingrese el color del monopatin: ")
                fechaUltimoPrecio = datetime.now()
                # Se pasa por parametros los datos ingresados
                nuevo_monopatin_2 = Monopatin_2(modelo,marca,potencia,precio,color,fechaUltimoPrecio)
                #Se llama a la función que inserta los datos
                nuevo_monopatin_2.cargar_monopatin_2()

            if nro ==3:
                #Se pide ingresar la Marca del monopatin y luego el precio a actualizar
                marca = input("Por favor ingrese el nombre de la marca: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                # Se pasan los valores por parámetro
                monopatin_a_modificar=Monopatin_1(marca,precio)
                # Se llama a la función de actualizar monopatin
                monopatin_a_modificar.modificar_monopatin_1() 
            if nro ==4:
                #Se pide ingresar la marca del monopatin a eliminar
                marca = input("Por favor ingrese el nombre de la marca: ")
                # Se pasa el valor por parametro
                monopatin_a_eliminar=Monopatin_1(marca)
                #Se llama a la función eliminar monopatin
                monopatin_a_eliminar.eliminar_monopatin_1(); 
            if nro==5:
                #Se pide el nombre de la marca para actualizar la disponibilidad
                marca= input("Por favor ingrese el nombre de la marca: ")
                #Se pasa el valor por parametro
                modificar_dispo = Monopatin_1(marca)
                #Se llama a la función actualizar disponibilidad
                modificar_dispo.modificar_disponibilidad()
            if nro==6:
                #Se listan todos los monopatines
                lista_automovil=Monopatin_1(marca,precio,cantidad,disponibilidad)
                lista_automovil.listar_monopatines_1()
            if nro==7:
                #Se hace un historico y se suma el 23% al precio actual
                historico = Monopatin_2(modelo,marca,potencia,precio,color,fechaUltimoPrecio)
                historico.cargar_historico()
            if nro==8:
                #Se pide la fecha para filtrar la tabla
                fecha= input("Por favor ingrese la fecha a filtrar: ")
                buscar_fecha = Monopatin_2(modelo,marca,potencia,precio,color,fecha)
                buscar_fecha.buscar_por_fecha() 

            if nro==0:
                print("Programa cerrado con éxito!")
                break