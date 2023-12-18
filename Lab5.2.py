"""
Задача 2.
2.Напишіть функцію, яка вибирає випадкове слово з переліку слів із словника
SOWPODS (sowpods.txt). Кожен рядок у файлі містить одне слово.

Автор: Волочнюк Поліна
"""
import random

def get_random_word(file):
    with open(file, 'r') as f:
        words = f.readlines()
        
    return random.choice(words).strip()

f = 'sowpods.txt'
random_word = get_random_word(f)
print(random_word)
