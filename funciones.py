from passlib.hash import sha256_crypt
import pymysql
#'''
class Usuarios():
    def __init__(self, pNombre, sNombre, pApellido, sApellido, correo, usuario, password):
        self.pNomnbre = pNombre
        self.sNombre = sNombre
        self.pApellido = pApellido
        self.sApellido = sApellido
        self.correo = correo
        self.usuario = usuario
        self.password = password
#Cambiar los datos necesarios
def conectarse()->None:
    return pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='2117',
                                db='bd_practica')

def save_user(pNombre:str, sNombre:str, pApellido:str, sApelldio:str, correo:str, usuario:str, password:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(primerNombre, segundoNombre, apellidoPaterno, apellidoMaterno, correo, usuario, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (pNombre, sNombre, pApellido, sApelldio, correo, usuario, password))
    conexion.commit()
    conexion.close()
    
def get_usuario(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT usuario FROM usuarios WHERE usuario = " + '"' + user_name + '"')
        usuario = cursor.fetchone()
    conexion.close()
    us = usuario.__getitem__(0)
    return us

def get_datos_usuario(user_name:str)->list:
    datosU = ['','','','','','']
    conexion = conectarse()
    with conexion.cursor() as cursor:
        primerNombre = cursor.execute("SELECT primerNombre FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        primerNombre = cursor.fetchone()
        segundoNombre = cursor.execute("SELECT segundoNombre FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        segundoNombre = cursor.fetchone()
        apellidoPaterno = cursor.execute("SELECT apellidoPaterno FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        apellidoPaterno = cursor.fetchone()
        apellidoMaterno = cursor.execute("SELECT apellidoMaterno FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        apellidoMaterno = cursor.fetchone()
        correo = cursor.execute("SELECT correo FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        correo = cursor.fetchone()
        usuario = cursor.execute("SELECT usuario FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        usuario = cursor.fetchone()
    conexion.close()

    datosU[0] = primerNombre.__getitem__(0)
    datosU[1] = segundoNombre.__getitem__(0)
    datosU[2] = apellidoPaterno.__getitem__(0)
    datosU[3] = apellidoMaterno.__getitem__(0)
    datosU[4] = correo.__getitem__(0)
    datosU[5] = usuario.__getitem__(0)
    
    """"
    datosU.append(primerNombre.__getitem__(0))
    datosU.append(segundoNombre.__getitem__(0))
    datosU.append(apellidoPaterno.__getitem__(0))
    datosU.append(apellidoMaterno.__getitem__(0))
    datosU.append(correo.__getitem__(0))
    datosU.append(usuario.__getitem__(0))"""
    
    return datosU

def comprobar_usuario()->list:
    c_us = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT usuario FROM usuarios")
        c_usuario = cursor.fetchall()
    conexion.close()
    for i in range(len(c_usuario)):
        us = c_usuario.__getitem__(i)
        c_us.append(us.__getitem__(0))
    return c_us

def get_password(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        password = cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        password = cursor.fetchone()
    conexion.close() 
    for i in range(len(password)):
        pas = password.__getitem__(i)
    return pas 

def actualizar_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor = cursor.execute("UPDATE usuarios SET contraseña =" + "'" + password_cryp + "'" + " WHERE usuario = " + "'" + user_name + "'")
    conexion.commit()
    conexion.close()

def save_peliculas(nombre:str, clasificacion:str, duracion:float, imagen:str, sinopsis:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO peliculas(nombre, clasificacion, duracion, imagen, sinopsis) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, clasificacion, duracion, imagen, sinopsis))
    conexion.commit()
    conexion.close()
    
def get_pelicula(nPelicula:str)->list:
    peliculas = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        nombre = cursor.execute("SELECT nombre FROM peliculas WHERE nombre = '" + nPelicula + "'")
        nombre = cursor.fetchone()
        clasificaion = cursor.execute("SELECT clasificacion FROM peliculas WHERE nombre = '" + nPelicula + "'")
        clasificaion = cursor.fetchone()
        duracion = cursor.execute("SELECT duracion FROM peliculas WHERE nombre = '" + nPelicula + "'")
        duracion = cursor.fetchone()
        imagen = cursor.execute("SELECT imagen FROM peliculas WHERE nombre = '" + nPelicula + "'")
        imagen = cursor.fetchone()
        sinopsis = cursor.execute("SELECT sinopsis FROM peliculas WHERE nombre = '" + nPelicula + "'")
        sinopsis = cursor.fetchone()
    conexion.close() 
    for i in range(len(nombre)):
        peliculas.append(nombre.__getitem__(i))
        peliculas.append(clasificaion.__getitem__(i))
        peliculas.append(duracion.__getitem__(i))
        peliculas.append(imagen.__getitem__(i)) 
        peliculas.append(sinopsis.__getitem__(i))
    print(peliculas)
    return peliculas 

def get_peliculas()->list:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        nombre = cursor.execute("SELECT nombre FROM peliculas")
        nombre = cursor.fetchall()
        clasificaion = cursor.execute("SELECT clasificacion FROM peliculas")
        clasificaion = cursor.fetchall()
        duracion = cursor.execute("SELECT duracion FROM peliculas")
        duracion = cursor.fetchall()
        imagen = cursor.execute("SELECT imagen FROM peliculas")
        imagen = cursor.fetchall()
        sinopsis = cursor.execute("SELECT sinopsis FROM peliculas")
        sinopsis = cursor.fetchall()
    conexion.close() 
    n = len(nombre)
    peliculas = [[0 for x in range(5)] for j in range(n)]
    
    for i in range(len(nombre)):    
        nom = nombre.__getitem__(i)
        clas = clasificaion.__getitem__(i)
        dura = duracion.__getitem__(i)
        img = imagen.__getitem__(i)
        sin = sinopsis.__getitem__(i)
        peliculas[i][0] = (nom.__getitem__(0))
        peliculas[i][1] = (clas.__getitem__(0))
        peliculas[i][2] = (dura.__getitem__(0))
        peliculas[i][3] = (img.__getitem__(0))
        peliculas[i][4] = (sin.__getitem__(0))
        
    return peliculas
    
def save_post(usuario:str, titulo:str, descripcion:float)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO post(usuario, titulo, comentario) VALUES (%s, %s, %s)",
                       (usuario, titulo, descripcion))
    conexion.commit()
    conexion.close()

def get_post()->list:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT usuario FROM post" )
        usuario = cursor.fetchall()
        titulo = cursor.execute("SELECT titulo FROM post")
        titulo = cursor.fetchall()
        comentario = cursor.execute("SELECT comentario FROM post")
        comentario = cursor.fetchall()
    conexion.close() 
    n=len(usuario)
    comentarios = [[0 for x in range(3)] for j in range(n)]
    for i in range(len(usuario)):
        us = usuario.__getitem__(i)
        com = comentario.__getitem__(i)
        tit = titulo.__getitem__(i)
        comentarios[i][0] = us.__getitem__(0)
        comentarios[i][1] = tit.__getitem__(0)
        comentarios[i][2] = com.__getitem__(0)
    return comentarios 

def save_quejas(usuario:str, queja:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO quejas(usuario, queja) VALUES (%s, %s)",
                       (usuario, queja))
    conexion.commit()
    conexion.close()
    
def get_quejas()->list:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT usuario FROM quejas" )
        usuario = cursor.fetchall()
        queja = cursor.execute("SELECT queja FROM quejas")
        queja = cursor.fetchall()
    conexion.close() 
    n=len(usuario)
    quejas = [[0 for x in range(2)] for j in range(n)]
    for i in range(len(usuario)):
        us = usuario.__getitem__(i)
        quej = queja.__getitem__(i)
        quejas[i][0] = us.__getitem__(0)
        quejas[i][1] = quej.__getitem__(0)
    return quejas

#Referencia de los get: https://parzibyte.me/blog/2021/03/29/flask-mysql-ejemplo-conexion-crud/
