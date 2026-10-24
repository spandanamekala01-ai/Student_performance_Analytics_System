
import numpy as np
import pandas as pd

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nStudent", i + 1)

    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    english = float(input("Enter English Marks: "))
    maths = float(input("Enter Maths Marks: "))
    science = float(input("Enter Science Marks: "))
    computer = float(input("Enter Computer Marks: "))

    marks = [english, maths, science, computer]

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Invalid marks! Enter marks between 0 and 100.")
        raise SystemExit

    students.append({
        "Roll No": roll,
        "Name": name,
        "English": english,
        "Maths": maths,
        "Science": science,
        "Computer": computer
    })


df = pd.DataFrame(students)


subject_columns = ["English", "Maths", "Science", "Computer"]
marks_array = df[subject_columns].to_numpy()

df["Total"] = np.sum(marks_array, axis=1)
df["Average"] = np.mean(marks_array, axis=1).round(2)

def calculate_result(row):
    subject_marks = [row[s] for s in subject_columns]

    if any(mark < 35 for mark in subject_marks):
        return "Fail"
    elif row["Average"] >= 75:
        return "Distinction"
    elif row["Average"] >= 60:
        return "First Class"
    else:
        return "Pass"

df["Result"] = df.apply(calculate_result, axis=1)

print("\nSTUDENT PERFORMANCE REPORT")
print(df.to_string(index=False))

print("\nPERFORMANCE ANALYTICS")
print("Total Students:", len(df))
print("Class Average:", round(df["Average"].mean(), 2))

topper = df.loc[df["Total"].idxmax()]
print("Topper Name:", topper["Name"])
print("Topper Total Marks:", topper["Total"])

passed = (df["Result"] != "Fail").sum()
failed = (df["Result"] == "Fail").sum()

print("Passed Students:", passed)
print("Failed Students:", failed)
print("Pass Percentage:",
      round((passed / len(df)) * 100, 2), "%")

print("\nSUBJECT-WISE AVERAGE")
print(df[subject_columns].mean().round(2))

print("\nSTUDENTS NEEDING IMPROVEMENT")
print(df[df["Result"] == "Fail"][["Name", "Average", "Result"]])
