from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Creneau:
    date_debut: datetime
    date_fin: datetime

    def est_compris_dans(self, creneau_existant: Creneau) -> bool:
        return creneau_existant.date_debut <= self.date_debut < creneau_existant.date_fin or \
               creneau_existant.date_debut < self.date_fin <= creneau_existant.date_fin
