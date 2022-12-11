import flet as ft


class SwitchMode:
    """
    change mode
    """
    def __init__(self, page):
        self.page = page
        self.page.floating_action_button = ft.FloatingActionButton("+", icon="add", content=ft.Icon(ft.icons.DARK_MODE))
        self.page.floating_action_button.on_click = self.switch_mode

    def switch_mode(self, e):
        """
        toggle dark mode light
        """
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.page.floating_action_button.content = ft.Icon(ft.icons.LIGHT_MODE) \
        if self.page.theme_mode == "dark" == "dark" else ft.Icon(ft.icons.DARK_MODE)
        self.page.update()