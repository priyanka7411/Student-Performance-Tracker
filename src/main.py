# src/main.py

from student import Student
from utils import load_data, save_to_csv, save_to_json, save_to_pickle
import pandas as pd

# Load student data from CSV
data_file = 'data\StudentsPerformance.csv'
df = load_data(data_file)

# Create a list of Student objects
students = []

for index, row in df.iterrows():
    gender = row['gender']
    race_ethnicity = row['race/ethnicity']
    parental_education = row['parental level of education']
    lunch = row['lunch']
    prep_course = row['test preparation course']
    scores = {
        'Math': row['math score'],
        'Reading': row['reading score'],
        'Writing': row['writing score']
    }
    student = Student(gender, race_ethnicity, parental_education, lunch, prep_course, scores)
    students.append(student)

# Print average scores for all students
for student in students:
    print(f"{student.gender}, {student.race_ethnicity}: {student.average_score()}")

# Get top performer
top_student = max(students, key=lambda s: s.average_score())
print(f"Top Performer: {top_student.gender}, {top_student.race_ethnicity} with average score {top_student.average_score()}")

# Filter students who completed the test preparation course and have an average score above 80
threshold = 80
filtered_students = list(filter(lambda s: s.prep_course == 'completed' and s.average_score() > threshold, students))

print(f"Students with average score above {threshold} and completed the test preparation course:")
for student in filtered_students:
    print(f"{student.gender}, {student.race_ethnicity}: {student.average_score()}")

# Save the processed student data
output_data = [{'Gender': student.gender, 'Race/Ethnicity': student.race_ethnicity, 
                'Average Score': student.average_score()} for student in students]
save_to_csv(pd.DataFrame(output_data), 'output/processed_students.csv')
save_to_json(output_data, 'output/processed_students.json')
save_to_pickle(output_data, 'output/processed_students.pkl')
