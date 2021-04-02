from src.model.patient.patient import Patient
from src.model.patient.patient_non_trouve_exception import PatientNonTrouveException
from src.model.patient.patient_repository import PatientRepository
from src.model.practicien.practicien import Practicien
from src.model.practicien.practicien_non_trouve_exception import PracticienNonTrouveException
from src.model.practicien.practicien_repository import PracticienRepository
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous
from src.model.rendez_vous.rendez_vous_non_valide_exception import RendezVousNonValideException
from src.model.rendez_vous.rendez_vous_repository import RendezVousRepository


class CreerRendezVous:

    def __init__(self, patient_repository: PatientRepository,
                 practicien_repository: PracticienRepository,
                 rendez_vous_repository: RendezVousRepository):
        self.patient_repository = patient_repository
        self.practicien_repository = practicien_repository
        self.rendez_vous_repository = rendez_vous_repository

    def execute(self, patient: Patient, practicien: Practicien, creneau: Creneau):
        rendez_vous_list = self.rendez_vous_repository.find_rendez_vous()
        practicien_lists = self.practicien_repository.find_practiciens()
        patients_lists = self.patient_repository.find_patients()
        rendez_vous = RendezVous(patient, practicien, creneau)
        if not rendez_vous.est_realisable(rendez_vous_list):
            raise RendezVousNonValideException
        if not practicien.est_present_dans(practicien_lists):
            raise PracticienNonTrouveException
        if not patient.est_present_dans(patients_lists):
            raise PatientNonTrouveException
        return self.rendez_vous_repository.create_rendez_vous(rendez_vous)
