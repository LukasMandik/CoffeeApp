import flet as ft


class ProductCard:

    def __init__(self, page):
        self.page = page
        self.page.horizontal_alignment = 'center'
        self.page.vertical_alignment = 'center'

        self.product_card = ft.Container(
            width=300,
            height=400,
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=ft.animation.Animation(
                duration=350,
                curve="decelerate"),
            on_hover=lambda e: _expand(e),
        )

        self._c = ft.Container(
            # width=310,
            # height=660,
            # border_radius=35,
            # bgcolor="black",
            # padding=10,
            content=ft.Stack(
                # width=300,
                # height=450,
                controls=[self.product_card, self.product_card],
            ),
        )

        def _expand(e):
            if e.data == "true":
                self._c.content.controls[0].height = 405
                self._c.content.controls[0].width = 305
                self._c.content.controls[0].update()
            else:
                self._c.content.controls[0].height = 400
                self._c.content.controls[0].width = 300
                self._c.content.controls[0].update()
            pass

        self.page.add(self._c)
        self.page.update()
