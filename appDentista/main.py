import flet as ft
from servicios import Servicios
from Clases.dentista import Dentista

# Página de inicio (página principal)
def pagina_inicial(page: ft.Page):
    # Contenedor principal para la vista
    return ft.View(
        "/",
        [
            ft.AppBar(
                title=ft.Text("Sistema de Gestión Odontológico"),
                bgcolor=ft.colors.SURFACE_VARIANT,
                center_title=True

            ),
            # Contenedor que centra el contenido
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton(
                            "Iniciar Sesión",
                            on_click=lambda _: page.go("/login"),
                            bgcolor=ft.colors.PRIMARY,
                            color=ft.colors.WHITE,
                            width=200,
                            height=50,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12)
                            )
                        ),
                        ft.ElevatedButton(
                            "Registrarse",
                            on_click=lambda _: page.go("/registro"),
                            bgcolor=ft.colors.SECONDARY,
                            color=ft.colors.WHITE,
                            width=200,
                            height=50,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12)
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,# Centrado de los botones
                    spacing=20  # Espacio entre los botones
                ),
                padding=ft.padding.all(20),  # Padding alrededor del contenido
                bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo azul suave
                border_radius=12,  # Bordes redondeados
                width=350,  # Tamaño fijo para el contenedor
                height=300,  # Tamaño fijo para el contenedor

            ),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrado horizontalmente
    )

# Página de inicio de sesión
def pagina_login(page: ft.Page):
    usuario_field = ft.TextField(label="Usuario", width=300)
    contrasena_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)

    status_message = ft.Text(value="", color=ft.colors.RED)

    def handle_login(e):
        usuario = usuario_field.value
        contrasena = contrasena_field.value

        if Servicios.verify_credentials(usuario, contrasena):
            status_message.value = "¡Inicio de sesión exitoso!"
            status_message.color = ft.colors.GREEN
        else:
            status_message.value = "Usuario o contraseña incorrectos."
            status_message.color = ft.colors.RED

        page.update()

    return ft.View(
        "/login",
        [
            ft.AppBar(title=ft.Text("Iniciar Sesión"), bgcolor=ft.colors.SURFACE_VARIANT),
            usuario_field,
            contrasena_field,
            ft.ElevatedButton("Iniciar Sesión", on_click=handle_login),
            status_message,
            ft.TextButton("Volver", on_click=lambda _: page.go("/")),
        ]
    )
def pagina_registro(page: ft.Page):
    nombre_field = ft.TextField(label="Nombre", width=300)
    especialidad_field = ft.TextField(label="Especialidad", width=300)
    telefono_field = ft.TextField(label="Teléfono", width=300)
    email_field = ft.TextField(label="Email", width=300)
    usuario_field = ft.TextField(label="Usuario", width=300)
    contrasena_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)

    status_message = ft.Text(value="", color=ft.colors.RED)

    def handle_register(e):
        try:
            dentista = Dentista(
                nombre=nombre_field.value,
                especialidad=especialidad_field.value,
                telefono=telefono_field.value,
                email=email_field.value,
                usuario=usuario_field.value,
                contrasena=contrasena_field.value,
            )

            if Servicios.registrar_dentista(dentista):
                status_message.value = "¡Registro exitoso!"
                status_message.color = ft.colors.GREEN
            else:
                status_message.value = "Error al registrar el dentista."
                status_message.color = ft.colors.RED
        except Exception as ex:
            status_message.value = f"Error: {ex}"
            status_message.color = ft.colors.RED

        page.update()

    return ft.View(
        "/registro",
        [
            ft.AppBar(title=ft.Text("Registro de Dentista"), bgcolor=ft.colors.SURFACE_VARIANT),
            nombre_field,
            especialidad_field,
            telefono_field,
            email_field,
            usuario_field,
            contrasena_field,
            ft.ElevatedButton("Registrar", on_click=handle_register),
            status_message,
            ft.TextButton("Volver", on_click=lambda _: page.go("/")),
        ]
    )

# Función principal
def main(page: ft.Page):
    page.title = "App Dentista"

    # Inicializar la vista principal explícitamente
    # page.views.append(pagina_inicial(page))  # Agregar la vista principal
    # page.update()  # Actualizar la página

    # Asignar vistas y rutas
    def route_change(route):
        page.views.clear()  # Limpiar vistas previas
        # Dependiendo de la ruta, agregar la vista correspondiente
        if page.route == "/":
            page.views.append(pagina_inicial(page))  # Página principal
        elif page.route == "/login":
             page.views.append(pagina_login(page))  # Página de login
        elif page.route == "/registro":
             page.views.append(pagina_registro(page))  # Página de registro

        page.update()  # Actualizar la página para reflejar los cambios

    # Función para manejar el pop de la vista (cuando el usuario navega hacia atrás)
    def view_pop(view):
        page.views.pop()  # Eliminar la vista actual
        top_view = page.views[-1]  # Recuperar la vista anterior
        page.go(top_view.route)  # Navegar a la vista anterior

    # Asignar los eventos para el cambio de ruta y retroceder en las vistas
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Inicializar la vista en la página principal
    page.go("/")  # Navegar a la página principal al iniciar

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=main)
