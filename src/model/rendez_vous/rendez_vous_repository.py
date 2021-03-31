from dataclasses import dataclass
from typing import Optional

from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practicien
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous


@dataclass
class RendezVousRepository:

    def create_rendez_vous(self, patient: Patient, practicien: Practicien, creneau: Creneau) -> RendezVous:
        raise NotImplementedError

    def find_rendez_vous_between_dates(self, date_start: int, date_end : int) -> Optional[RendezVous]:
        raise NotImplementedError
