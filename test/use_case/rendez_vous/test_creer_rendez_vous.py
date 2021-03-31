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

    @classmethod
    def setUpClass(cls) -> None:
        patient_repository = FakePatients()
        practicien_repository = FakePracticiens()
        rendez_vous_repository = FakeRendezVous()
        cls.rdv = CreerRendezVous(patient_repository, practicien_repository, rendez_vous_repository)

    def test_creer_rendez_vous(self):
        test_rdv = RendezVous(Patient(2, 'Bob'), Practicien(2, 'Baptiste'), Creneau(6, 7))
        self.assertEqual(self.rdv.execute(Patient(2, 'Bob'),
                                          Practicien(2, 'Baptiste'),
                                          Creneau(6, 7)), test_rdv)

    def test_creer_rendez_vous_creneau_utilise(self):
        self.assertRaises(Exception, self.rdv.execute, Patient(2, 'Bob'), Practicien(2, 'Baptiste'), Creneau(11, 12))
