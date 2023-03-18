"""Test suite to accompany mini-exam 1"""

import unittest
from loonweb import Course, Offerings, Schedule, NO_SUCH_COURSE

class TestOfferings(unittest.TestCase):
    def setUp(self) -> None:
        self.loonweb = Offerings()
        self.loonweb.load([
            Course("FSH", 210, "Scooping up minnows", 900),
            Course("FSH", 211, "Swallowing minnows", 900),
            Course("FSH", 300, "Catching frogs", 1000),
            Course("FLY", 239, "Takeoffs and landings", 1000),
            Course("FLY", 232, "Diving into water", 1000),
            Course("SWM", 251, "Paddling I", 1000),
            Course("VOI", 104, "Weird yodeling", 1300),
            Course("VOI", 107, "Tremolo", 1400),
            Course("VOI", 232, "Screeching", 1700)
        ])

    def test_select_present(self):
        self.assertEqual(Course("VOI", 232, "Screeching", 1700),
                         self.loonweb.select("VOI", 232))
        self.assertEqual(Course("VOI", 107, "Tremolo", 1400),
                         self.loonweb.select("VOI", 107))

    def test_select_absent(self):
        self.assertEqual(NO_SUCH_COURSE,
                         self.loonweb.select("VOI", 108))
        self.assertEqual(NO_SUCH_COURSE,
                         self.loonweb.select("FEA", 210))

class TestSchedule(unittest.TestCase):
    def setUp(self) -> None:
        self.fish_211 = Course("FSH", 211, "Swallowing minnows", 900)
        self.fly_239 = Course("FLY", 239, "Takeoffs and landings", 1000)
        self.voice_107 = Course("VOI", 107, "Tremolo", 1400)
        self.voice_104 = Course("VOI", 104, "Weird yodeling", 1300)

        self.martin = Schedule()
        self.martin.append(self.fish_211)  # 900
        self.martin.append(self.voice_107) # 1400
        self.martin.append(self.fly_239)   # 1000

        self.elsa = Schedule()
        self.elsa.append(self.fly_239)
        self.elsa.append(self.voice_104)
        self.elsa.append(self.fish_211)

    def test_together(self):
        together = self.martin.together(self.elsa)
        expected = Schedule()
        expected.append(self.fish_211)
        expected.append(self.fly_239)
        self.assertEqual(expected, together)

    def test_free_at(self):
        # Martin is in class at 900, 1400, 1000
        self.assertTrue(self.martin.free_at(1500))
        self.assertFalse(self.martin.free_at(1000))


if __name__ == "__main__":
    unittest.main()


