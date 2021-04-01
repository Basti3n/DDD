import unittest

from datetime import datetime
from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practicien
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous
from src.use_case.rendez_vous.creer_rendez_vous import CreerRendezVous
from test.use_case.rendez_vous.fake_patients import FakePatients
from test.use_case.rendez_vous.fake_practiciens import FakePracticiens
from test.use_case.rendez_vous.fake_rendez_vous import FakeRendezVous


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        patient_repository = FakePatients()
        practicien_repository = FakePracticiens()
        rendez_vous_repository = FakeRendezVous()
        self.rdv = CreerRendezVous(patient_repository, practicien_repository, rendez_vous_repository)

    # TODO DATETIME
    def test_creer_rendez_vous(self):
        date_start = datetime(2021, 4, 1, 6)
        date_end = datetime(2021, 4, 1, 7)
        initial_rdv = RendezVous(Patient(2, 'Bob'), Practicien(2, 'Baptiste'), Creneau(date_start, date_end))
        output_rdv = self.rdv.execute(Patient(2, 'Bob'), Practicien(2, 'Baptiste'), Creneau(date_start, date_end))
        self.assertEqual(output_rdv, initial_rdv)

    def test_creer_rendez_vous_creneau_utilise(self):
        date_start = datetime(2021, 4, 1, 11)
        date_end = datetime(2021, 4, 1, 12)
        params_rdv = Patient(2, 'Bob'), Practicien(1, 'Jean'), Creneau(date_start, date_end)
        self.assertRaises(Exception, self.rdv.execute, params_rdv)

    def test_creer_rendez_meme_creneau_practicien_different(self):
        date_start = datetime(2021, 4, 1, 11)
        date_end = datetime(2021, 4, 1, 12)
        initial_rdv = RendezVous(Patient(3, 'Tom'), Practicien(3, 'Alex'), Creneau(date_start, date_end))
        output_rdv = self.rdv.execute(Patient(3, 'Tom'), Practicien(3, 'Alex'), Creneau(date_start, date_end))
        self.assertEqual(output_rdv, initial_rdv)
