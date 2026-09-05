# Day 8 — OOP II

from day_07_oop_i import Habit


class TimedHabit(Habit):
    def __init__(self, name, goal, minutes):
        super().__init__(name, goal)
        self.minutes = minutes

    def progress(self):
        return f"{self.name}: {self.completions}/{self.goal}, {self.minutes} min"


class HabitTracker:
    def __init__(self):
        self.habits = []

    def add(self, habit):
        self.habits.append(habit)

    def completed_names(self):
        completed = []
        for habit in self.habits:
            if habit.is_done():
                completed.append(habit.name)
        return completed

    def complete(self, name):
        for habit in self.habits:
            if habit.name == name:
                habit.complete()
                return True
        return False


if __name__ == "__main__":
    tracker = HabitTracker()

    tracker.add(Habit("Python", 2))
    tracker.add(Habit("Reading", 1))
    tracker.add(TimedHabit("Backend", 1, 45))

    print(tracker.complete("Reading"))
    print(tracker.complete("Unknown"))
    print(tracker.completed_names())

    habits = [
        Habit("Reading", 1),
        TimedHabit("Python", 2, 45),
    ]

    for habit in habits:
        print(habit.progress())
