#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_movies():

    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    
    # Первый фильм
    first_comma = my_favorite_movies.find(',')
    first_movie = my_favorite_movies[:first_comma]
    
    # Последний фильм  
    last_comma = my_favorite_movies.rfind(',')
    last_movie = my_favorite_movies[last_comma + 2:]
    
    # Второй фильм
    second_comma = my_favorite_movies.find(',', first_comma + 1)
    second_movie = my_favorite_movies[first_comma + 2:second_comma]
    
    # Второй с конца
    prev_last_comma = my_favorite_movies.rfind(',', 0, last_comma)
    second_last_movie = my_favorite_movies[prev_last_comma + 2:last_comma]
    
    print(f"Первый фильм: {first_movie}")
    print(f"Последний фильм: {last_movie}") 
    print(f"Второй фильм: {second_movie}")
    print(f"Второй с конца: {second_last_movie}")
    
    return [first_movie, last_movie, second_movie, second_last_movie]