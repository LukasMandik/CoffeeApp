import flet as ft
from app_main import AppMain
from switch_mode import SwitchMode


def main(page: ft.Page):
    page.title = 'COFFEE BAR'
    page.theme = ft.theme.Theme(color_scheme_seed="indigo")
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = 'center'
    page.window_height = 800
    page.window_width = 480
    page.window_top = 0
    page.window_max_height = 1200
    # page.window_max_width = 560
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.bgcolor = "#CDD6D8"
    page.padding = 10

    AppMain(page)
    SwitchMode(page)
    page.update()


# ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main, assets_dir="assets")