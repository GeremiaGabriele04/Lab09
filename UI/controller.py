import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_Analisi(self, e):
        self._view.txt_result.clean()
        distanza = self._view.txt_name.value
        if distanza is None or distanza == "":
            self._view.create_alert("Inserire una distanza valida")
            return

        try:
            dist = int(distanza)
        except ValueError:
            self._view.create_alert("Inserire una distanza valida")
            return

        self._model.buildGraph(dist)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.get_numnodi()} nodi e {self._model.get_numarchi()} archi."))
        for u,v,peso in self._model._graph.edges(data=True):
            self._view.txt_result.controls.append(ft.Text(f"{u} -> {v} : {peso['weight']}"))
        self._view.update_page()
