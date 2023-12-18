"""
Задача 1.
1.Напишіть функцію, яка отримує послідовність балів (цілі числа) і повертає
буквенну інтерпретацію числових балів на основі наступної шкали оцінок:
90-100 - A
80-89 - B
70-79 - C
60-69 - D
Нижче 60 - F

Автор: Волочнюк Поліна
"""

def get_grade(score):
    if score >= 90: 
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C' 
    elif score >=60:
        return 'D'
    else:
        return 'F'

def assign_grades(scores):
    grades = {'A':[], 'B':[], 'C':[], 'D':[], 'F':[]}
    for score in scores:
        grade = get_grade(score) 
        grades[grade].append(score)
    return grades

scores = [60, 80, 64, 45, 35, 87, 90, 95, 91, 64, 78]  
result = assign_grades(scores)
print(result)
