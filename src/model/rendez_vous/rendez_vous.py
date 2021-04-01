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

    def est_realisable(self, rendez_vous_list: List[RendezVous]) -> bool:
        if self.creneau.date_debut >= self.creneau.date_fin:
            return False
        for rdv in rendez_vous_list:
            if self.practicien.id == rdv.practicien.id and self.creneau.est_compris_dans(rdv.creneau):
                return False
        return True
