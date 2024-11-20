class Dentista:
    def __init__(self, id=None, nombre=None, especialidad=None, telefono=None, email=None, usuario=None, contrasena=None):
        self._id = id
        self._nombre = nombre
        self._especialidad = especialidad
        self._telefono = telefono
        self._email = email
        self._usuario = usuario
        self._contrasena = contrasena

    def __str__(self):
        return f'''
        ID: {self._id}
        Nombre: {self._nombre}
        Especialidad: {self._especialidad}
        Teléfono: {self._telefono}
        Email: {self._email}
        Usuario: {self._usuario}
        '''

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
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        self._especialidad = especialidad

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
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

