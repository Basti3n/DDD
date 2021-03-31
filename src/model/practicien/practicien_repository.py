from dataclasses import dataclass

from src.model.practicien.practicien import Practicien


@dataclass
class PracticienRepository:

    def find_practicien_by_id(self, practicien_id: int) -> Practicien:
        raise NotImplementedError
