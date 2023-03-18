""" LAB 05 - 01/07/23
Aliasing - Sterling Miller
"""
from typing import List, Set, Dict, Optional


class Student:
    def __init__(self, name: str,
                 interests: List[str]):
        self.name = name
        self.interests = interests
        self.freetimes = set([8, 9, 10, 11, 12, 13, 14, 15])
        self.meetings: List[int] = []

    def schedule_meeting(self, time: int):
        for meeting in self.freetimes:
            if meeting == time:
                self.freetimes.remove(meeting)
                self.meetings.append(time)
                return
        return print("The time is taken")


class Club:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Student] = []
        self.meeting_time: Optional[int] = None

    def __str__(self) -> str:
        member_names = [member.name for member in self.members]
        return f"{self.name} ({', '.join(member_names)})"

    def join(self, student: Student):
        return self.members.append(student)

    def find_common_time(self) -> int:
        for time in range(8, 16):
            common_time = True
            for student in self.members:
                if time not in student.freetimes:
                    common_time = False
                if common_time is True:
                    return time
        return 0

    def schedule(self, time: int):
        self.meeting_time = time
        for member in self.members:
            member.schedule_meeting(time)


class ASUO:
    def __init__(self):
        self.students: List[Student] = []
        self.clubs: List[Club] = []

    def enroll(self, s: Student):
        return self.students.append(s)

    def form_clubs(self):
        clubs_to_form: Dict[str, Club] = {}

        for student in self.students:
            for interest in student.interests:
                if interest not in clubs_to_form:
                    clubs_to_form[interest] = Club(interest)
                clubs_to_form[interest].join(student)
            self.clubs = clubs_to_form.values()

    def schedule_clubs(self):
        for club in self.clubs:
            time = club.find_common_time()
            if time > 0:
                club.schedule(time)

    def print_club_schedule(self):
        for club in self.clubs:
            if club.meeting_time is not None:
                print(f"{club} meets at {club.meeting_time}")


def main():
    asuo = ASUO()
    asuo.enroll(Student("Marty", ["badminton", "robotics"]))
    asuo.enroll(Student("Kim", ["backgammon"]))
    asuo.enroll(Student("Tara", ["robotics", "horticulture", "chess"]))
    asuo.enroll(Student("George", ["chess", "badminton"]))

    asuo.form_clubs()
    asuo.schedule_clubs()
    asuo.print_club_schedule()


if __name__ == '__main__':
    main()
