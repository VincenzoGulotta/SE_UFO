import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def populate_dd_year(self):
        """ Metodo per popolare i dropdown """
        self._model.get_anni_forme()
        dict_anni_forme = self._model.dict_anni_forme
        for year in dict_anni_forme:
            self._view.dd_year.options.append(ft.DropdownOption(key = year, text = year))
        self._view.update()

    def populate_dd_shape(self, e):
        self._view.dd_shape.disabled = False
        year = int(self._view.dd_year.value)
        list_shape = self._model.dict_anni_forme[year]
        self._view.dd_shape.options.clear()
        for shape in list_shape:
            self._view.dd_shape.options.append(ft.DropdownOption(key= shape, text=shape))
        self._view.update()

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        year = self._view.dd_year.value
        shape = self._view.dd_shape.value
        nodi, archi = self._model.crea_grafo(year, shape)
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Numero di vertici: {nodi} Numero di archi: {archi}"))

        lista_chiavi = sorted(self._model.pesi_totali.keys())
        for state in lista_chiavi:
            weight = self._model.pesi_totali[state]
            self._view.lista_visualizzazione_1.controls.append(
                ft.Text(f"Nodo {state}, somma di pesi su archi = {weight}"))

        self._view.update()


    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO
