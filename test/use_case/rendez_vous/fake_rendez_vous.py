from typing import Optional

from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practicien
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous
from src.model.rendez_vous.rendez_vous_repository import RendezVousRepository


class FakeRendezVous(RendezVousRepository):

    def __init__(self):
        self.rendez_vous = [RendezVous(Patient(1, "Alice"), Practicien(1, "Jean"), Creneau(10, 14)),
                            RendezVous(Patient(1, "Alice"), Practicien(1, "Jean"), Creneau(18, 20)),
                            RendezVous(Patient(1, "Alice"), Practicien(1, "Jean"), Creneau(21, 23))]

    def create_rendez_vous(self, patient: Patient, practicien: Practicien, creneau: Creneau) -> RendezVous:
        rdv = RendezVous(patient, practicien, creneau)
        self.rendez_vous.append(rdv)
        return rdv

    def find_rendez_vous_between_dates(self, date_start: int, date_end: int) -> Optional[RendezVous]:
        if date_start >= date_end:
            raise Exception
        for rdv in self.rendez_vous:
            if rdv.creneau.date_start <= date_start < rdv.creneau.date_end or rdv.creneau.date_start < date_end <= rdv.creneau.date_end:
                return rdv
        return None
