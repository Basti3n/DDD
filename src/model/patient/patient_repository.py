from dataclasses import dataclass
from typing import List

from src.model.patient.patient import Patient


@dataclass
class PatientRepository:

    def find_patient_by_id(self, patient_id: int) -> Patient:
        raise NotImplementedError

    def find_patients(self) -> List[Patient]:
        raise NotImplementedError
