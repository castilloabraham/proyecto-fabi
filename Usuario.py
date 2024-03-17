class Usuario():
    def __init__(self, id, nombre, correo, username, tipo_de_usuario):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.username = username
        self.tipo_de_usuario = tipo_de_usuario

    def mostrar_usuario(self):
        print(f'''
        nombre: {self.nombre}
        correo: {self.correo}
        username: {self.username}
        tipo_de_usuario: {self.tipo_de_usuario}
        ''')
    
    #Metodo que permite cambiar datos del usuario
    def cambiar_informacion(self):
        print("Que desea cambiar?")
        cambio = input("1. Nombre -- 2. Correo -- 3. Username  >")
        while not cambio.isnumeric() or not int(opcion) in range(1, 4):
            cambio = input("1. Nombre -- 2. Correo -- 3. Username  >")
        
        if cambio == "1":
            nombre = input("Ingrese su nombre: ")
            self.nombre=nombre

            print("Dato actualizado con exito!")
        elif cambio == "2":
            correo = input("Ingrese su correo electrónico: ")
            while not "@" in correo:
                print("Correo inválido, introduzca de nuevo:")
                correo = input("Ingrese su correo electrónico: ")
            self.correo = correo

            print("Dato actualizado con exito!")
        elif cambio == "3":
            #Falta verificar que sea unico
            username = input("Ingrese su username: ")
            self.username = username

            print("Dato actualizado con exito!")