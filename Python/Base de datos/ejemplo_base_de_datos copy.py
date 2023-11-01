import sqlite3

with sqlite3.connect("Python/Base de datos/bd_ejemplo.db") as conexion:
    #Crar tabla
    try:
        sentencia = """ create table personajes
                        (
                                id integer primary key autoincrement,
                                nombre text,
                                apellido text,
                                anio real    
                        )
        
                    """
        conexion.execute(sentencia)
        print("Se creo la tabla de personajes")
    
    #Problemas con la creación de la tabla
    except sqlite3.OperationalError:
        print("La tabla de personajes ya existe")
        sentencia = "delete from personajes"
        cursor = conexion.execute(sentencia)
        conexion.execute("insert into personajes(nombre,apellido,anio) values (?,?,?)" , ("Naruto", "Uzumaki", "12"))
        conexion.execute("insert into personajes(nombre,apellido,anio) values (?,?,?)" , ("Sasuke", "Uchiha", "12"))
        conexion.execute("insert into personajes(nombre,apellido,anio) values (?,?,?)" , ("Sakura", "Haruno", "12"))
        conexion.commit() #Actualiza los datos realmente en la tabla
        print("Se borraron los datos anteriores y se agragaron nuevos")
    
    #Agregarle cosas    
    else:
        try:
            conexion.execute("insert into personajes(nombre,apellido,anio) values (?,?,?)" , ("Marty", "Macfly", "1968"))
            conexion.execute("insert into personajes(nombre,apellido,anio) values (?,?,?)" , ("Emmet", "Brown", "1914"))
            conexion.commit() #Actualiza los datos realmente en la tabla
            print("Se agragaron datos")
        except:
            print("error")

    
