from datetime import datetime, timedelta
from typing import Optional, List, Dict
from models import Member, Attendance, Payment, TransportType
from math import ceil

class MembershipDB:
    def __init__(self, db_config):
        self.db = db_config

    def register_member(self, code: str, name: str, transport_type: str) -> int:
        query = """
        INSERT INTO members (code, name, transport_type)
        VALUES (%s, %s, %s)
        """
        return self.db.execute_query(query, (code, name, transport_type))

    def get_member_by_code(self, code: str) -> Optional[Member]:
        query = """
        SELECT id, code, name, transport_type, registration_date
        FROM members
        WHERE code = %s
        """
        result = self.db.execute_query(query, (code,))
        return Member.from_db_row(result[0]) if result else None

    def get_all_members(self, page: int = 1, per_page: int = 15) -> List[Member]:
        offset = (page - 1) * per_page
        query = """
        SELECT id, code, name, transport_type, registration_date
        FROM members
        ORDER BY registration_date DESC
        LIMIT %s OFFSET %s
        """
        results = self.db.execute_query(query, (per_page, offset))
        return [Member.from_db_row(row) for row in results] if results else []

    def get_total_members(self) -> int:
        query = "SELECT COUNT(*) as count FROM members"
        result = self.db.execute_query(query)
        return result[0]['count'] if result else 0

    def record_attendance(self, member_id: int) -> int:
        # Get current attendance count
        count_query = """
        SELECT COUNT(*) as count
        FROM attendances
        WHERE member_id = %s
        """
        result = self.db.execute_query(count_query, (member_id,))
        attendance_count = result[0]['count'] if result else 0
        attendance_number = (attendance_count % 5) + 1

        # Insert attendance record
        attendance_query = """
        INSERT INTO attendances (member_id, attendance_number)
        VALUES (%s, %s)
        """
        attendance_id = self.db.execute_query(attendance_query, (member_id, attendance_number))

        if attendance_number == 5:
            member = self.get_member_by_id(member_id)
            if member:
                payment_query = """
                INSERT INTO payments (member_id, amount, attendance_cycle)
                VALUES (%s, %s, %s)
                """
                self.db.execute_query(
                    payment_query, 
                    (member_id, member.fee_amount * 5, (attendance_count // 5) + 1)
                )

        return attendance_id

    def get_member_by_id(self, member_id: int) -> Optional[Member]:
        query = """
        SELECT id, code, name, transport_type, registration_date
        FROM members
        WHERE id = %s
        """
        result = self.db.execute_query(query, (member_id,))
        return Member.from_db_row(result[0]) if result else None

    def get_recent_attendances(self, page: int = 1, per_page: int = 15) -> List[Dict]:
        try:
            offset = (page - 1) * per_page
            query = """
            SELECT 
                a.id,
                a.member_id,
                a.check_in_time,
                a.attendance_number,
                m.code as member_code,
                m.name as member_name,
                m.transport_type as member_transport_type
            FROM attendances a
            JOIN members m ON a.member_id = m.id
            ORDER BY a.check_in_time DESC
            LIMIT %s OFFSET %s
            """
            results = self.db.execute_query(query, (per_page, offset))
            if results is None:
                print("No results returned from attendance query")
                return []
                
            return results
        except Exception as e:
            print(f"Error in get_recent_attendances: {str(e)}")
            return []

    def get_total_attendances(self) -> int:
        query = "SELECT COUNT(*) as count FROM attendances"
        result = self.db.execute_query(query)
        return result[0]['count'] if result else 0

    def get_payments(self, page: int = 1, per_page: int = 15) -> List[Dict]:
        try:
            offset = (page - 1) * per_page
            query = """
            SELECT 
                p.id,
                p.member_id,
                p.amount,
                p.payment_date,
                p.attendance_cycle,
                m.code as member_code,
                m.name as member_name,
                m.transport_type as member_transport_type
            FROM payments p
            JOIN members m ON p.member_id = m.id
            ORDER BY p.payment_date DESC
            LIMIT %s OFFSET %s
            """
            results = self.db.execute_query(query, (per_page, offset))
            if results is None:
                print("No results returned from payments query")
                return []
                
            return results
        except Exception as e:
            print(f"Error in get_payments: {str(e)}")
            return []

    def get_total_payments(self) -> int:
        query = "SELECT COUNT(*) as count FROM payments"
        result = self.db.execute_query(query)
        return result[0]['count'] if result else 0

    def check_attendance_cooldown(self, member_id: int, cooldown_minutes: int) -> bool:
        query = """
        SELECT check_in_time
        FROM attendances
        WHERE member_id = %s
        ORDER BY check_in_time DESC
        LIMIT 1
        """
        result = self.db.execute_query(query, (member_id,))
        if result:
            last_attendance = result[0]['check_in_time']
            cooldown = timedelta(minutes=cooldown_minutes)
            return datetime.now() - last_attendance < cooldown
        return False