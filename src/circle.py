#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_circle():
    """Расчет площади круга и проверка точек"""
    radius = 42
    pi = 3.1415926
    
    # Площадь круга
    area = pi * radius ** 2
    print(f"Площадь круга: {round(area, 4)}")
    
    # Проверка точек
    point_1 = (23, 34)
    point_2 = (30, 30)
    
    def is_point_in_circle(point, radius=42):
        distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
        return distance <= radius
    
    result1 = is_point_in_circle(point_1)
    result2 = is_point_in_circle(point_2)
    
    print(f"Точка {point_1} в круге: {result1}")
    print(f"Точка {point_2} в круге: {result2}")
    
    return area, result1, result2