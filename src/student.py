# src/student.py

class Student:
    def __init__(self, gender, race_ethnicity, parental_education, lunch, prep_course, scores):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_education = parental_education
        self.lunch = lunch
        self.prep_course = prep_course
        self.scores = scores  # Dictionary of subject: score

    def average_score(self):
        return sum(self.scores.values()) / len(self.scores)

    def top_subject(self):
        return max(self.scores, key=self.scores.get)

    def __str__(self):
        return f"Student({self.gender}, {self.race_ethnicity}, {self.parental_education}, {self.scores})"
