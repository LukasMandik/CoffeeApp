import flet as ft
import json


def main(page: ft.Page):
    page.title = "GridView Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 660
    page.window_width = 380
    page.padding = 15
    page.update()

    all_product = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=200,
        child_aspect_ratio=1.0,
        spacing=15,
        run_spacing=15,
    )
    s = []
    with open('data.json') as json_file:
        data = json.load(json_file)
        s = data




    page.add(all_product)

    for x in s:
        all_product.controls.append(
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
    page.update()


# ft.app(target=main, assets_dir="assets")