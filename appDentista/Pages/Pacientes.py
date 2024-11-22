import flet as ft
from appDentista.Clases.paciente import Paciente
from appDentista.Services.servicios import Servicios

def pagina_pacientes(page : ft.Page):
    id_dentista = page.client_storage.get('dentista_id')
    print(id_dentista)
    pacientes = []
    consulta_pacientes = Servicios.obtener_pacientes(id_dentista)
    pacientes.append(consulta_pacientes)
    print(pacientes)

    tabla_pacientes = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Edad")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[],
    )

    # Función para actualizar la tabla
    def actualizar_tabla():
        tabla_pacientes.rows.clear()
        for paciente in consulta_pacientes:
            tabla_pacientes.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(paciente.id))),
                        ft.DataCell(ft.Text(paciente.nombre)),
                        ft.DataCell(ft.Text(str(paciente.telefono)),),
                        ft.DataCell(ft.Text(paciente.email)),
                        ft.DataCell(ft.Text(str(Paciente.calcular_edad(paciente)))),
                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.icons.EDIT,
                                        on_click=lambda e, p=paciente: editar_paciente(p),
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.DELETE,
                                        on_click=lambda e, p=paciente: eliminar_paciente(p),
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            )
        page.update()

    # Campos de entrada para el diálogo de agregar/editar pacientes
    nombre_field = ft.TextField(label="Nombre")
    fecha_nacimiento = ft.TextField(label="Fecha Nacimiento")
    telefono_field = ft.TextField(label="Teléfono")
    email_field = ft.TextField(label="Email")

    # Función para agregar un nuevo paciente
    def agregar_paciente(e):
        nombre = nombre_field.value
        f_nacimiento = fecha_nacimiento.value
        telefono = telefono_field.value
        email = email_field.value
        paciente_nuevo = Paciente(nombre, f_nacimiento, telefono, email)
        Servicios.registrar_paciente(paciente_nuevo, id_dentista)
        pacientes.append(paciente_nuevo)
        actualizar_tabla()
        dialog_agregar.open = False
        page.update()

    # Función para editar un paciente
    def editar_paciente(paciente):
        nombre_field.value = paciente.nombre
        fecha_nacimiento.value = str(paciente.fecha_nacimiento)
        telefono_field.value = paciente.telefono
        email_field.value = paciente.email

        def guardar_cambios(e):
            paciente.nombre = nombre_field.value
            paciente.fecha_nacimiento = fecha_nacimiento.value
            paciente.telefono = telefono_field.value
            paciente.email = email_field.value


            actualizar_tabla()
            dialog_editar.open = False
            page.update()

        dialog_editar.actions = [ft.TextButton("Guardar", on_click=guardar_cambios)]
        dialog_editar.open = True
        page.update()

    # Función para eliminar un paciente
    def eliminar_paciente(paciente):
        pacientes.remove(paciente)
        actualizar_tabla()


    # Diálogo para agregar pacientes
    dialog_agregar = ft.AlertDialog(
        title=ft.Text("Agregar Paciente"),
        content=ft.Column([nombre_field, fecha_nacimiento, telefono_field, email_field]),
        actions=[ft.TextButton("Agregar", on_click=agregar_paciente)],
    )

    # Diálogo para editar pacientes
    dialog_editar = ft.AlertDialog(
        title=ft.Text("Editar Paciente"),
        content=ft.Column([nombre_field, fecha_nacimiento, telefono_field, email_field]),
    )

    def abrir_dialog_agregar():
        dialog_agregar.open = True
        page.update()

    # Botón para abrir el diálogo de agregar pacientes
    btn_agregar = ft.FloatingActionButton(
        text="Agregar Paciente",
        icon=ft.icons.ADD,
        on_click=lambda e: (abrir_dialog_agregar()),
    )

    # Cargar tabla inicial
    actualizar_tabla()

    return ft.View(
        "/pacientes",
        [
            ft.AppBar(title=ft.Text("Pacientes"), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
            ft.Column(
                [
                    tabla_pacientes,
                    btn_agregar,
                ]
            ),
            dialog_agregar,
            dialog_editar,
            ft.ElevatedButton("Volver", on_click=lambda _: page.go("/dashboard")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
