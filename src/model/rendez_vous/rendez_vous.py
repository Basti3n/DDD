from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practicien
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous_deja_annule_exception import RendezVousDejaAnnuleException
from src.model.rendez_vous.rendez_vous_deja_clos_exception import RendezVousDejaClosException
from src.model.rendez_vous.statut import Statut


@dataclass
class RendezVous:
    patient: Patient
    practicien: Practicien
    creneau: Creneau
    rendez_vous_id: int = 0
    statut: Statut = Statut.VALIDE

    def est_realisable(self, rendez_vous_list: List[RendezVous]) -> bool:
        if self.creneau.date_debut >= self.creneau.date_fin:
            return False
        for rdv in rendez_vous_list:
            if self.practicien.id == rdv.practicien.id and self.creneau.est_compris_dans(rdv.creneau) and rdv.statut != Statut.ANNULE:
                return False
        return True

    def modifier_statut(self, nouveau_statut: Statut) -> None:
        if self.statut == Statut.CLOS:
            raise RendezVousDejaClosException
        elif self.statut == Statut.ANNULE:
            raise RendezVousDejaAnnuleException
        self.statut = nouveau_statut
