from src.model.rendez_vous.rendez_vous import RendezVous
from src.model.rendez_vous.rendez_vous_non_trouve_exception import RendezVousNonTrouveException
from src.model.rendez_vous.rendez_vous_repository import RendezVousRepository
from src.model.rendez_vous.statut import Statut


class CloreRendezVous:
    def __init__(self, rendez_vous_repository: RendezVousRepository):
        self.rendez_vous_repository = rendez_vous_repository

    def execute(self, rdv_id: int) -> RendezVous:
        rendez_vous_list = self.rendez_vous_repository.find_rendez_vous()
        try:
            rdv = next(rdv for rdv in rendez_vous_list if rdv.rendez_vous_id == rdv_id)
        except StopIteration:
            raise RendezVousNonTrouveException
        rdv.modifier_statut(Statut.CLOS)
        return self.rendez_vous_repository.update_rendez_vous(rdv)
