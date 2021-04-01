from datetime import datetime
from typing import List

from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practicien
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous
from src.model.rendez_vous.rendez_vous_repository import RendezVousRepository
from src.model.rendez_vous.statut import Statut


class FakeRendezVous(RendezVousRepository):

    def __init__(self):
        self.rendez_vous = [
            RendezVous(
                Patient(1, 'Alice'),
                Practicien(1, 'Jean'),
                Creneau(
                    datetime(2021, 4, 1, 10),
                    datetime(2021, 4, 1, 14)),
                rendez_vous_id=1),
            RendezVous(
                Patient(1, 'Alice'),
                Practicien(1, 'Jean'),
                Creneau(
                    datetime(2021, 4, 1, 18),
                    datetime(2021, 4, 1, 20)),
                rendez_vous_id=2),
            RendezVous(
                Patient(1, 'Alice'),
                Practicien(1, 'Jean'),
                Creneau(
                    datetime(2021, 4, 1, 21),
                    datetime(2021, 4, 1, 23)),
                rendez_vous_id=3),
            RendezVous(
                Patient(1, 'Alice'),
                Practicien(1, 'Jean'),
                Creneau(
                    datetime(2021, 4, 2, 21),
                    datetime(2021, 4, 2, 23)),
                rendez_vous_id=4,
                statut=Statut.CLOS),
            RendezVous(
                Patient(1, 'Alice'),
                Practicien(1, 'Jean'),
                Creneau(
                    datetime(2021, 4, 3, 21),
                    datetime(2021, 4, 3, 23)),
                rendez_vous_id=5,
                statut=Statut.ANNULE)]

    def create_rendez_vous(self, rendez_vous: RendezVous) -> RendezVous:
        rendez_vous.rendez_vous_id = len(self.rendez_vous) + 1
        self.rendez_vous.append(rendez_vous)
        return rendez_vous

    def find_rendez_vous(self) -> List[RendezVous]:
        return self.rendez_vous

    def update_rendez_vous(self, rendez_vous: RendezVous) -> RendezVous:
        self.rendez_vous[rendez_vous.rendez_vous_id - 1] = rendez_vous
        return rendez_vous
