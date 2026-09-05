# Day 7 — OOP I

class Habit:
    category = "general"

    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.completions = 0

    def complete(self):
        self.completions += 1

    def is_done(self):
        return self.completions >= self.goal

    def progress(self):
        return f"{self.name}: {self.completions}/{self.goal}"

    def reset(self):
        self.completions = 0

    def rename(self, new_name):
        self.name = new_name

    def set_goal(self, new_goal):
        self.goal = new_goal

    def status(self):
        if self.is_done():
            return "done"
        return "in progress"

    def __str__(self):
        return f"Habit {self.name}: {self.completions}/{self.goal}"


if __name__ == "__main__":
    coding = Habit("Python", 2)
    reading = Habit("Reading", 1)

    assert coding.is_done() is False
    coding.complete()
    coding.complete()
    assert coding.is_done() is True
    assert coding.completions == 2
    assert reading.completions == 0

    print(coding.progress())
