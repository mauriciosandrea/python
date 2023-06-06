class PersonaDao:
    '''
    Dao significa :data acces object
    crud significa
            create----insertar
            read----seleccionar
            update-----Actualizar
            Delete-----Eliminar
    '''

    _SELECCIONAR ='SELECT * FROM persona ORDER BY id_persona '
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
    __ACTUALIZAR ='UPDATE persona SET nombre = %s, apellido =%s, email=%s WHERE id_persona=%s'
    __DELETE ='DELETE FROM persona WHERE id_persona=%s'