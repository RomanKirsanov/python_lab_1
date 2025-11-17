#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_songs_time():
    # Работа со списком
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]
    
    # Время трех песен из списка
    time1 = 0
    for song in violator_songs_list:
        if song[0] in ['Halo', 'Enjoy the Silence', 'Clean']:
            time1 += song[1]
    
    print(f"Три песни звучат {round(time1, 2)} минут")
    
    # Работа со словарем
    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }
    
    # Время других трех песен
    time2 = (violator_songs_dict['Sweetest Perfection'] + 
             violator_songs_dict['Policy of Truth'] + 
             violator_songs_dict['Blue Dress'])
    
    print(f"А другие три песни звучат {round(time2, 2)} минут")
    
    return time1, time2