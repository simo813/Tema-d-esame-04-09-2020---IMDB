import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.btnMyPlaylist = None
        self.txtInMax = None
        self._btnCreaGrafo = None
        self.txtInMin = None
        self.txtInDTot = None
        self.ddGenre = None
        self.ddGenreValue = None
        self._page = page
        self._page.title = "TdP - Esame	del	02/11/2022	–	appello	riservato	"
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
        self._title = ft.Text("TdP - Esame	del	02/11/2022	–	appello	riservato	", color="red", size=24)
        self._page.controls.append(self._title)

        #ROW1
        self.ddGenre = ft.Dropdown(label="Genre", on_change=self.on_ddGenre_change)
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([
            ft.Container(self.ddGenre , width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW2
        self.txtInMin = ft.TextField(label="minimum")


        row2 = ft.Row([
            ft.Container(self.txtInMin, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #ROW3
        self.txtInMax = ft.TextField(label="maximum")

        row3 = ft.Row([
            ft.Container(self.txtInMax, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        
        #ROW4
        self.txtInDTot = ft.TextField(label="dTot")
        self.btnMyPlaylist = ft.ElevatedButton(text="My playlist",
                                               on_click=self._controller.handleMyPlaylist)
        row4 = ft.Row([
            ft.Container(self.txtInDTot, width=300),
            ft.Container(self.btnMyPlaylist, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)
        

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

    def on_ddGenre_change(self, e):
        self.ddGenreValue = self.ddGenre.value
        self.update_page()


    def update_page(self):
        self._page.update()
