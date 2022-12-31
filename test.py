import flet as ft
from flet import icons, colors
import json


all_product = ft.Row(scroll=True)
s = []
with open('data.json') as json_file:
    data = json.load(json_file)
    s = data

# NOW PUSH TO NEW WIDGET
for x in s:
    all_product.controls.append(
        ft.Card(
            elevation=2,
            content=ft.Container(
                width=300,
                height=400,
                padding=10,
                bgcolor="white",
                content=ft.Column([
                    ft.Image(
                        src="/assets/images/" + x["image"],
                        width=250,
                        height=350,
                        border_radius=ft.border_radius.all(5),
                        fit="contain"
                    ),
                    ft.Text(x["name"],
                         size=18,
                         weight="bold")

                ], alignment="center")
            )
        )
    )

mysection1 = ft.Column([


    all_product,

])
