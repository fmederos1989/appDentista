import flet as ft
from appDentista.Services.servicios import Servicios
from appDentista.Clases.dentista import Dentista

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
