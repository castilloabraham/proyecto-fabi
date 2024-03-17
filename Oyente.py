from Usuario import Usuario

class Oyente(Usuario):
    def __init__(self, id, nombre, correo, username, tipo_de_usuario, escuchado, playlists):
        super().__init__(id, nombre, correo, username, tipo_de_usuario)
        self.escuchado = escuchado #(0)
        self.playlists = playlists #[]

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
        while not cambio.isnumeric() or not int(cambio) in range(1, 4):
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
    
    def dar_like(self, id_usuario):
        if not id_usuario in self.usuarios_like:
            self.like = self.like + 1
            self.usuarios_like.append(id_usuario)
            print("Diste like con exito")
        else:
            print("ya le dio like")
    
    def quitar_like(self, id_usuario):
        if id_usuario in self.usuarios_like:
            self.like = self.like - 1
            self.usuarios_like.remove(id_usuario)
            print("Diste dislike con exito")
        else:
            print("no le has dado like")
    
    def nueva_reproduccion(self):
        self.escuchado = self.escuchado + 1
        print("estas escuchando la cancion con exito")
    

    #Consigue le total de escuchas por playlist y lo suma al oyente
    def contador_escuchas(self, lista_playlists):
        for id_playlist in self.playlists:
            for playlist in lista_playlists:
                if playlist.id == id_playlist:
                    self.escuchado += playlist.escuchado