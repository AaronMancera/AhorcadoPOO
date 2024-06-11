import flet as ft

from View.Game import Game
from View.Home import Home

# https://github.com/flet-dev/flet/discussions/2748


def myRoutes(page: ft.Page, ruta: str):
    """Contiene las rutas de la aplicaicon y al pasarle un string devuelve dicha vista

    Args:
        page (ft.Page): Pagina principal del main
        ruta (str): Ruta a la que queremos acceder

    Returns:
        _type_: Devuelve la busqueda de la ruta dentro de las rutas que tenemos registradas
    """

    routes = {"/": Home(page), "/game": Game(page, ruta)}

    return routes[ruta]


class Views:
    """La clase que se va a encargar de gestionar las vistas de la app"""

    def __init__(self, page=ft.Page):
        """Inicializar el gestor de vistas

        Args:
            page (_type_): pagina de la app que se realiza en el main
        """

        self.page = page
        self.ft = ft
        # La pagina en la que queremos que se inicialice la pagina, en este caso el main "/"
        self.body = ft.Container(
            content=myRoutes(page, "/"),
            # bgcolor=ft.colors.RED,
            # FIX: Por alguna extraña razon no pilla el svg
            image_src='/Img/fondoSimple.png',
            image_fit=ft.ImageFit.COVER,
            # TODO: Da aqui un error que al hacerse responsivo deja de expandirse
            expand=True
        )

        def page_resize(e):
            page.value = f"{page.width} px"
            print(page.value)
            page.update()

        self.page.on_resize = page_resize

    def route_change(self, route):
        """Funcion para cambiar la ruta

        Args:
            route (_type_): ruta
        """

        print("rute: ", route.route)
        self.body.content = myRoutes(self.page, route.route)
        self.body.update()
