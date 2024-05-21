import flet as ft

from Ahorcado.AhorcadoView import AhorcadoView


class AhorcadoWidget(ft.Container):
    def __init__(self, text, view:AhorcadoView):
        """Genera un widget donde se dibujara el ahorcado

        Args:
            text (_type_): El texto que se va a mostrar como figura del ahorcado
            view (AhorcadoView): El control de vista del ahorcado que se encargara de actualizar el dibujo
        """
        super().__init__()
        
        self.view = view
        self.adaptive=True
        self.top = True
        self.left = True
        self.content = ft.Container(
            bgcolor=ft.colors.YELLOW,
            content=ft.Text(text, text_align=ft.TextAlign.CENTER, font_family="Courier New"),            
        )        

    def update(self, text):
        """Actualizacion de la vista

        Args:
            text (_type_): El texto que se va a mostrar como figura del ahorcado

        Returns:
            _type_: Devuelve el mismo widget con los cambios realizados
        """
        self.content = ft.Container(
            col={
                    "sm": 6,
                    "md": 4,
                    "xl": 2,
                },
            content=ft.Text(text, text_align=ft.TextAlign.CENTER, font_family="Courier New"),            
        )
        return super().update()


    def avanzar_partida(self,vidas:int,palabra:str):
        """Actualiza el dibujo del ahorcado al progreso actual

        Args:
            vidas (int): vidas restantes del jugador
            palabra (str): palabra buscada, por si el jugador pierde mencionarsela
        """
        self.update(self.view.dibujar_ahorcado(vidas=vidas,palabra_buscada=palabra))
