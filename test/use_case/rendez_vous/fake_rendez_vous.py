from typing import Optional, List

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

    def find_rendez_vous_by_practicien_id_between_dates(self, practicien_id: int, date_start: int, date_end: int) -> \
            List[RendezVous]:
        if date_start >= date_end:
            raise Exception
        results: List[RendezVous] = []
        for rdv in self.rendez_vous:
            if rdv.practicien.id == practicien_id and (
                    rdv.creneau.date_start <= date_start < rdv.creneau.date_end or rdv.creneau.date_start < date_end <= rdv.creneau.date_end):
                results.append(rdv)
        return results
