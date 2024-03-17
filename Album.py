from Cancion import Cancion
import uuid

class Album():
    def __init__(self, id, nombre, descripcion, portada, fecha, genero, tracklist, autor, escuchado, usuarios_like, like):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.portada = portada
        self.fecha = fecha
        self.genero = genero
        self.tracklist = tracklist
        self.autor = autor
        self.escuchado = escuchado #(0)
        self.usuarios_like = usuarios_like #[]
        self.like = like #0

    def mostrar(self):
        print(f'''
        nombre: {self.nombre}
        descripcion: {self.descripcion}
        portada: {self.portada}
        fecha: {self.fecha}
        genero: {self.genero}
        tracklist: {self.tracklist}
        autor: {self.autor}
        ''')

    #Crea id aleatorios unicos para los usuarios, albums y canciones
    def crear_id(self):
        uuid_aleatorio = uuid.uuid4()
        id_unnico = (f"{uuid_aleatorio.hex[:8]}-{uuid_aleatorio.hex[8:12]}-{uuid_aleatorio.hex[12:16]}-{uuid_aleatorio.hex[16:20]}-{uuid_aleatorio.hex[20:]}")
        return id_unnico

    
    #Este metodo crea las canciones como objeto y las agrega al tracklist
    def crear_canciones(self, lista_canciones, usuario_registrado):
        while True:
            print("\nIngrese los datos de su nueva cancion: ")
            id = self.crear_id()
            nombre = input("Ingresa el nombre de la cancion nueva: ")
            duracion = input("Ingresa la duracion de la cancion nueva: ")
            autor = usuario_registrado.id
            link = input("Ingresa el link de la cancion nueva: ")
            escuchado = 0
            usuarios_like = []
            like = []

            nueva_cancion = Cancion(id, nombre, duracion, autor, link, escuchado, usuarios_like, like)
            lista_canciones.append(nueva_cancion)
            self.tracklist.append(nueva_cancion.id)

            print("Cancion creada con exito!")

            print("\nDesea seguir agregando canciones? ")
            seguir = input("Escoge, sabiendo que: a = si y b = no >")
            while "a" == seguir.lower() and "b" == seguir.lower():
             seguir = input("Opción inválida, vuelva a escoger, sabiendo que: a = si y b = no >")
            
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
    
    #Consigue le total de escuchas por cancion y lo suma al album
    def contador_escuchas(self, lista_cancion):
        for id_cancion in self.tracklist:
            for cancion in lista_cancion:
                if cancion.id == id_cancion:
                    self.escuchado += cancion.escuchado