#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import sys
import os

# Добавляем путь к корневой папке в sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Теперь импортируем модули
try:
    from src.distance import calculate_distances
    from src.circle import calculate_circle
    from src.operations import calculate_operations
    from src.favorite_movies import print_movies
    from src.my_family import print_family_info
    from src.zoo import manage_zoo
    from src.songs_list import calculate_songs_time
    from src.secret import decode_message
    from src.garden import analyze_flowers
    from src.shopping import analyze_prices
    from src.store import calculate_store_value
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure you have src folder with all modules")


def test_calculate_distances():
    """Тест расчета расстояний между городами"""
    distances = calculate_distances()
    assert 'Moscow' in distances


def test_circle():
    """Тест площади круга и проверки точек"""
    area, point1_result, point2_result = calculate_circle()
    expected_area = 3.1415926 * 42 ** 2
    assert abs(area - expected_area) < 0.0001


def test_movies():
    """Тест извлечения названий фильмов"""
    movies = print_movies()
    assert len(movies) == 4


def test_garden():
    """Тест операций с множествами цветов"""
    garden_set, meadow_set, all_flowers, common_flowers, only_garden, only_meadow = analyze_flowers()
    assert isinstance(garden_set, set)


def test_family():
    """Тест информации о семье"""
    father_height, total_height = print_family_info()
    assert father_height == 182


def test_operation():
    """Тест математических операций"""
    result = calculate_operations()
    assert result == 25


def test_shopping():
    """Тест анализа цен"""
    sweets = analyze_prices()
    assert isinstance(sweets, dict)


def test_songs():
    """Тест расчета времени песен"""
    time1, time2 = calculate_songs_time()
    assert time1 > 0


def test_secret():
    """Тест декодирования секретного сообщения"""
    decoded_parts = decode_message()
    assert isinstance(decoded_parts, str)


def test_store():
    """Тест расчета стоимости товаров"""
    results = calculate_store_value()
    assert 'Лампа' in results


def test_zoo():
    """Тест операций с зоопарком"""
    zoo, lion_index, lark_index = manage_zoo()
    assert 'bear' in zoo