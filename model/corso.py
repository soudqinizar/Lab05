from dataclasses import dataclass

from model import studente


@dataclass
class Corso:
    codIns : str
    crediti : int
    nome : str
    pd : int


    def __hash__(self):
        return hash(self.codIns)

    def __eq__(self, other: "Corso"):
        return self.codIns == other.codIns

    def __str__(self):
        return f"{self.nome} ({self.codIns})"






