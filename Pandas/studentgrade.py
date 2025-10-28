import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 90, 66, 95],
    'Science': [88, 72, 85, 70, 89],
    'English': [75, 80, 70, 60, 98]
}

df = pd.DataFrame(data)
print(df)


df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Average'] = df['Total'] / 3


def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Average'].apply(assign_grade)



top_students = df[df['Grade'].isin(['A', 'B'])]
print(top_students)


df_sorted = df.sort_values(by='Total', ascending=False)

df_sorted.to_csv('student_report.csv', index=False)
