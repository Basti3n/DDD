from src.model.patient.patient import Patient
from src.model.patient.patient_repository import PatientRepository
from src.model.practicien.practicien import Practicien
from src.model.practicien.practicien_repository import PracticienRepository
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous_repository import RendezVousRepository


class CreerRendezVous:

    def __init__(self, patient_repository: PatientRepository,
                 practicien_repository: PracticienRepository,
                 rendez_vous_repository: RendezVousRepository):
        self.patient_repository = patient_repository
        self.practicien_repository = practicien_repository
        self.rendez_vous_repository = rendez_vous_repository

    def execute(self, patient: Patient, practicien: Practicien, creneau: Creneau):
        # FETCH
        rendez_vous = self.rendez_vous_repository.find_rendez_vous()

        # Recherche RDV + RM
        if creneau.date_start >= creneau.date_end:
            raise Exception
        for rdv in rendez_vous:
            if rdv.practicien.id == practicien.id and (
                    rdv.creneau.date_start <= creneau.date_start < rdv.creneau.date_end or
                    rdv.creneau.date_start < creneau.date_end <= rdv.creneau.date_end):
                raise Exception
        # Retour
        return self.rendez_vous_repository.create_rendez_vous(patient, practicien, creneau)
