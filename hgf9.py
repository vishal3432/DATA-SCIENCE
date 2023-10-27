import pandas as pd
student_data1 = pd.DataFrame({
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
   'name': ['Vishal Singh', 'Prince Bhatt', 'Lakshya Rajput', 'Shiva Gupta', 'Ansh Jain'],
    'marks': [200, 210, 190, 222, 199]
})
student_data2 = pd.DataFrame({
    'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
    'name': ['Rahul Dubey', 'Aryan Dubey', 'Harsh Pawar', 'Yash Pandey', 'Harshit Tiwari'],
    'marks': [201, 200, 198, 219, 201]
})
merged_data = pd.concat([student_data1, student_data2], axis=1)
print(merged_data)
