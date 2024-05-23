import flet as ft

from Ahorcado.AhorcadoModel import AhorcadoModel
from Ahorcado.AhorcadoView import AhorcadoView
from Widgets.AhorcadoWidget import AhorcadoWidget
from Widgets.CampoDeTextoWidget import CampoDeTextoWidget


def Game(page, ruta):
    # Creacion en vacio de la columna
    content = ft.ResponsiveRow([ft.Container(ft.Text("Vacio"))])
    # Se pone esto para que no se ejecute sin entrar en esta pantalla, ya que flet carga todas las vistas al llamar la funcion de myRoutes() de Views.py
    if ruta == "/game":
        path = "./data/palabras.txt"
        VIDA = 6
        model = AhorcadoModel(path=path, vida=VIDA)
        model.elegir_palabra()
        viewTerminal = AhorcadoView()
        viewTerminal.preparar_juego_visual(model.get_palabra_elegida())
        model.registrar_nuevo_observador(viewTerminal)
        # Inicia la partida y necesitamos previsualizar el ahorcado

        visual_ahorcado_widget = AhorcadoWidget(
            text=viewTerminal.dibujar_ahorcado(
                model.get_vida(), model.get_palabra_elegida()
            ),
            view=viewTerminal,
        )
        mostrar_juego = ft.ResponsiveRow()

        # page.add(visual_ahorcado_widget)
        # mostrar_juego.controls.append(visual_ahorcado_widget)

        # Inicializacmos el campo de texto y lo añadimos a la pantalla
        campo_de_texto_widget = CampoDeTextoWidget(
            model=model, ahorcado_dibujado=visual_ahorcado_widget
        )
        # page.add(campo_de_texto_widget)
        # mostrar_juego.controls.append(
        #     campo_de_texto_widget
        # )

        def btn_go_to_home(e):
            page.go("/")
            page.update()

        # mostrar_juego.controls.append(
        #     ft.ElevatedButton(
        #             text="Ir para el juego", on_click=btn_go_to_home
        #         )
        # )
        mostrar_juego = ft.ResponsiveRow(
            [
                visual_ahorcado_widget,
                ft.Container(
                    campo_de_texto_widget,
                    bgcolor=ft.colors.RED,
                ),
                ft.Container(
                    col={"sm": 2},
                    content=ft.TextButton(
                        content=ft.Row(
                            [ft.Icon(name=ft.icons.HOME)],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                        on_click=btn_go_to_home,
                        adaptive=True,
                    ),
                    bgcolor=ft.colors.YELLOW,
                    width=150,
                ),
            ]
        )
        content = mostrar_juego

    return content
