import webbrowser

class Cancion():
    def __init__(self, id, nombre, duracion, autor, link, escuchado, usuarios_like, like):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion
        self.autor = autor
        self.link = link
        self.escuchado = escuchado #(0)
        self.usuarios_like = usuarios_like #[]
        self.like = like #0

    def mostrar(self):
        print(f'''
        nombre: {self.nombre}
        duracion: {self.duracion}
        autor: {self.autor}
        ''')
    
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
    
    def nueva_reproduccion(self, id_usuario):
        self.escuchado = self.escuchado + 1
        print("estas escuchando la cancion con exito")
        webbrowser.open(self.link)