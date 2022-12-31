import flet as ft

import test
import test2
from app_main import AppMain
from switch_mode import SwitchMode
from product_card import ProductCard
from product_section import ProductSection
def main(page: ft.Page):
    page.title = 'COFFEE BAR'
    # page.theme = ft.theme.Theme(color_scheme_seed="indigo")
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_width = 414
    page.window_height = 736
    page.window_top = 0
    # page.window_max_height = 1200
    # page.window_max_width = 560
    # page.bgcolor = "#CDD6D8"
    page.padding = 10
    # ProductCard(page)
    AppMain(page)
    # SwitchMode(page)
    # ProductSection(page)
    # page.add(test2.all_product)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
    # ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
