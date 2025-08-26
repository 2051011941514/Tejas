# Analysing Grading of student With Help of Numpy and Pandas
import pandas as pd
df = pd.read_csv(r"T:\Python datasets\archive (1)\Student_performance_10k.csv") # Taken data from Kaggle
print(df.head)
df_clean =df[['roll_no','total_score']]
print(df_clean)
print(df_clean.isnull().sum()) # taking sum of the null values 
df_clean_na = df_clean.dropna(subset=['roll_no','total_score']) # droping the null values 
print(df_clean_na.isnull().sum())
print("Original rows", len(df_clean))
print("New rows", len(df_clean_na))
import numpy as np
arr_1 = df_clean_na['total_score']
score = np.array([arr_1])
print(score)
grade_A = (score>=360)
grade_B = (score>=320) & (score<=360)
grade_C = (score>=280) & (score<=320)
grade_D = (score>=240) & (score<=280)
grade_E = (score<=240)

Score_A = score[grade_A]
Score_B = score[grade_B]
Score_C = score[grade_C]
Score_D = score[grade_D]
Score_E = score[grade_E]

Count_A =np.sum(grade_A)
Count_B =np.sum(grade_B)
Count_C =np.sum(grade_C)
Count_D =np.sum(grade_D)
Count_E =np.sum(grade_E)


print(f"No of Students with Grades:\nGrade-A: {Count_A}\nGrade-B: {Count_B}\nGrade-C: {Count_C}\nGrade-D: {Count_D}\nGrade-E: {Count_E}")

print(f"\nScores of Grade-A Students: {Score_A}\nGrade-B: {Score_B}\nGrade-C: {Score_C}\nGrade-D: {Score_D}\nGrade-E: {Score_E}")
