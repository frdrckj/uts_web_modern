from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

class TransportType(Enum):
    BUS = 'bus'
    TRAVEL = 'travel'

@dataclass
class Member:
    id: Optional[int]
    code: str
    name: str
    transport_type: TransportType
    registration_date: datetime = None

    @property
    def fee_amount(self) -> int:
        if self.transport_type == TransportType.BUS:
            return 100000
        else:
            return 50000

    @staticmethod
    def from_db_row(row: dict) -> 'Member':
        return Member(
            id=row['id'],
            code=row['code'],
            name=row['name'],
            transport_type=TransportType(row['transport_type']),
            registration_date=row['registration_date']
        )

@dataclass
class Attendance:
    id: Optional[int]
    member_id: int
    check_in_time: datetime
    attendance_number: int

    @staticmethod
    def from_db_row(row: dict) -> 'Attendance':
        return Attendance(
            id=row['id'],
            member_id=row['member_id'],
            check_in_time=row['check_in_time'],
            attendance_number=row['attendance_number']
        )

@dataclass
class Payment:
    id: Optional[int]
    member_id: int
    amount: float
    payment_date: datetime
    attendance_cycle: int

    @staticmethod
    def from_db_row(row: dict) -> 'Payment':
        return Payment(
            id=row['id'],
            member_id=row['member_id'],
            amount=row['amount'],
            payment_date=row['payment_date'],
            attendance_cycle=row['attendance_cycle']
        )