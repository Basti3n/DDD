import unittest

from datetime import datetime
from src.model.patient.patient import Patient
from src.model.patient.patient_non_trouve_exception import PatientNonTrouveException
from src.model.practicien.practicien import Practicien
from src.model.practicien.practicien_non_trouve_exception import PracticienNonTrouveException
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous_non_valide_exception import RendezVousNonValideException
from src.model.rendez_vous.rendez_vous import RendezVous
from src.model.rendez_vous.statut import Statut
from src.use_case.rendez_vous.creer_rendez_vous import CreerRendezVous
from test.use_case.rendez_vous.fake_patients import FakePatients
from test.use_case.rendez_vous.fake_practiciens import FakePracticiens
from test.use_case.rendez_vous.fake_rendez_vous import FakeRendezVous


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        patient_repository = FakePatients()
        practicien_repository = FakePracticiens()
        rendez_vous_repository = FakeRendezVous()
        self.creer_rendez_vous = CreerRendezVous(patient_repository, practicien_repository, rendez_vous_repository)

    def test_creer_rendez_vous(self):
        date_start = datetime(2021, 4, 1, 6)
        date_end = datetime(2021, 4, 1, 7)
        output_rdv = self.creer_rendez_vous.execute(Patient(2, 'Bob'), Practicien(2, 'Baptiste'), Creneau(date_start, date_end))
        self.assertEqual(output_rdv.statut, Statut.VALIDE)

    def test_creer_rendez_vous_creneau_utilise(self):
        date_start = datetime(2021, 4, 1, 11)
        date_end = datetime(2021, 4, 1, 12)
        params_rdv = [Patient(2, 'Bob'), Practicien(1, 'Jean'), Creneau(date_start, date_end)]
        self.assertRaises(RendezVousNonValideException, self.creer_rendez_vous.execute, *params_rdv)

    def test_creer_rendez_meme_creneau_practicien_different(self):
        date_start = datetime(2021, 4, 1, 11)
        date_end = datetime(2021, 4, 1, 12)
        initial_rdv = RendezVous(Patient(3, 'Tom'), Practicien(3, 'Alex'), Creneau(date_start, date_end), rendez_vous_id=6)
        output_rdv = self.creer_rendez_vous.execute(Patient(3, 'Tom'), Practicien(3, 'Alex'), Creneau(date_start, date_end))
        self.assertEqual(output_rdv, initial_rdv)

    def test_creer_rendez_vous_creneau_annule(self):
        date_start = datetime(2021, 4, 3, 22)
        date_end = datetime(2021, 4, 3, 23)
        initial_rdv = RendezVous(Patient(3, 'Tom'), Practicien(1, 'Jean'), Creneau(date_start, date_end), rendez_vous_id=6)
        output_rdv = self.creer_rendez_vous.execute(Patient(3, 'Tom'), Practicien(1, 'Jean'), Creneau(date_start, date_end))
        self.assertEqual(output_rdv, initial_rdv)

    def test_creer_rendez_vous_practicien_non_trouve(self):
        date_start = datetime(2021, 4, 1, 6)
        date_end = datetime(2021, 4, 1, 7)
        params_rdv = [Patient(2, 'Bob'), Practicien(10, 'Albert'), Creneau(date_start, date_end)]
        self.assertRaises(PracticienNonTrouveException, self.creer_rendez_vous.execute, *params_rdv)

    def test_creer_rendez_vous_patient_non_trouve(self):
        date_start = datetime(2021, 4, 1, 6)
        date_end = datetime(2021, 4, 1, 7)
        params_rdv = [Patient(15, 'Gérard'), Practicien(2, 'Baptiste'), Creneau(date_start, date_end)]
        self.assertRaises(PatientNonTrouveException, self.creer_rendez_vous.execute, *params_rdv)
