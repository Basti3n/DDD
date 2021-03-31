import unittest
from unittest.mock import Mock, MagicMock

from src.model.patient.patient import Patient
from src.model.practicien.practicien import Practitien
from src.model.rendez_vous.creneau import Creneau
from src.model.rendez_vous.rendez_vous import RendezVous
from src.use_case.rendez_vous.creer_rendez_vous import CreerRendezVous


class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.rdv = CreerRendezVous()

    def test_creer_rendez_vous(self):
        test_rdv = RendezVous(Patient('Pierre'), Practitien('ROUZADOFRE'), Creneau('19h', '21h'))
        self.assertEqual(self.rdv.execute(Patient('Pierre'),
                                          Practitien('ROUZADOFRE'),
                                          Creneau('19h', '21h')), test_rdv)
