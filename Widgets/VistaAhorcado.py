import flet as ft

class VistaAhorcado(ft.SafeArea):
    def __init__(self, text):
        super().__init__()
        self.content = ft.Text(text)
    def update(self,text):
        self.content = ft.Text(text)
        return super().update()