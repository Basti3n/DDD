from dataclasses import dataclass
from typing import Optional, List

from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practicien
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous


@dataclass
class RendezVousRepository:

    def create_rendez_vous(self, patient: Patient, practicien: Practicien, creneau: Creneau) -> RendezVous:
        raise NotImplementedError

    def find_rendez_vous_by_practicien_id_between_dates(self, practicien_id: int, date_start: int, date_end: int) -> \
            List[RendezVous]:
        raise NotImplementedError
