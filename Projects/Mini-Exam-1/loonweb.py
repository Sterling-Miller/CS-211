"""Mini-exam 1, CS 211, U. Oregon Winter 2023.
Instructions are in doc comments like this one.

There are three methods for you to write.  Each is marked
with a #FIXME comment attached to a dummy statement. 
"""

"""
A course at Aves University, whose mascot is the Loon, 
has a subject code (e.g., FSH), an integer course number (e.g., 211),
 a short title (e.g., "Fishing for minnows"), and a time. To
 simplify scheduling, all Aves University courses take one hour, 
 so a course time can be represented by an integer like 900 for 9:00am
 or 1500 for 3:00pm.   I have provided class Course for you:
"""


class Course:
    """A course offering at Aves University"""

    def __init__(self, subj: str, num: int, title: str, time: int):
        self.subj = subj
        self.num = num
        self.title = title
        self.time = time

    def __str__(self) -> str:
        """The printed representation of an Aves University course"""
        return f"{self.subj} {self.num}:  {self.title}  (MUWHF {self.time:04})"

    def __repr__(self) -> str:
        """The debugging representation of an Aves University course"""
        return f"Course('{self.subj}', {self.num:3}, '{self.title}' {self.time:4})"

    def __eq__(self, other: "Course") -> bool:
        return self.subj == other.subj and self.num == other.num


# It will be useful to have a special error value, e.g., when a
# course cannot be found in the schedule of classes.
NO_SUCH_COURSE = Course("XXX", 0, "NO SUCH COURSE", 0)

"""A CourseList is a base class that wraps a list of courses. """


class CourseList:
    """Any list of courses.  Abstract base class."""

    def __init__(self):
        self.courses: list[Course] = []

    def append(self, course: Course):
        """Delegate to list"""
        self.courses.append(course)

    def load(self, courses: list[Course]):
        for course in courses:
            self.append(course)

    def __len__(self) -> int:
        """Delegate to list"""
        return len(self.courses)


"""A schedule of offerings  indicates which courses are available to
a student in an academic term.  The select method, which you write,
returns a course with a matching subject code and number, or 
NO_SUCH_COURSE if there is no matching course in the schedule.
(A linear search is ok.)  
"""


class Offerings(CourseList):
    """A collection of available classes in an academic term"""

    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        """Printed form, one line per class, in order by subject and number"""
        courses = sorted(self.courses, key=lambda course: str(course))
        return "\n".join(str(course) for course in courses)

    def select(self, subj: str, num: int) -> Course:
        """Returns the matching Course object
        or NO_SUCH_COURSE if there is no such course in self.items.
        """
        for course in self.courses:
            if course.subj == subj and course.num == num:
                return course
        return NO_SUCH_COURSE  # FIXME: write this method


"""A student schedule is another kind of course list.  
You must write two methods: 
- free_at(t):  True if a student does NOT have a class at hour t
- together(other): List of courses that student and other are
  both enrolled in. 
"""


class Schedule(CourseList):
    """A collection of courses taken by a student"""

    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        """Printed form, one line per class, in order by start time"""
        courses = sorted(self.courses, key=lambda course: course.time)
        return "\n".join(str(course) for course in courses)

    def __repr__(self) -> str:
        """Sames as str but bracketed"""
        return f"Schedule([\n{self}\n])"

    def __eq__(self, other: "Schedule") -> bool:
        return (sorted(self.courses, key=lambda c: str(c))
                == sorted(other.courses, key=lambda c: str(c)))

    def free_at(self, time: int) -> bool:
        """True if not in class at weekday time"""
        for course in self.courses:
            if course.time == time:
                return False
        return True  # FIXME: Write this method

    def together(self, other: "Schedule") -> "Schedule":
        """What courses are we taking together?"""
        together = Schedule()
        for item in self.courses:
            for course in other.courses:
                if item == course:
                    together.append(course)
        return together  # FIXME: Write this method


def main():
    """Just an example"""
    print("Running sample, Juan and Mary enrolling through Loonweb")
    loonweb = Offerings()
    loonweb.load([
        Course("FSH", 210, "Scooping up minnows", 900),
        Course("FSH", 211, "Swallowing minnows", 900),
        Course("FSH", 300, "Catching frogs", 1000),
        Course("FLY", 231, "Takeoffs and landings", 1000),
        Course("FLY", 232, "Diving into water", 1000),
        Course("SWM", 251, "Paddling I", 1000),
        Course("VOI", 105, "Weird yodeling", 1300),
        Course("VOI", 107, "Tremolo", 1400)
    ])
    assert loonweb.select("FLY", 355) == NO_SUCH_COURSE
    # Smoke test of selection and equality test
    fly_211 = Course("FLY", 231, "Title ignored", 900)
    selection = loonweb.select("FLY", 231)
    assert selection == fly_211
    # Schedules for two students
    juan = Schedule()
    juan.append(loonweb.select("FSH", 211))
    juan.append(loonweb.select("FLY", 231))
    juan.append(loonweb.select("VOI", 107))
    mary = Schedule()
    mary.append(loonweb.select("VOI", 105))
    mary.append(loonweb.select("FLY", 231))
    mary.append(loonweb.select("FSH", 211))
    together = juan.together(mary)
    print(together)
    # Expected output:
    # FSH 211:  Swallowing minnows  (MUWHF 900)
    # FLY 231:  Takeoffs and landings  (MUWHF 1000)
    print(f"Juan free at 1000? Expect false. {juan.free_at(1000)}")
    print(f"Juan free at 1300? Expect true.  {juan.free_at(1300)}")


if __name__ == "__main__":
    main()
