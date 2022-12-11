import flet as ft


class AppMain:

    def __init__(self, page):
        self.page = page
        self.page.horizontal_alignment = 'center'
        self.page.vertical_alignment = 'center'

        self.TextHeaderWelcome = ft.Text('Welcome', style="headlineLarge", text_align='center')
        self.Container1 = ft.Container(content=self.TextHeaderWelcome, margin=5,
                                       padding=ft.padding.only(left=30, right=30))

        self.Btn1 = ft.FilledButton("Go to next page", height=50, width=200)
        self.Btn1.on_click = self.next_page
        self.Container2 = ft.Container(self.Btn1, margin=5, padding=ft.padding.only(left=30, right=30))

        self.WidgetList =[self.Container1, self.Container2]
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

        self.Btn1 = ft.FilledButton("Go to main page", height=50, width=200)
        self.Btn1.on_click = self.back_main_page
        self.Container2 = ft.Container(self.Btn1, margin=5, padding=ft.padding.only(left=30, right=30))

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
        go to registration page
        """
        for i in self.WidgetList:
            self.page.controls.pop()
        AppMain(self.page)
        self.page.update()