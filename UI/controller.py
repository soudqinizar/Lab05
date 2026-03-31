import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()
        self._ddCodinsValue = None


    def cercaIscritti(self, e):
        self._ddCodinsValue = self._view.ddCodins.value
        self._view.lvTxtOut.controls.clear()

        if self._ddCodinsValue is None:
            self._view.create_alert("Selezionare un corso di interesse.")
            return
        studenti = self._model.getStudentiCorso(self._ddCodinsValue)

        if len(studenti) == 0:
            self._view.lvTxtOut.controls.append(
                self._view.create_alert("Nessuno studente iscritto risulta essere iscritto a questo corso."))
            self._view.update_page()
            return

        self._view.lvTxtOut.controls.append(
            ft.Text(f"Studenti iscritti al corso {self._ddCodinsValue}:"))

        for s in studenti:
            self._view.lvTxtOut.controls.append(ft.Text(s))
        self._view.update_page()


    def cercaStudente(self,e):
        matricola = self._view.txtMatricola.value

        if matricola is None:
            self._view.create_alert("Inserisci una matricola")
            return

        studente = self._model.getStudentiDataMatricola(matricola)
        if studente is None:
            self._view.lvTxtOut.controls.append(
                self._view.create_alert("Non esiste uno studente con tale matricola"))
            return

        self._view.txtNome.value = studente.nome
        self._view.txtCognome.value = studente.cognome
        self._view.update_page()






    def cercaCorsi(self,e):
        pass

    def Iscrivi(self,e):
        pass

    def refil_corso(self):

        for c in self._model.getAllCorsi():
            self._view.ddCodins.options.append(ft.dropdown.Option(
                key=c.codIns,
                text=c
            ))
            pass


