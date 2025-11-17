#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_family_info():
    # моя семья
    my_family = ['Отец', 'Мать', 'Сын', 'Дочь']
    
    # список списков приблизительного роста членов вашей семьи
    my_family_height = [
        ['Отец', 182],
        ['Мать', 165], 
        ['Сын', 190],
        ['Дочь', 160]
    ]
    
    # Рост отца
    father_height = None
    for member in my_family_height:
        if member[0] == 'Отец':
            father_height = member[1]
            break
    
    if father_height:
        print(f"Рост отца - {father_height} см")
    
    # Общий рост семьи
    total_height = sum(member[1] for member in my_family_height)
    print(f"Общий рост моей семьи - {total_height} см")
    
    return father_height, total_height