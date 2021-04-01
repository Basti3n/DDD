from src.model.practicien.practicien import Practicien
from src.model.practicien.practicien_repository import PracticienRepository


class FakePracticiens(PracticienRepository):

    def __init__(self):
        self.practiciens = [Practicien(1, "Jean"), Practicien(2, "Baptiste"), Practicien(3, "Alex")]

    def find_practicien_by_id(self, practicien_id: int) -> Practicien:
        for practicien in self.practiciens:
            if practicien.id == practicien_id:
                return practicien
        raise Exception
