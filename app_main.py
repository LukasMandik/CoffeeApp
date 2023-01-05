import flet as ft
import json

from product_section import ProductSection

class AppMain:

    def __init__(self, page):
        self.page = page
        self.page.horizontal_alignment = 'center'
        self.page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN

        #top menu

        self.up_main_menu = ft.AppBar(
            bgcolor=ft.colors.BLACK12,
            center_title=True,
            toolbar_height=80,
            leading=ft.IconButton(
                icon=ft.icons.MENU,
                icon_color="white",
                icon_size=40,

            ),
            title=ft.Text(
                "COFFEEBAR",
                size=40,
                color="white",
                weight='w100',
                font_family="Futura",
            ),
            actions=[
                ft.IconButton(
                    icon=ft.icons.SHOPPING_BAG,
                    icon_color="white",
                    icon_size=40,
                ),
            ]
    )

        self.up_menu_container = ft.Container(

            content=self.up_main_menu,
            height=100,
            # bgcolor=ft.colors.BLACK12
        )



        #top text

        self.TextHeaderWelcome = ft.Text(
            'WELCOME,\nToday is great day for coffee',
            style=ft.TextThemeStyle.HEADLINE_LARGE,
            text_align=ft.TextAlign.LEFT,
            weight=ft.FontWeight.W_100,
            font_family="Futura",
            size=20,

        )
        self.TextContainer = ft.Container(
            self.TextHeaderWelcome,
            # margin=5,
            # padding=ft.padding.all(10),
            height=80,
            width=414,
            # bgcolor=ft.colors.BLACK12,
            padding=10
        )

        # Grid product



        self.all_product = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=190,
            child_aspect_ratio=1.0,
            spacing=10,
            run_spacing=10,
            horizontal=True




        )
        self.grid_container = ft.Container(
            self.all_product,
            # width=600,
            height=180,
            # bgcolor=ft.colors.BLACK12,
            padding=10
        )
        self.s = []
        with open('data.json') as json_file:
            self.data = json.load(json_file)
            self.s = self.data



        for x in self.s:
            self.all_product.controls.append(
                ft.Stack(controls=[
                    ft.Image(
                        width=200,
                        height=200,
                        src="/assets/images/" + x["image"],
                        fit=ft.ImageFit.COVER,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                        border_radius=ft.border_radius.all(10),

                    ),
                    ft.FloatingActionButton(
                        mini=True,
                        icon="add",
                        content=ft.Text(
                            value=x["price"],
                            size=10,
                            weight=ft.FontWeight.W_100,
                            font_family="Futura",
                            color=ft.colors.WHITE,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        right=5,
                        bottom=5,
                        bgcolor=ft.colors.BLACK26

                    ),

                    ft.Text(
                        value=x["name"],
                        size=18,
                        weight=ft.FontWeight.W_100,
                        font_family="Futura",
                        color=ft.colors.WHITE,
                        # text_align=ft.TextAlign.CENTER,
                        left=5,
                        top=3,
                        style=ft.TextThemeStyle.HEADLINE_LARGE,

                        # tooltip="najlepsia kava v meste"


                    ),
                    # ft.Text(
                    #     value=x["price"],
                    #     size=18,
                    #     weight=ft.FontWeight.W_100,
                    #     font_family="Futura",
                    #     color=ft.colors.WHITE,
                    #     text_align=ft.TextAlign.CENTER,
                    #     right=12,
                    #     bottom=12,
                    #     style=ft.TextThemeStyle.HEADLINE_LARGE,
                    #     bgcolor=ft.colors.BLACK54,
                    # )
            ]
                )
            )

        # down grid

        self.down_grid_container = ft.Container(
            height=250,
            # bgcolor=ft.colors.BLACK12
        )


        # animacia fotiek zo spodu

        self.PhotoRow = ft.Row(expand=1, wrap=False, scroll=ft.ScrollMode.ADAPTIVE,run_spacing=10, spacing=10)
        self.photo_img = ["/assets/images/_DSC5424.jpg",
                          "/assets/images/_DSC5444.jpg",
                          "/assets/images/_DSC5569.jpg",
                          "/assets/images/_DSC5409.jpg",
                          "/assets/images/_DSC5546.jpg"]
        for x in self.photo_img:
            self.PhotoRow.controls.append(
                ft.Image(
                    src=x,
                    width=300,
                    height=400,
                    fit=ft.ImageFit.COVER,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),


                )


            )

        self.photo_row_container = ft.Container(self.PhotoRow,bgcolor=ft.colors.BLACK26,)

        self.animate_container = ft.Container(
            self.photo_row_container,
            width=320,
            height=420,
            bgcolor=ft.colors.BLACK26,
            padding=10,
            border_radius=10,
            offset=ft.transform.Offset(0, 3),
            animate_offset=ft.animation.Animation(700),
        )

        def animate(e):
            self.animate_container.offset = ft.transform.Offset(0, -0.3)
            self.animate_container.update()


        #down product menu

        self.Btn1 = ft.TextButton(
            "Coffee",
            icon=ft.icons.COFFEE,

            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color=ft.colors.BLACK54,
                overlay_color=ft.colors.BLACK12
            )
        )
        self.Btn1.on_click = self.next_page


        self.Btn2 = ft.TextButton(
            "Drink",
            icon=ft.icons.LOCAL_DRINK,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color=ft.colors.BLACK54,
                overlay_color=ft.colors.BLACK12

            )
        )
        self.Btn2.on_click = animate

        self.Btn3 = ft.TextButton(
            "Cake",
            icon=ft.icons.CAKE,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                color=ft.colors.BLACK54,
                overlay_color=ft.colors.BLACK12,
            )
        )

        # self.Btn3.on_click =

        self.row_down_menu = ft.Row([
            ft.Container(expand=True,content=self.Btn1),
            ft.Container(expand=True,content=self.Btn2),
            ft.Container(expand=True, content=self.Btn3) #border_radius=2, border=ft.border.all(0.2, ft.colors.BLACK26))
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, aspect_ratio=10)
        self.down_menu_container = ft.Container(
            self.row_down_menu,
            # height=80,


            # bgcolor=ft.colors.BLACK26,
            # border_radius=10
        )
        self.WidgetList = [
            self.up_main_menu,
            # self.up_menu_container,
            self.TextContainer,
            self.grid_container,
            self.down_grid_container,
            self.down_menu_container,

        ]
        for i in self.WidgetList:
            self.page.add(i)
        self.page.update()

    def next_page(self, event):
        """
        go to next page
        """
        for i in self.WidgetList:
            self.page.controls.pop()
        NextPage(self.page)
        self.page.update()


class NextPage:
    def __init__(self, page):
        self.page = page
        self.page.horizontal_alignment = 'center'
        self.page.vertical_alignment = 'center'

        self.TextHeaderWelcome = ft.Text('This is next page', style="headlineLarge", text_align='center')
        self.Container1 = ft.Container(content=self.TextHeaderWelcome, margin=5,
                                       padding=ft.padding.only(left=30, right=30))

        self.Btn1 = ft.ElevatedButton("Go to main page", height=50,icon=ft.icons.ARROW_BACK)
        self.Btn1.on_click = self.back_main_page
        self.Container2 = ft.Container(content=self.Btn1, margin=5, padding=ft.padding.only(left=30, right=30))

        self.PhotoRow = ft.Row(expand=1, wrap=False, scroll="always")
        self.photo_img = ["/assets/images/_DSC5424.jpg",
                     "/assets/images/_DSC5444.jpg",
                     "/assets/images/_DSC5569.jpg",
                     "/assets/images/_DSC5409.jpg",
                     "/assets/images/_DSC5546.jpg"]
        for x in self.photo_img:
            self.PhotoRow.controls.append(
                ft.Image(
                    src=x,
                    width=200,
                    height=300,
                    fit=ft.ImageFit.COVER,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                    gapless_playback=True

                )
            )

        self.Container3 = ft.Container(self.PhotoRow, margin=5, padding=ft.padding.only(left=30, right=30))

        # self.Photo = ft.Image(src=f"/assets/images/_DSC5424.jpg", width=300, height=300, fit=ft.ImageFit.CONTAIN)
        # self.Container3 = ft.Container(self.Photo, margin=5, padding=ft.padding.only(left=30, right=30))

        self.WidgetList = [self.Container1, self.Container2, self.Container3]
        for i in self.WidgetList:
            self.page.add(i)
        self.page.update()

    def back_main_page(self, event):
        """
        go to main page
        """
        for i in self.WidgetList:
            self.page.controls.pop()
        AppMain(self.page)
        self.page.update()