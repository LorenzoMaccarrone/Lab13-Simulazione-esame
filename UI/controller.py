import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        self._listYear=self._model.getYear()
        self._listShape = self._model.getShape()
        for a in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(a))
        for b in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(b))
        self._view.update_page()

    def handle_graph(self, e):
        if self._view.ddyear.value is None and self._view.ddshape.value is None:
            self._view.create_alert("inserire dati")
            return
        if self._view.ddyear.value is None:
            self._view.create_alert("anno non inserito")
            return
        if self._view.ddshape.value is None:
            self._view.create_alert("shape non inserito")
            return
        #ricordati che i value dei dd ritornano sempre delle stringhe
        #quindi anche il valore dell'anno viene ritornato come una stringa!
        #non faccio controlli sulla conversione perchè non è una stringa
        #inserita dell'utente ma scelta da un dropdown di stringhe
        self._model.creaGrafo(int(self._view.ddyear.value), self._view.ddshape.value)
        self._view.txt_result.controls.append(
            ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getNumNodi()} nodi e {self._model.getNumArchi()} archi"))
        printPesi=self._model.pesiArchiAdiacenti()
        printPesi.sort(key=lambda x: x[0])
        for a in printPesi:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {a[0]}, somma pesi su archi= {a[1]}"))
        self._view.update_page()

    def handle_path(self, e):
        pass