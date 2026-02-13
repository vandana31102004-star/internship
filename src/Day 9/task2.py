import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

missing = grades.isnull()  # Returns True for None / NaN
print("Missing values in the Series:")
print(missing)

filled_grades = grades.fillna(0)
print("\nGrades after filling missing values:")
print(filled_grades)

high_scores = filled_grades[filled_grades > 60]
print("\nScores greater than 60:")
print(high_scores)


