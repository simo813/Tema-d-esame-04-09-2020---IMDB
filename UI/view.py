import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.btnIncrementalPath = None
        self._btnFilmHighGrade = None
        self.btnMyPlaylist = None
        self.txtInMax = None
        self._btnCreateGraph = None
        self.txtInRank = None
        self.txtInDTot = None
        self.ddFilm = None
        self.ddFilmValue = None
        self._page = page
        self._page.title = "TdP - Esame	del	04/09/2020 IMDB"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP - Esame	del	04/09/2020 IMDB", color="red", size=24)
        self._page.controls.append(self._title)

        #ROW1
        self.txtInRank = ft.TextField(label="Insert rank")
        self._btnCreateGraph = ft.ElevatedButton(text="Crea Grafo",
                                                 on_click=self._controller.handleCreateGraph)
        row1 = ft.Row([
            ft.Container(self.txtInRank, width=300),
            ft.Container(self._btnCreateGraph, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW2
        self._btnFilmHighGrade = ft.ElevatedButton(text="Highest grade Film",
                                                   on_click=self._controller.handleHighFilmGrade)
        row2 = ft.Row([
            ft.Container(self._btnFilmHighGrade, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #ROW3
        self.ddFilm = ft.Dropdown(label="Film", on_change=self.on_ddFilm_change)
        self.btnIncrementalPath = ft.ElevatedButton(text="Incremental path",
                                               on_click=self._controller.handleIncrementalPath)

        row3 = ft.Row([
            ft.Container(self.ddFilm, width=300),
            ft.Container(self.btnIncrementalPath, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._controller.fillDD()
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def on_ddFilm_change(self, e):
        self.ddFilmValue = self.ddFilm.value
        self.update_page()


    def update_page(self):
        self._page.update()
