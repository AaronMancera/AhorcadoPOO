import flet as ft


class VistaAhorcado(ft.SafeArea):
    def __init__(self, text):
        super().__init__()
        self.adaptive=True
        self.top = True
        self.left = True
        self.content = ft.Container(
            content=ft.Text(text, text_align=ft.TextAlign.CENTER, font_family="Courier New"),
            adaptive= True,
            alignment=ft.alignment.center
            
        )

    def update(self, text):
        self.content = ft.Container(
            content=ft.Text(text, text_align=ft.TextAlign.CENTER, font_family="Courier New"),
            adaptive= True,
            alignment=ft.alignment.center
            
        )
        return super().update()
