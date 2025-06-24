import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model


    def fillDD(self):
       pass

    def handleCreateGraph(self, e):
        if self.view.txtInRank is not None:
            try:
                self.view.txt_result.clean()
                rank = float(self.view.txtInRank.value)
                self.model.createGraph(rank)
                graph = self.model.graph
                for node in graph.nodes():
                    self.view.ddFilm.options.append(ft.dropdown.Option(key=node.id, text=node.name))
                self.view.txt_result.controls.append(ft.Text(
                    f"Grafo creato!\n"
                    f"# Vertici: {graph.number_of_nodes()}\n"
                    f"# Archi: {graph.number_of_edges()}\n"))

            except ValueError:
                self.view.txt_result.clean()
                self.view.txt_result.controls.append(ft.Text(
                    f"Inserisci un valore numerico di rank"))
        else:
            self.view.txt_result.clean()
            self.view.txt_result.controls.append(ft.Text(
                f"Inserisci un valore di rank per continuare"))
        self.view.update_page()

    def handleHighFilmGrade(self, e):
        HighFilmGradeNode, HighFilmGradeSumWeight = self.model.getHighFilmGrade()
        self.view.txt_result.clean()
        self.view.txt_result.controls.append(ft.Text(
            f"FILM GRADO MASSIMO:\n"
            f"{HighFilmGradeNode.__str__()}({HighFilmGradeSumWeight})"))
        self.view.update_page()


    def handleIncrementalPath(self, e):
        self.view.txt_result.clean()
        sourceid = int(self.view.ddFilmValue)
        source = self.model.idMapFilm[sourceid]
        incrementalPath = self.model.getIncrementalPath(source)
        self.view.txt_result.controls.append(ft.Text(
            f"Il cammino incrementale è il seguente"))
        for node in incrementalPath:
            self.view.txt_result.controls.append(ft.Text(
                f"{node.__str__()}"))
        self.view.update_page()





