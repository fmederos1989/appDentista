import logging

import flet as ft
from appDentista.Services.servicios import Servicios

def pagina_login(page: ft.Page):
    usuario_field = ft.TextField(label="Usuario",
                                 value='fmederos',
                                 width=300,
                                 on_focus=True,
                                 bgcolor=ft.colors.SURFACE_VARIANT)
    contrasena_field = ft.TextField(label="Contraseña",
                                    value='pass123',
                                    password=True,
                                    can_reveal_password=True,
                                    width=300,
                                    bgcolor=ft.colors.SURFACE_VARIANT)
    status_message = ft.Text(value="", color=ft.colors.RED)

    def handle_login(e):
        usuario = usuario_field.value
        contrasena = contrasena_field.value

        # Llamar a la función de verificación de credenciales y almacenar el user_id
        user_id = Servicios.verify_credentials(usuario, contrasena)
        print(user_id)

        if user_id:
            status_message.value = "¡Inicio de sesión exitoso!"
            status_message.color = ft.colors.GREEN

            # Aquí almacenamos el ID del dentista
            id_dentista = user_id

            # Redirigir al dashboard pasando el id_dentista como parámetro de la URL
            page.go("/dashboard", data={"id_dentista": id_dentista})

        else:
            status_message.value = "Usuario o contraseña incorrectos."
            status_message.color = ft.colors.RED

        page.update()
        # Retornamos el id_dentista para su uso posterior si es necesario

    return ft.View(
        "/login",
        [
            ft.AppBar(title=ft.Text("Iniciar Sesión"),
                      bgcolor=ft.colors.SURFACE_VARIANT,
                      center_title=True),
            ft.Container(
                ft.Column([
                    usuario_field,
                    contrasena_field,
                    ft.TextButton("Iniciar Sesión", on_click=handle_login),
                    status_message,
                    ft.TextButton("Volver", on_click=lambda _: page.go("/"),),
                ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrado de los botones
                    spacing=20
                ),
                padding=ft.padding.all(20),  # Padding alrededor del contenido
                bgcolor=ft.colors.BLUE_GREY_700,  # Fondo azul suave
                border_radius=12,  # Bordes redondeados
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
