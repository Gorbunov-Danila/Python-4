#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def trapezoid_perimeter(base1, base2, height):
    """
    Вычисляет периметр равнобедренной трапеции.

    :param base1: Длина первого основания
    :param base2: Длина второго основания
    :param height: Высота трапеции
    :return: Периметр трапеции
    """
    side_length = ((base2 - base1) ** 2 + height ** 2) ** 0.5  # Длина бокового отрезка
    perimeter = base1 + base2 + 2 * side_length  # Периметр трапеции
    return perimeter

if __name__ == "__main__": 
    # Пример использования функции
    base1 = float(input("Введите длину первого основания трапеции: "))
    base2 = float(input("Введите длину второго основания трапеции: "))
    height = float(input("Введите высоту трапеции: "))

    result = trapezoid_perimeter(base1, base2, height)
    print(f"Периметр трапеции: {result}")
