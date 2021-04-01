from dataclasses import dataclass
from typing import List

from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practicien
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous


@dataclass
class RendezVousRepository:

    def create_rendez_vous(self, rendez_vous: RendezVous) -> RendezVous:
        raise NotImplementedError

    def find_rendez_vous(self) -> List[RendezVous]:
        raise NotImplementedError
