#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import src.distance as distance_module
import src.circle as circle_module
import src.operations as operations_module
import src.favorite_movies as movies_module
import src.my_family as family_module
import src.zoo as zoo_module
import src.songs_list as songs_module
import src.secret as secret_module
import src.garden as garden_module
import src.shopping as shopping_module
import src.store as store_module

def main():
    
    # Задание 00: Расстояния между городами
    print("1. Расстояния между городами:")
    distance_module.calculate_distances()
    print()
    
    # Задание 01: Площадь круга и проверка точек
    print("2. Площадь круга и проверка точек:")
    circle_module.calculate_circle()
    print()
    
    # Задание 02: Математические операции
    print("3. Математические операции:")
    operations_module.calculate_operations()
    print()
    
    # Задание 03: Любимые фильмы
    print("4. Любимые фильмы:")
    movies_module.print_movies()
    print()
    
    # Задание 04: Моя семья
    print("5. Моя семья:")
    family_module.print_family_info()
    print()
    
    # Задание 05: Зоопарк
    print("6. Зоопарк:")
    zoo_module.manage_zoo()
    print()
    
    # Задание 06: Список песен
    print("7. Список песен:")
    songs_module.calculate_songs_time()
    print()
    
    # Задание 07: Секретное сообщение
    print("8. Секретное сообщение:")
    secret_module.decode_message()
    print()
    
    # Задание 08: Сад и луг
    print("9. Сад и луг:")
    garden_module.analyze_flowers()
    print()
    
    # Задание 09: Покупки
    print("10. Покупки:")
    shopping_module.analyze_prices()
    print()
    
    # Задание 10: Магазин
    print("11. Магазин:")
    store_module.calculate_store_value()
    print()

if __name__ == "__main__":
    main()