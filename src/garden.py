#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def analyze_flowers():
    """Анализ цветов в саду и на лугу"""
    # в саду сорвали цветы
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    
    # на лугу сорвали цветы  
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
    
    
    garden_set = set(garden)
    meadow_set = set(meadow)
    
    # все виды цветов
    all_flowers = garden_set.union(meadow_set)
    print(f"Все виды цветов: {all_flowers}")
    
    # которые растут и там и там
    common_flowers = garden_set.intersection(meadow_set)
    print(f"Растут и в саду и на лугу: {common_flowers}")
    
    # которые растут в саду, но не на лугу
    only_garden = garden_set.difference(meadow_set)
    print(f"Только в саду: {only_garden}")
    
    # которые растут на лугу, но не в саду
    only_meadow = meadow_set.difference(garden_set)
    print(f"Только на лугу: {only_meadow}")
    
    return garden_set, meadow_set, all_flowers, common_flowers, only_garden, only_meadow