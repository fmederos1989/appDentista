from datetime import datetime, date

import bcrypt
from appDentista.Services.logger_base import log
from appDentista.Services.cursor_del_pool import CursorDelPool
from appDentista.Clases.paciente import Paciente


class Servicios:
    '''
    DAO significa (Data Access Object)
    CRUD (Create - Read - Update - Delete)
    '''
    @staticmethod
    def verify_credentials(username, password):
        """
        Verifica las credenciales del usuario en la base de datos.
        :param username: Nombre de usuario
        :param password: Contraseña ingresada por el usuario
        :return: El id del usuario si las credenciales son válidas, False en caso contrario
        """
        try:
            with CursorDelPool() as cursor:
                # Buscar el usuario por nombre
                query = "SELECT contrasena, id FROM dentistas WHERE usuario = %s"
                cursor.execute(query, (username,))
                result = cursor.fetchone()

            if result:
                stored_hash = result[0]
                # Verificar la contraseña
                if bcrypt.checkpw(password.encode(), stored_hash.encode()):
                    user_id = result[1]  # Guardamos el id del usuario
                    return user_id  # Retornamos el id del usuario
                else:
                    return False
            return False
        except Exception as e:
            log.error(f"Error durante la verificación de credenciales: {e}")
            return False

    @staticmethod
    def registrar_dentista(dentista):
        """
        Registra un nuevo dentista en la base de datos.
        :param dentista: Objeto de la clase Dentista con los datos del nuevo dentista
        :return: True si el registro fue exitoso, False en caso contrario
        """
        try:
            # Hashear la contraseña
            hashed_password = bcrypt.hashpw(dentista.contrasena.encode(), bcrypt.gensalt()).decode()

            with CursorDelPool() as cursor:
                # Insertar el nuevo dentista
                query = """
                INSERT INTO dentistas (nombre, especialidad, telefono, email, usuario, contrasena)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                valores = (
                    dentista.nombre,
                    dentista.especialidad,
                    dentista.telefono,
                    dentista.email,
                    dentista.usuario,
                    hashed_password,
                )
                cursor.execute(query, valores)

            log.info(f"Dentista registrado exitosamente: {dentista.usuario}")
            return True
        except Exception as e:
            log.error(f"Error al registrar el dentista: {e}")
            return False

    @staticmethod
    def registrar_paciente(paciente, dentista_id):
        """
        Registra un nuevo paciente en la base de datos.
        :param paciente: Objeto de la clase Paciente con los datos del nuevo paciente
        :return: True si el registro fue exitoso, False en caso contrario
        """
        try:
            with CursorDelPool() as cursor:
                # Asegurar que fecha_nacimiento esté en formato adecuado
                if isinstance(paciente.fecha_nacimiento, datetime):
                    fecha_formateada = paciente.fecha_nacimiento.date()  # Convertir a date
                elif isinstance(paciente.fecha_nacimiento, date):
                    fecha_formateada = paciente.fecha_nacimiento  # Ya es un objeto date
                elif isinstance(paciente.fecha_nacimiento, str):
                    # Convertir string a date si no lo está
                    fecha_formateada = datetime.strptime(paciente.fecha_nacimiento, '%Y-%m-%d').date()
                else:
                    raise ValueError("El formato de fecha_nacimiento no es válido.")

                # Insertar el nuevo paciente
                query = """
                    INSERT INTO pacientes (nombre, fecha_nacimiento, telefono, email, dentista_id)
                    VALUES (%s, %s, %s, %s, %s)
                    """
                valores = (
                    paciente.nombre,
                    fecha_formateada,  # Aseguramos que la fecha esté en formato adecuado
                    paciente.telefono,
                    paciente.email,
                    dentista_id,
                )
                cursor.execute(query, valores)

            log.info(f"Paciente registrado exitosamente: {paciente.nombre}")
            return True
        except Exception as e:
            log.error(f"Error al registrar el paciente: {e}")
            return False

    @staticmethod
    def obtener_pacientes(id_dentista):
        """
        Obtiene todos los pacientes registrados en la base de datos para un dentista específico.
        :param id_dentista: ID del dentista cuyos pacientes se quieren obtener.
        :return: Lista de objetos de la clase Paciente
        """
        try:
            pacientes = []
            with CursorDelPool() as cursor:
                # Obtener todos los pacientes
                query = """
                    SELECT id, nombre, fecha_nacimiento, telefono, email 
                    FROM pacientes 
                    WHERE dentista_id = %s
                    """
                cursor.execute(query, (id_dentista,))
                result = cursor.fetchall()
                print(result)  # Para depuración

            for row in result:
                # Asegurarnos de que fecha_nacimiento sea un string en formato 'YYYY-MM-DD'
                fecha_nacimiento = row[2]
                if isinstance(fecha_nacimiento, datetime):
                    fecha_nacimiento = fecha_nacimiento.date()  # Convertir a objeto date
                elif isinstance(fecha_nacimiento, str):
                    # Si la base de datos ya devuelve un string, asegurarse del formato
                    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()

                # Crear el objeto Paciente
                paciente = Paciente(
                    id=row[0],
                    nombre=row[1],
                    fecha_nacimiento=fecha_nacimiento,
                    telefono=row[3],
                    email=row[4],
                )
                pacientes.append(paciente)

            return pacientes
        except Exception as e:
            log.error(f"Error al obtener los pacientes: {e}")
            return []




if __name__ == "__main__":
    # Test de verificación de credenciales
    # username = "fmederos"
    # password = "pass123"
    # is_valid = Servicios.verify_credentials(username, password)
    # print(f"Credenciales válidas: {is_valid}")

    #! Test obtener pacientes
    # id_dentista = 3
    # pacientes = Servicios.obtener_pacientes(id_dentista)
    # for paciente in pacientes:
    #     print(f"Paciente: {paciente.nombre}, {paciente.fecha_nacimiento}, {paciente.telefono}, {paciente.email}")

    #! Test registrar paciente
    paciente = Paciente(nombre="Test Paciente", fecha_nacimiento="1990-01-01", telefono="123456789", email="test@example.com")
    is_registered = Servicios.registrar_paciente(paciente, 3)
    print(f"Registro de paciente exitoso: {is_registered}")