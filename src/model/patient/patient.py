from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Patient:
    id: int
    nom: str

    def est_egal(self, patient: Patient):
        return self.id == patient.id \
               and self.nom == patient.nom

    def est_present_dans(self, patients: List[Patient]) -> bool:
        for p in patients:
            if self.est_egal(p):
                return True
        return False
