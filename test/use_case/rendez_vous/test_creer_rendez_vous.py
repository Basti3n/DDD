import unittest

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
        initial_rdv = RendezVous(Patient(2, 'Bob'), Practicien(2, 'Baptiste'), Creneau(date_start=6, date_end=7))
        output_rdv = self.rdv.execute(Patient(2, 'Bob'), Practicien(2, 'Baptiste'), Creneau(date_start=6, date_end=7))
        self.assertEqual(output_rdv, initial_rdv)

    def test_creer_rendez_vous_creneau_utilise(self):
        params_rdv = Patient(2, 'Bob'), Practicien(1, "Jean"), Creneau(date_start=11, date_end=12)
        self.assertRaises(Exception, self.rdv.execute, params_rdv)

    def test_creer_rendez_meme_creneau_practicien_different(self):
        initial_rdv = RendezVous(Patient(3, 'Tom'), Practicien(3, "Alex"), Creneau(date_start=11, date_end=12))
        output_rdv = self.rdv.execute(Patient(3, 'Tom'), Practicien(3, "Alex"), Creneau(date_start=11, date_end=12))
        self.assertEqual(output_rdv, initial_rdv)
