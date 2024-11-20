import bcrypt
from logger_base import log
from cursor_del_pool import CursorDelPool
from Clases.dentista import Dentista

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
        :return: True si las credenciales son válidas, False en caso contrario
        """
        try:
            with CursorDelPool() as cursor:
                # Buscar el usuario por nombre
                query = "SELECT contrasena FROM dentistas WHERE usuario = %s"
                cursor.execute(query, (username,))
                result = cursor.fetchone()

            if result:
                stored_hash = result[0]
                # Verificar la contraseña
                return bcrypt.checkpw(password.encode(), stored_hash.encode())
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


if __name__ == "__main__":
    # Test de verificación de credenciales
    username = "fmederos"
    password = "pass123"
    is_valid = Servicios.verify_credentials(username, password)
    print(f"Credenciales válidas: {is_valid}")