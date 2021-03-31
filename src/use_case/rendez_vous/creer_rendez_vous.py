from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practitien
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous


class CreerRendezVous:

    def execute(self, patient: Patient, practitien: Practitien, creneau: Creneau):
        return RendezVous(patient, practitien, creneau)
