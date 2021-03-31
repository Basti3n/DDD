from dataclasses import dataclass

from src.model.patient.patient import Patient


@dataclass
class PatientRepository:

    def find_patient_by_id(self, patient_id: int) -> Patient:
        raise NotImplementedError
