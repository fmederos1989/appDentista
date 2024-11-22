import flet as ft

def pagina_dashboard(page: ft.Page) -> ft.View:
    # Función para manejar redirecciones
    def ir_a_seccion(e, ruta):
        page.go(ruta)

    # Botones de acceso a las secciones
    btn_pacientes = ft.ElevatedButton(
        "Gestión de Pacientes",
        icon=ft.icons.PERSON,
        on_click=lambda e: ir_a_seccion(e, "/pacientes"),
    )

    btn_agenda = ft.ElevatedButton(
        "Agenda de Citas",
        icon=ft.icons.CALENDAR_TODAY,
        on_click=lambda e: ir_a_seccion(e, "/agenda"),
    )

    btn_tratamientos = ft.ElevatedButton(
        "Tratamientos",
        icon=ft.icons.HEALTH_AND_SAFETY,
        on_click=lambda e: ir_a_seccion(e, "/tratamientos"),
    )

    btn_finanzas = ft.ElevatedButton(
        "Gestión Financiera",
        icon=ft.icons.ATTACH_MONEY,
        on_click=lambda e: ir_a_seccion(e, "/finanzas"),
    )

    btn_perfil = ft.ElevatedButton(
        "Configuración del Perfil",
        icon=ft.icons.SETTINGS,
        on_click=lambda e: ir_a_seccion(e, "/perfil"),
    )

    # Layout del dashboard
    return ft.View(
        "/dashboard",
        controls=[
            ft.Text("Dashboard - Sistema de Gestión", size=24),
            ft.Divider(),
            ft.Column(
                [
                    btn_pacientes,
                    btn_agenda,
                    btn_tratamientos,
                    btn_finanzas,
                    btn_perfil,
                ],
                spacing=10,
            ),
        ],
    )