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
    
    #Agregarle cosas    
    try:
        conexion.execute("insert into personajes(nombre,apellido,anio) values (?,?,?)" , ("Marty", "Macfly", "1968"))
        conexion.execute("insert into personajes(nombre,apellido,anio) values (?,?,?)" , ("Emmet", "Brown", "1914"))
        conexion.commit() #Actualiza los datos realmente en la tabla
        print("Se agragaron cosas")
    except:
        print("error")
    
    #Seleccionar lineas
    borrar = True
    if borrar:
        cursor = conexion.execute("SELECT * FROM personajes")
        for fila in cursor:
            id = (fila[0])
            sentencia = "delete from personajes WHERE id=?"
            cursor = conexion.execute(sentencia, str(id))
            
    # sentencia = "SELECT * FROM personajes WHERE id=?" 
    # cursor = conexion.execute(sentencia, (id,))
    # for fila in cursor:
    #     print(fila)
    
