import flet as ft
import json


class ProductSection:

    def __init__(self, page):
        self.page = page
        # self.page.horizontal_alignment = 'center'
        # self.page.vertical_alignment = 'center'

        self.All_Product = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=250,
            child_aspect_ratio=1.0,
            spacing=15,
            run_spacing=15,
        )
        self.s = []
        with open('data.json') as json_file:
            data = json.load(json_file)
            self.s = data

        self.page.add(self.All_Product)

        for x in self.s:
            self.All_Product.controls.append(
                ft.Stack(controls=[
                    ft.Image(
                        width=200,
                        height=200,
                        src="/assets/images/" + x["image"],
                        fit=ft.ImageFit.COVER,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                        border_radius=ft.border_radius.all(10)
                    ),
                    ft.Text(
                        value=x["name"],
                        size=18,
                        weight="bold",
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                        left=10,

                    ),
                    ft.Text(
                        value=x["price"],
                        size=18,
                        weight="bold",
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                        right=12,
                        bottom=12

                    )
                ]
                )
            )
        self.page.update()





        self.Animate_Container = ft.Container(
            self.All_Product,
            width=320,
            height=420,
            # bgcolor="black",
            padding=10,
            border_radius=10,
            offset=ft.transform.Offset(0, 3),
            animate_offset=ft.animation.Animation(700),

        )

        def animate(e):
            self.Animate_Container.offset = ft.transform.Offset(0, -0.3)
            self.Animate_Container.update()