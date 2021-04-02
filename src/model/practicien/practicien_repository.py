from dataclasses import dataclass
from typing import List

from src.model.practicien.practicien import Practicien


@dataclass
class PracticienRepository:

    def find_practicien_by_id(self, practicien_id: int) -> Practicien:
        raise NotImplementedError

    def find_practiciens(self) -> List[Practicien]:
        raise NotImplementedError
