import flet as ft


class AppMain:

    def __init__(self, page):
        self.page = page
        self.page.horizontal_alignment = 'center'
        self.page.vertical_alignment = 'center'

        self.TextHeaderWelcome = ft.Text('Welcome', style="headlineLarge", text_align='center')
        self.Container1 = ft.Container(
            content=self.TextHeaderWelcome,
            margin=5,
            padding=ft.padding.all(100)
        )

        self.PhotoRow = ft.Row(expand=1, wrap=False, scroll=ft.ScrollMode.ADAPTIVE,run_spacing=300, spacing=10)
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

        self.Container4 = ft.Container(self.PhotoRow)
        self.c = ft.Container(
            self.Container4,
            width=320,
            height=420,
            # bgcolor="black",
            padding=10,
            border_radius=10,
            offset=ft.transform.Offset(0, 3),
            animate_offset=ft.animation.Animation(700),

        )

        def animate(e):
            self.c.offset = ft.transform.Offset(0, -0.3)
            self.c.update()



        self.Btn1 = ft.TextButton(
            "Coffee",
            icon=ft.icons.COFFEE,
            # icon_color=ft.colors.BLACK87,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
        )
        self.Btn2 = ft.TextButton("Drink", icon=ft.icons.LOCAL_DRINK,
                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
                                  )
        self.Btn3 = ft.TextButton("Cake", icon=ft.icons.CAKE,
                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
        self.Btn1.on_click = self.next_page
        self.Btn2.on_click = animate
        # self.Container2 = ft.Container(content=self.Btn1, margin=10,
        #             padding=10,
        #             alignment=ft.alignment.bottom_center,
        #             bgcolor=ft.colors.CYAN_200,
        #             width=150,
        #             height=150,
        #             border_radius=10,
        #                                border=ft.border.all(3, ft.colors.BLACK26)
        #
        #             )



        self.r = ft.Row([
            ft.Container(expand=True,content=self.Btn1),
            ft.Container(expand=True,content=self.Btn2),
            ft.Container(expand=True, content=self.Btn3) #border_radius=2, border=ft.border.all(0.2, ft.colors.BLACK26))
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, aspect_ratio=10)
        self.Container3 = ft.Container(self.r)
        self.WidgetList =[self.Container1, self.c, self.Container3]
        for i in self.WidgetList:
            self.page.add(i)
        self.page.update()

    def next_page(self, event):
        """
        go to registration page
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
                    border_radius=ft.border_radius.all(10),))

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