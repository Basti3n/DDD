from dataclasses import dataclass

from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practicien
from src.model.rendez_vous.creneau import Creneau


@dataclass
class RendezVous:
    patient: Patient
    practicien: Practicien
    creneau: Creneau
