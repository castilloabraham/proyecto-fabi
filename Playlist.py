class Playlist():
    def __init__(self, id, nombre, descripcion, lista_de_cancion, creador, escuchado, usuarios_like, like):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.lista_de_cancion = lista_de_cancion
        self.creador = creador
        self.escuchado = escuchado #(0)
        self.usuarios_like = usuarios_like #[]
        self.like = like #0

    def mostrar(self):
        print(f'''
        nombre: {self.nombre}
        descripcion: {self.descripcion}
        lista_de_cancion: {self.lista_de_cancion}
        creador: {self.creador}
        ''')
    
    #Este metodo agrega las canciones  y las agrega al tracklist
    def agregar_canciones(self, lista_canciones, usuario_registrado):
        while True:
            print("Agregue una nueva cancion: ")
            for i, cancion in enumerate(lista_canciones):
                print(i+1, cancion.nombre)
            
            numero_cancion = input("Ingrese el numero de la cancion que desea agregar: ")
            while not numero_cancion.isnumeric() or not int(numero_cancion) in range(1, len(lista_canciones)+1):
                numero_cancion = input("Ingrese el numero de la cancion que desea agregar: ")

            cancion = lista_canciones[int(numero_cancion)-1]

            self.lista_de_cancion.append(cancion.id)

            print("Cancion agregada con exito!")

            print("\nDesea seguir agregando canciones? ")
            seguir = input("Escoge, sabiendo que: a = si y b = no >")
            while "a" == seguir.lower() and "b" == seguir.lower():
             seguir = input("Opción inválida, vuelva a escoger, sabiendo que: a = si y b = no > ")
            
            if seguir.lower() == "b":
                break
            
    
    
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
    

    #Consigue le total de escuchas por cancion y lo suma al playlist
    def contador_escuchas(self, lista_cancion):
        for id_cancion in self.lista_de_cancion:
            for cancion in lista_cancion:
                if cancion.id == id_cancion:
                    self.escuchado += cancion.escuchado