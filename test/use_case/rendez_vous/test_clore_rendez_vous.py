import unittest

from src.model.rendez_vous.rendez_vous_deja_annule_exception import RendezVousDejaAnnuleException
from src.model.rendez_vous.rendez_vous_deja_clos_exception import RendezVousDejaClosException
from src.model.rendez_vous.rendez_vous_non_trouve_exception import RendezVousNonTrouveException
from src.model.rendez_vous.statut import Statut
from src.use_case.rendez_vous.clore_rendez_vous import CloreRendezVous
from test.use_case.rendez_vous.fake_rendez_vous import FakeRendezVous


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        rendez_vous_repository = FakeRendezVous()
        self.clore_rendez_vous = CloreRendezVous(rendez_vous_repository)

    def test_clore_rendez_vous(self) -> None:
        rdv_id = 1
        output_rdv = self.clore_rendez_vous.execute(rdv_id)
        self.assertEqual(output_rdv.statut, Statut.CLOS)

    def test_clore_rendez_vous_deja_clos(self) -> None:
        rdv_id = 4
        self.assertRaises(RendezVousDejaClosException, self.clore_rendez_vous.execute, rdv_id)

    def test_clore_rendez_vous_deja_annule(self) -> None:
        rdv_id = 5
        self.assertRaises(RendezVousDejaAnnuleException, self.clore_rendez_vous.execute, rdv_id)

    def test_clore_rendez_vous_non_trouve(self) -> None:
        rdv_id = 6
        self.assertRaises(RendezVousNonTrouveException, self.clore_rendez_vous.execute, rdv_id)
