from dataclasses import dataclass
from datetime import datetime


@dataclass
class Creneau:
    date_start: datetime
    date_end: datetime
