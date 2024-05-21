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
        # mostrar_juego = ft.ResponsiveRow(
        #     [
        #         ft.Container(
        #             ft.Text("Column 1"),
        #             bgcolor=ft.colors.RED,
        #             col={"sm": 6, "md": 4, "xl": 2},
        #         ),
        #         ft.Container(
        #             ft.Text("Column 1"),
        #             bgcolor=ft.colors.RED,
        #             col={"sm": 6, "md": 4, "xl": 2},
        #         ),
        #         ft.Container(
        #             ft.Text("Column 1"),
        #             bgcolor=ft.colors.RED,
        #             col={"sm": 6, "md": 4, "xl": 2},
        #         ),
        #     ]
        # )

        # page.add(visual_ahorcado_widget)
        mostrar_juego.controls.append(
            visual_ahorcado_widget
        )
        # Inicializacmos el campo de texto y lo añadimos a la pantalla
        campo_de_texto_widget = CampoDeTextoWidget(
            model=model, ahorcado_dibujado=visual_ahorcado_widget
        )
        # page.add(campo_de_texto_widget)
        # mostrar_juego.controls.append(
        #     ft.Column(
        #         col={
        #             "sm": 6,
        #             "md": 4,
        #             "xl": 2,
        #         },
        #         controls=campo_de_texto_widget,
        #     )
        # )

        def btn_go_to_home(e):
            page.go("/")
            page.update()

        # mostrar_juego.controls.append(
        #     ft.Column(
        #         col={
        #             "sm": 6,
        #             "md": 4,
        #             "xl": 2,
        #         },
        #         controls=ft.ElevatedButton(
        #             text="Ir para el juego", on_click=btn_go_to_home
        #         ),
        #     )
        # )
        content = mostrar_juego

    return content
