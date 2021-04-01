from __future__ import annotations
from dataclasses import dataclass
from typing import List

from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practicien
from src.model.rendez_vous.creneau import Creneau


@dataclass
class RendezVous:
    patient: Patient
    practicien: Practicien
    creneau: Creneau

    def est_valide(self, rendez_vous_list: List[RendezVous]) -> bool:
        if self.creneau.date_start >= self.creneau.date_end:
            return False
        for rdv in rendez_vous_list:
            if rdv.practicien.id == self.practicien.id and (
                    rdv.creneau.date_start <= self.creneau.date_start < rdv.creneau.date_end or
                    rdv.creneau.date_start < self.creneau.date_end <= rdv.creneau.date_end):
                return False
        return True
