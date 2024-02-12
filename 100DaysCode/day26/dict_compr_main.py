# 
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# 

import random
names = ['Sony', 'Alex', 'Ammu', 'Annie']
students_score = {student:random.randint(75, 100) for student in names}
print (students_score)

passed_students = {student:score for (student, score) in students_score.items() if score >=70}
print (passed_students)

inp_sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in inp_sentence.split()}
print(result)


temp = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# res_f = {print(day, temp) for (day, temp) in temp.items()}
# Always first print the items the way you want it, then modify the comprehension with steps you want it to do
res_f = {(day, temp * 9/5 + 32) for (day, temp) in temp.items()}
print(res_f)

import pandas

student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56,76,98]
}

# Looping in dict
# for (key, value) in student_dict.items():
#   print(key)
#   print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
