#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def manage_zoo():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    print(f"Исходный зоопарк: {zoo}")
    
    # посадите медведя (bear) между львом и кенгуру
    zoo.insert(1, 'bear')
    print(f"После добавления медведя: {zoo}")
    
    # добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark']
    zoo.extend(birds)
    print(f"После добавления птиц: {zoo}")
    
    # уберите слона
    zoo.remove('elephant')
    print(f"После удаления слона: {zoo}")
    
    # выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark)
    lion_index = zoo.index('lion') + 1  
    lark_index = zoo.index('lark') + 1
    
    print(f"Лев сидит в клетке №{lion_index}")
    print(f"Жаворонок сидит в клетке №{lark_index}")
    
    return zoo, lion_index, lark_index