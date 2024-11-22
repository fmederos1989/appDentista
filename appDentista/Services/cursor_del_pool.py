from appDentista.Services.logger_base import log
from appDentista.Services.Conexiones import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        # log.debug("Inicio del método whit __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        # log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Error en la transacción, se hace rollback: {valor_excepcion} / {tipo_excepcion} / {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Transacción exitosa')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        # log.debug('Dentro del bloque WIHT')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
