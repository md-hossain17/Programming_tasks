# timestamp_lib.py
from datetime import datetime
from typing import List

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

WEEKDAYS = [
    "Monday", "Tuesday", "Wednesday", "Thursday", 
    "Friday", "Saturday", "Sunday"
]

def readTimestamps(PFilename: str, PTimestamps: List[datetime]) -> None:
    # Your implementation here
    pass

def calculateYears(PYear: int, PTimestamps: List[datetime]) -> int:
    # Your implementation here
    pass

def calculateMonths(PMonth: str, PTimestamps: List[datetime]) -> int:
    # Your implementation here
    pass

def calculateWeekdays(PWeekday: str, PTimestamps: List[datetime]) -> int:
    # Your implementation here
    pass