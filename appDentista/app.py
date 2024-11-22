import flet as ft
from Pages.PaginaInicial import pagina_inicial
from Pages.PaginaRegistro import pagina_registro
from Pages.dashboard import pagina_dashboard
from Pages.Pacientes import pagina_pacientes


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
            page.views.append(pagina_inicial(page))  # Página de login
        elif page.route == "/registro":
            page.views.append(pagina_registro(page))  # Página de registro
        elif page.route == "/dashboard":
            page.views.append(pagina_dashboard(page))  # Página de dashboard
        elif page.route == "/pacientes":
            page.views.append(pagina_pacientes(page))  # Página de pacientes

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
