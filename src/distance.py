#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_distances():
    """Расчет расстояний между городами"""
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }

    distances = {}
    
    for ct1, coords1 in sites.items():
        distances[ct1] = {}
        for ct2, coords2 in sites.items():
            if ct1 != ct2:
                distance = ((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2) ** 0.5
                distances[ct1][ct2] = round(distance, 2)
    
    print("Расстояния между городами:")
    for ct1 in distances:
        for ct2 in distances[ct1]:
            print(f"{ct1} - {ct2}: {distances[ct1][ct2]}")
    
    return distances