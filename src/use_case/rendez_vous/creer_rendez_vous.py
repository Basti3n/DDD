from src.model.patient.patient import Patient
from src.model.patient.patient_repository import PatientRepository
from src.model.practicien.practicien import Practicien
from src.model.practicien.practicien_repository import PracticienRepository
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous
from src.model.rendez_vous.rendez_vous_repository import RendezVousRepository


class CreerRendezVous:

    def __init__(self, patient_repository: PatientRepository,
                 practicien_repository: PracticienRepository,
                 rendez_vous_repository: RendezVousRepository):
        self.patient_repository = patient_repository
        self.practicien_repository = practicien_repository
        self.rendez_vous_repository = rendez_vous_repository

    def execute(self, patient: Patient, practicien: Practicien, creneau: Creneau):
        if len(self.rendez_vous_repository.find_rendez_vous_by_practicien_id_between_dates(practicien.id,
                                                                                           creneau.date_start,
                                                                                           creneau.date_end)) != 0:
            raise Exception
        return self.rendez_vous_repository.create_rendez_vous(patient, practicien, creneau)
