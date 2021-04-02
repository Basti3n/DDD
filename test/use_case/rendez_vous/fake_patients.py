from typing import List

from src.model.patient.patient import Patient
from src.model.patient.patient_repository import PatientRepository


class FakePatients(PatientRepository):

    def __init__(self):
        self.patients = [Patient(1, 'Alice'), Patient(2, 'Bob'), Patient(3, 'Tom')]

    def find_patient_by_id(self, patient_id: int) -> Patient:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise Exception

    def find_patients(self) -> List[Patient]:
        return self.patients
