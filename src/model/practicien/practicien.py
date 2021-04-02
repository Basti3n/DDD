from __future__ import annotations
from dataclasses import dataclass

from typing import List


@dataclass
class Practicien:
    id: int
    nom: str

    def est_egal(self, practicien: Practicien):
        return self.id == practicien.id \
               and self.nom == practicien.nom

    def est_present_dans(self, practiciens: List[Practicien]) -> bool:
        for p in practiciens:
            if self.est_egal(p):
                return True
        return False
