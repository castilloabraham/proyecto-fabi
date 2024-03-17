#Importacion de clases
from Cancion  import Cancion
from Album import Album
from Playlist import Playlist
from Usuario import Usuario
from Musico import Musico
from Oyente import Oyente

#Importacion de librerias
import requests
import uuid
import json

#Obtiene la informacion del api y la guarda
def api(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists):
    info_archivo = 0
    with open("usuarios.txt", "r") as archivo:
        informacion = archivo.read()
        info_archivo = str(informacion)

    if info_archivo == "":
        #obtiene la informacion del api album
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json"
        informacion = json.loads((requests.get(url)).text)
        for playlist in informacion:
            nuevo_playlist = Playlist(playlist["id"], playlist["name"], playlist["description"], playlist["tracks"], playlist["creator"], 0, [], 0)
            lista_playlists.append(nuevo_playlist)

        #obtiene la informacion del api album
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json"
        informacion = json.loads((requests.get(url)).text)
        for album in informacion:
            tracklist = []
            for cancion_dic in album["tracklist"]:
                tracklist.append(cancion_dic["id"])
                nueva_cancion = Cancion(cancion_dic["id"], cancion_dic["name"], cancion_dic["duration"], album["artist"], cancion_dic["link"], 0, [], 0)
                lista_canciones.append(nueva_cancion)

            nuevo_album = Album(album["id"], album["name"], album["description"], album["cover"], album["published"], album["genre"], tracklist, album["artist"], 0, [], 0)
            lista_albums.append(nuevo_album)

        #obtiene la informacion del api usuario
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json"
        informacion = json.loads((requests.get(url)).text)
        
        for usuario in informacion:
            if usuario["type"] == "listener":
                nuevo_usuario = Oyente(usuario["id"], usuario["name"], usuario["email"], usuario["username"], usuario["type"], 0, [])
                lista_oyentes.append(nuevo_usuario)
            else:
                albums = []
                for album in lista_albums:
                    if album.autor == usuario["id"]:
                        albums.append(album.id)

                nuevo_usuario = Musico(usuario["id"], usuario["name"], usuario["email"], usuario["username"], usuario["type"], 0, [], 0, albums)
                lista_musicos.append(nuevo_usuario)

            todos_usuarios.append(nuevo_usuario)
    else:
        obtener_info_txt(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists)
    


#Crea id aleatorios unicos para los usuarios, albums y canciones
def crear_id():
    uuid_aleatorio = uuid.uuid4()
    id_unnico = (f"{uuid_aleatorio.hex[:8]}-{uuid_aleatorio.hex[8:12]}-{uuid_aleatorio.hex[12:16]}-{uuid_aleatorio.hex[16:20]}-{uuid_aleatorio.hex[20:]}")
    return id_unnico

#Funcion que crea y guarda un usuario de no estar registrado
def registro(todos_usuarios, lista_musicos, lista_oyentes, usuario_registrado):
    
    id= crear_id()

    nombre = input("Ingrese su nombre: ")

    correo = input("Ingrese su correo electrónico: ")
    while not "@" in correo:
        print("Correo inválido, introduzca de nuevo:")
        correo = input("Ingrese su correo electrónico: ")
    
    #Falta verificar que sea unico
    username = input("Ingrese su username: ")

    tipo_de_usuario = input("¿Eres músico u oyente? Escoge, sabiendo que: a = cantante y b = oyente")
    while "a" == tipo_de_usuario.lower() and "b" == tipo_de_usuario.lower():
        print("Opción inválida, vuelva a escoger, sabiendo que: a = cantante y b = oyente")
        tipo_de_usuario = input("¿Eres músico u oyente? Escoge, sabiendo que: a = cantante y b = oyente")

    if tipo_de_usuario == 'a':
        tipo_de_usuario = 'musician'
        escuchado = 0
        usuarios_like = []
        like = 0
        albums = []
        
        nuevo_usuario = Musico(id, nombre, correo, username, tipo_de_usuario, escuchado, usuarios_like, like, albums)
        lista_musicos.append(neuvo_usuario)
    else: 
        tipo_de_usuario = 'listener'
        escuchado = 0
        playlists = []

        nuevo_usuario = Oyente(id, nombre, correo, username, tipo_de_usuario, escuchado, playlists)
        lista_oyentes.append(nuevo_usuario)
        usuario_registrado = nuevo_usuario
    
    usuarios.append(nuevo_usuario)
    print("Usuario registrado con exito")

#Funcion para crear menu apartir de una lista de opciones
def menu(opciones):
    for indice, opcion in enumerate(opciones):
        print(indice + 1, opcion)
    opcion_escogida = input("Ingresa (el número) de la opción escogida: ")

    while not opcion_escogida.isnumeric() or not int(opcion_escogida) in range(0, len(opciones) + 1):
        print("Ingrese una opción válida: ")
        opcion_escogida = input("Ingresa (el número) de la opción escogida: ")

    return opcion_escogida

#funcion para buscar musico, album, cancion y playlist
def buscador(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado):
    opciones_buscador = ["Nombre del músico", "Nombre del álbum", "Nombre de la canción", "Nombre del playlist", "Salir"]
    opcion = menu(opciones_buscador)

    if opcion == "1":
        buscador = input("Ingrese el nombre del musico que desea buscar: ").lower()
        print("Coincidencias: ")
        for perfil in lista_musicos:
            if buscador in perfil.nombre.lower():
                perfil.mostrar_usuario()
                
    elif opcion == "2":
        buscador = input("Ingrese el nombre del album que desea buscar: ").lower()
        print("Coincidencias: ")
        for album in lista_albums:
            if buscador in album.nombre.lower():
                album.mostrar()
            
    elif opcion == "3":
        buscador = input("Ingrese el nombre de la cancion que desea buscar: ").lower()
        print("Coincidencias: ")
        for cancion in lista_canciones:
            if buscador in cancion.nombre.lower():
                cancion.mostrar()

    elif opcion == "4":
        buscador = input("Ingrese el nombre de la playlist que desea buscar: ").lower()
        print("Coincidencias: ")
        for playlist in lista_playlists:
            if buscador in playlist.nombre.lower():
                playlist.mostrar()

    elif opcion == "5":
        print("Acabas de salir del modulo de ")

#salen y ejecutan las opciones de interacciones como like y reproduccion
def opcion_interaccion(opcion_escogida, usuario_registrado):
    opciones_interaccion = ["Like", "Dislike", "Reproduccion"]
    opcion = menu(opciones_interaccion)

    if opcion == "1":
        opcion_escogida.dar_like(usuario_registrado.id)
    elif opcion == "2":
        opcion_escogida.quitar_like(usuario_registrado.id)
    elif opcion == "3":
        opcion_escogida.nueva_reproduccion(usuario_registrado.id)

#Gestion de perfil, posee las opciones: Buscar perfil, Cambiar información del perfil, Borrar datos de perfil
def gestion_de_perfil(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado):
    opciones_gp = ["Buscar perfil", "Cambiar información del perfil", "Borrar datos de perfil", "Salir"]
    opcion = menu(opciones_gp)

    if opcion == "1":
        #Falta que si no hay coincidencia muestre error:
        #Muestra los usuarios que tengan alguna coincidencia con el nombre que escribio el usuario
        print("Buscar perfil")
        buscador = input("Ingresa el nombre de la persona que desea buscar: ").lower()

        print("\nCoincidencias:")
        for perfil in todos_usuarios:
            if buscador in perfil.nombre.lower():
                perfil.mostrar_usuario()
        
    elif opcion == "2":
        #Entra en el metodo del usuario para cambiar informacion
        print("Cambiar información del perfil")
        usuario_registrado.cambiar_informacion()
        
    elif opcion == "3":
        #Busca el usuario de las listas y lo elimina
        print("Borrar datos de perfil")

        print("\nEsta seguro que desea eliminar su cuenta? Perdera su informacion")
        eliminar = input("Escoge, sabiendo que: a = si y b = no")
        while "a" == eliminar.lower() and "b" == eliminar.lower():
            eliminar = input("Opción inválida, vuelva a escoger, sabiendo que: a = si y b = no")
        
        if eliminar.lower() == "a":
            for perfil in todos_usuarios:
                if usuario_registrado == perfil.nombre:
                    todos_usuarios.remove(usuario_registrado)
                    lista_musicos.remove(usuario_registrado)
                    lista_oyentes.remove(usuario_registrado)
            print("eliminado con exito")


        main()

    elif opcion == "4":
        print("¡Saliste de la Gestion de perfil!")

#Gestion musical, posee las opcion: Subir Album, Crear playlist, Buscar. Dependiendo del tipo de usuario
def gestion_musical(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado):
    #depende del tipo de usuario te muestra un menu distinto
    if usuario_registrado.tipo_de_usuario == "musician":
        opciones_gm_m = ["Subir Album", "Buscar", "Salir"]
        opcion = menu(opciones_gm_m)

        #Crea el album, las canciones dentro de el y guarda en las listas
        if opcion == "1":
            id = crear_id()
            nombre = input("Ingresa el nombre del nuevo album: ")
            descripcion = input("Ingresa la descricion del nuevo album: ")
            portada = input("Ingresa el link de la portada del nuevo album: ")
            fecha = input("Ingresa la fecha del nuevo album: ")
            genero = input("Ingresa el genero del nuevo album: ")
            tracklist = []
            autor = usuario_registrado.id
            escuchado = 0
            usuarios_like = []
            like = []


            nuevo_album = Album(id, nombre, descripcion, portada, fecha, genero, tracklist, autor, escuchado, usuarios_like, like)
            nuevo_album.crear_canciones(lista_canciones, usuario_registrado)

            lista_albums.append(nuevo_album)
            usuario_registrado.albums.append(nuevo_album)

            print("Se ha creado su album con exito")

        #lleva a la funcion buscar que comparte con oyente   
        elif opcion == "2":
            buscador(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado)

        elif opcion == "3":
            print("Ha salido de la gestion musical")
    else:
        opciones_gm_o = ["Crear Playlist", "Buscar", "Salir"]
        opcion = menu(opciones_gm_o)

        #Crea el playlist y guarda en las listas
        if opcion == "1":
            id = crear_id()
            nombre = input("Ingresa el nombre de la nueva playlist: ")
            descripcion = input("Ingresa la descricion de la nueva playlist: ")
            lista_de_cancion = []
            creador = usuario_registrado.id
            escuchado = 0
            usuarios_like = []
            like = []


            nuevo_playlist = Playlist(id, nombre, descripcion, lista_de_cancion, creador, escuchado, usuarios_like, like)
            nuevo_playlist.agregar_canciones(lista_canciones, usuario_registrado)

            lista_albums.append(nuevo_playlist)

            print("Se ha creado su album con exito")

        #lleva a la funcion buscar que comparte con oyente   
        elif opcion == "2":
            buscador(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado)

        elif opcion == "3":
            print("Ha salido de la gestion musical")
    
#Gestion Interaccion, posee las opciones de: dar like y reproduccion a las canciones, playlist, albums y musicos
def gestion_interaccion(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado):
    print("En este modulo podras interactuar, dandole like, dislike o reproduciendo a los siguientes:")
    
    opciones_gi = ["Cancion", "Musico", "Playlist", "Album", "Salir"]
    opcion = menu(opciones_gi)

    if opcion == "1":
        
        for i, cancion in enumerate(lista_canciones):
            print(i+1, cancion.nombre)
                

        opcion = input("Ingresa el numero de la cancion que deseas elegir: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, len(lista_canciones)+1):
            opcion = input("Ingresa el numero de la cancion que deseas elegir: ")
        
        cancion_escogida = lista_canciones[int(opcion)-1]

        opcion_interaccion(cancion_escogida, usuario_registrado)


    elif opcion == "2":
        #muestra y escoge los musicos
        for i, musico in enumerate(lista_musicos):
            print(i+1, musico.nombre)

        opcion = input("Ingresa el numero del musico que deseas elegir: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, len(lista_musicos)+1):
            opcion = input("Ingresa el numero del musico que deseas elegir: ")
        
        musico_escogido = lista_musicos[int(opcion)-1]

        #muestra y escoge los albums de ese musico
        for i, id_album in enumerate(musico_escogido.albums):
            for album in lista_albums:
                if album.id == id_album:
                    print(i+1, album.nombre)

        opcion = input("Ingresa el numero del album que deseas elegir: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, len(musico_escogido.albums)+1):
            opcion = input("Ingresa el numero del album que deseas elegir: ")

        album_escogido = ""
        for i, id_album in enumerate(musico_escogido.albums):
            for album in lista_albums:
                if album.id == id_album:
                    if int(opcion) == i:
                        album_escogido = album

        

        #muestra y escoge las canciones de ese album
        for i, id_cancion in enumerate(album_escogido.tracklist):
            for cancion in lista_canciones:
                if cancion.id == id_cancion:
                    print(i+1, cancion.nombre)

        opcion = input("Ingresa el numero de. la cancion que deseas elegir: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, len(album_escogido.tracklist)+1):
            opcion = input("Ingresa el numero de. la cancion que deseas elegir: ")

        cancion_escogido = ""
        for i, id_cancion in enumerate(album_escogido.tracklist):
            for cancion in lista_canciones:
                if cancion.id == id_cancion:
                    if int(opcion) == i+1:
                        cancion_escogido = cancion

        opcion_interaccion(cancion_escogido, usuario_registrado)

    elif opcion == "3":
        for i, album in enumerate(lista_playlists):
            print(i+1, album.nombre)

        opcion = input("Ingresa el numero del album que deseas elegir: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, len(lista_playlists)+1):
            opcion = input("Ingresa el numero del album que deseas elegir: ")

        playlist_escogido = lista_playlists[int(opcion)-1]

        #muestra y escoge las canciones de ese album
        for i, id_cancion in enumerate(playlist_escogido.lista_de_cancion):
            for cancion in lista_canciones:
                if cancion.id == id_cancion:
                    print(i+1, cancion.nombre)

        opcion = input("Ingresa el numero de. la cancion que deseas elegir: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, len(playlist_escogido.lista_de_cancion)+1):
            opcion = input("Ingresa el numero de. la cancion que deseas elegir: ")

        cancion_escogido = ""
        for i, id_cancion in enumerate(playlist_escogido.lista_de_cancion):
            for cancion in lista_canciones:
                if cancion.id == id_cancion:
                    if int(opcion) == i+1:
                        cancion_escogido = cancion

        opcion_interaccion(cancion_escogido, usuario_registrado)

    elif opcion == "4":
        for i, album in enumerate(lista_albums):
            print(i+1, album.nombre)

        opcion = input("Ingresa el numero del album que deseas elegir: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, len(lista_albums)+1):
            opcion = input("Ingresa el numero del album que deseas elegir: ")

        album_escogido = lista_albums[int(opcion)-1]

        #muestra y escoge las canciones de ese album
        for i, id_cancion in enumerate(album_escogido.tracklist):
            for cancion in lista_canciones:
                if cancion.id == id_cancion:
                    print(i+1, cancion.nombre)

        opcion = input("Ingresa el numero de. la cancion que deseas elegir: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, len(album_escogido.tracklist)+1):
            opcion = input("Ingresa el numero de. la cancion que deseas elegir: ")

        cancion_escogido = ""
        for i, id_cancion in enumerate(album_escogido.tracklist):
            for cancion in lista_canciones:
                if cancion.id == id_cancion:
                    if int(opcion) == i+1:
                        cancion_escogido = cancion

        opcion_interaccion(cancion_escogido, usuario_registrado)

    elif opcion == "5":
        print("Ha salido del modulo de iteraccion")

#Indicadores, aqui se muestran estadisticas en el formato de Top 5
def indicadores(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado):
    opciones_i = ["Top 5 de músicos con mayor cantidad de streams", "Top 5 de álbumes con mayor cantidad de streams", "Top 5 de canciones con mayor cantidad de streams", "Top 5 de escuchas con mayor cantidad de streams", "Salir"]
    opcion = menu(opciones_i)

    for playlist in lista_playlists:
        playlist.contador_escuchas(lista_playlists)
    for album in lista_albums:
        album.contador_escuchas(lista_albums)
    for oyente in lista_oyentes:
        oyente.contador_escuchas(lista_oyentes)
    for musicos in lista_musicos:
        musicos.contador_escuchas(lista_musicos)

    if opcion == "1":
        

        print("Top 5 de músicos con mayor cantidad de streams: ")
        top5 = sorted(lista_musicos, key=lambda x: x.escuchado, reverse=True)

        contador = 0
        while contador != 5:
            print(top5[contador].nombre, top5[contador].escuchado)
            contador = contador + 1

    elif opcion == "2":
        print("Top 5 de álbumes con mayor cantidad de streams: ")
        top5 = sorted(lista_albums, key=lambda x: x.escuchado, reverse=True)

        contador = 0
        while contador != 5:
            print(top5[contador].nombre, top5[contador].escuchado)
            contador = contador + 1

    elif opcion == "3":
        print("Top 5 de canciones con mayor cantidad de streams: ")
        top5 = sorted(lista_canciones, key=lambda x: x.escuchado, reverse=True)

        contador = 0
        while contador != 5:
            print(top5[contador].nombre, top5[contador].escuchado)
            contador = contador + 1

    elif opcion == "4":
        print("Top 5 de escuchas con mayor cantidad de streams: ")
        top5 = sorted(lista_oyentes, key=lambda x: x.escuchado, reverse=True)

        contador = 0
        while contador != 5:
            print(top5[contador].nombre, top5[contador].escuchado)
            contador = contador + 1

    elif opcion == "4":
        print("Ha salido del modeulo de indicadores")

#Esta funcion te arma los objetos en diccionario nuevamente y te los guarda en archivos txt
def cierre_txt(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado):
    usuarios=[]
    for usuario in todos_usuarios:
        if usuario.tipo_de_usuario == "musician":
            dicc = {
            "id":usuario.id,
            "name":usuario.nombre,
            "email":usuario.correo,
            "username":usuario.username,
            "type":usuario.tipo_de_usuario,
            "escuchado":usuario.escuchado,
            "usuarios_like":usuario.usuarios_like,
            "like":usuario.like,
            "albums":usuario.albums,
            }
        else:
            dicc = {
            "id":usuario.id,
            "name":usuario.nombre,
            "email":usuario.correo,
            "username":usuario.username,
            "type":usuario.tipo_de_usuario,
            "escuchado":usuario.escuchado,
            "playlists":usuario.playlists,
            }
        usuarios.append(dicc)
    
    albums=[]
    for album in lista_albums:
        dicc = {
        "id": album.id,
        "name": album.nombre,
        "description": album.descripcion,
        "cover": album.portada,
        "published": album.fecha,
        "genre": album.genero,
        "artist": album.tracklist,
        "tracklist": album.autor,
        "escuchado": album.escuchado,
        "usuarios_like": album.usuarios_like,
        "like": album.like,
        }
        albums.append(dicc)

    playlists=[]
    for playlist in lista_playlists:
        dicc = {
        "id": playlist.id,
        "name": playlist.nombre,
        "description": playlist.descripcion,
        "creator": playlist.lista_de_cancion,
        "tracks": playlist.creador,
        "escuchado": playlist.escuchado,
        "usuarios_like": playlist.usuarios_like,
        "like": playlist.like,
        }
        playlists.append(dicc)
     
    canciones=[]
    for cancion in lista_canciones:
        dicc = {
        "id": cancion.id,
        "name": cancion.nombre,
        "duration": cancion.duracion,
        "autor": cancion.autor,
        "link": cancion.link,
        "escuchado": cancion.escuchado,
        "usuarios_like": cancion.usuarios_like,
        "like": cancion.like,
        }
        canciones.append(dicc)


     
     
    

    with open("usuarios.txt", "w") as archivo:
        json_string = json.dumps(usuarios)
        archivo.write(json_string)
    
    with open("albums.txt", "w") as archivo:
        json_string = json.dumps(albums)
        archivo.write(json_string)

    with open("playlists.txt", "w") as archivo:
        json_string = json.dumps(playlists)
        archivo.write(json_string)
    
    with open("canciones.txt", "w") as archivo:
        json_string = json.dumps(canciones)
        archivo.write(json_string)

def obtener_info_txt(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists):
    informacion=""
    #obtiene la informacion del txt playlists
    with open("playlists.txt", "r") as archivo:
        informacion = archivo.read()
        informacion = json.loads(str(informacion))
    
    for playlist in informacion:
        nuevo_playlist = Playlist(playlist["id"], playlist["name"], playlist["description"], playlist["tracks"], playlist["creator"], playlist["escuchado"], playlist["usuarios_like"], playlist["like"])
        lista_playlists.append(nuevo_playlist)

    informacion = ""
    #obtiene la informacion del txt album
    with open("albums.txt", "r") as archivo:
        informacion = archivo.read()
        informacion = json.loads(str(informacion))
    for album in informacion:
        nuevo_album = Album(album["id"], album["name"], album["description"], album["cover"], album["published"], album["genre"], album["tracklist"], album["artist"], album["escuchado"], album["usuarios_like"], album["like"])
        lista_albums.append(nuevo_album)
    
    
    informacion = ""
    #obtiene la informacion del txt cancion
    with open("canciones.txt", "r") as archivo:
        informacion = archivo.read()
        informacion = json.loads(str(informacion))
    for cancion_dic in informacion:
        nueva_cancion = Cancion(cancion_dic["id"], cancion_dic["name"], cancion_dic["duration"], cancion_dic["autor"], cancion_dic["link"], cancion_dic["escuchado"], cancion_dic["usuarios_like"], cancion_dic["like"])
        lista_canciones.append(nueva_cancion)

    informacion=""
    #obtiene la informacion del txt usuario
    with open("usuarios.txt", "r") as archivo:
        informacion = archivo.read()
        informacion = json.loads(str(informacion))
    
    for usuario in informacion:
        if usuario["type"] == "listener":
            nuevo_usuario = Oyente(usuario["id"], usuario["name"], usuario["email"], usuario["username"], usuario["type"], usuario["escuchado"], usuario["playlists"])
            lista_oyentes.append(nuevo_usuario)
        else:
            nuevo_usuario = Musico(usuario["id"], usuario["name"], usuario["email"], usuario["username"], usuario["type"], usuario["escuchado"], usuario["usuarios_like"], usuario["like"], usuario["albums"])
            lista_musicos.append(nuevo_usuario)

        todos_usuarios.append(nuevo_usuario)
    

def main():
    todos_usuarios = []
    lista_musicos = []
    lista_oyentes = []
    lista_albums = []
    lista_canciones = []
    lista_playlists = []
    usuario_registrado = ""
    
    
    api(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists)

    print("¡Bienvenid@ a Metrotify! Regístrate!")

    #Pide el usuario y ve si existe en losregistros, si no lo manda a registrarse
    aux = 0
    usuario = input("Ingresa tu nombre de usuario: ")
    for perfil in todos_usuarios:
        if usuario.lower().split() == perfil.username.lower().split():
            aux= 1
            usuario_registrado = perfil

    if aux == 0:
        registro(todos_usuarios, lista_musicos, lista_oyentes, usuario_registrado)

    while True:
        #Opciones del menú
        opciones = ["Gestión de perfil", "Gestión musical", "Gestión de interacciones", "Indicadores", "Salir"]
        opcion_escogida = menu(opciones)

        if opcion_escogida == "1":
            print("\nGestión de perfil")
            gestion_de_perfil(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado)
        elif opcion_escogida == "2":
            print("\nGestión de musical")
            gestion_musical(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado)
        elif opcion_escogida == "3":
            print("\nGestión de interacciones")
            gestion_interaccion(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado)
        elif opcion_escogida == "4":
            print("\nIndicadores")
            indicadores(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado)
        else:
            cierre_txt(todos_usuarios, lista_musicos, lista_oyentes, lista_albums, lista_canciones, lista_playlists, usuario_registrado)
            print("Regrese pronto")
            break
            



main()