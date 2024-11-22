from datetime import datetime, date


class Paciente:
    def __init__(self, id=None, nombre=None, fecha_nacimiento=None, telefono=None, email=None, ):
        self._id = id
        self._nombre = nombre

        if isinstance(fecha_nacimiento, str):
            # Si la fecha viene como string, intenta convertirla
            self._fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
        else:
            self._fecha_nacimiento = fecha_nacimiento

        self._telefono = telefono
        self._email = email

        # Asegurarte de que la fecha se almacene como un objeto date


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def fecha_nacimiento(self):
        """Devuelve la fecha de nacimiento en formato 'YYYY-MM-DD'."""
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha):
        """Permite establecer una nueva fecha, aceptando strings o objetos date."""
        if isinstance(fecha, str):
            self._fecha_nacimiento = datetime.strptime(fecha, '%Y-%m-%d').date()
        elif isinstance(fecha, date):
            self._fecha_nacimiento = fecha
        else:
            raise ValueError("La fecha debe ser un string en formato 'YYYY-MM-DD' o un objeto date.")

    def calcular_edad(self):
        """Calcula la edad del paciente en función de la fecha de nacimiento."""
        if not self._fecha_nacimiento:
            return None
        hoy = date.today()
        edad = hoy.year - self._fecha_nacimiento.year - (
                    (hoy.month, hoy.day) < (self._fecha_nacimiento.month, self._fecha_nacimiento.day))
        return edad

    def __str__(self):
        """Devuelve una representación legible del paciente."""
        return (f"Paciente(ID: {self._id}, Nombre: {self._nombre}, Teléfono: {self._telefono}, "
                f"Email: {self._email}, Fecha de nacimiento: {self._fecha_nacimiento}, Edad: {self.calcular_edad()})")