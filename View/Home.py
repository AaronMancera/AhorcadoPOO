from typing import Any, List
import flet as ft


def Home(page):
    print("Inicia el home")

    # bienvenida.controls.append(ft.Text("Bienvenido al juego del Ahorcado POO"))
    def btn_go_to_game(e):
        page.go("/game")
        page.update()

    # bienvenida.controls.append(ft.ElevatedButton(text="Ir para el juego",on_click=btn_go_to_game))

    content = ft.ResponsiveRow(
        [
            ft.Container(
                #https://github.com/flet-dev/flet/discussions/2545
                content=ft.Column(
                    controls=[
                        ft.Image(
                            src="../assets/Img/test.svg",
                            fit=ft.ImageFit.CONTAIN,
                            expand=True,
                        )
                    ],
                    height=200,
                    expand=True,
                ),
                col={"md": 12, "lg": 4, "xl": 3},
                alignment=ft.alignment.top_center,
                bgcolor=ft.colors.YELLOW,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton(
                            text="Ir para el juego", on_click=btn_go_to_game
                        )
                    ],
                ),
                col={"md": 12, "lg": 8, "xl": 9},
                bgcolor=ft.colors.GREEN,
            ),
        ]
    )
    return content
