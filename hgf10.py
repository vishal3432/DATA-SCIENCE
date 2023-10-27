import pandas as pd
student_data1 = pd.DataFrame({
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'name': ['Vishal Singh', 'Aryan Dubey', 'Harsh Pawar', 'Yash Pandey', 'Harshit Tiwari'],
    'marks': [200, 210, 190, 222, 199]
})
new_row = pd.DataFrame({
    'student_id': ['S6'],
    'name': ['Rahul Khan'],
    'marks': [205]
})
student_data1 = student_data1._append(new_row, ignore_index=True)
print(student_data1)
