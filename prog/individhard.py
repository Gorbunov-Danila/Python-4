#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def calculate_angle(hour, minute):
    """
    Рассчитывает угол между часовой и минутной стрелкой, количество полных часов и минут.

    :param hour: Час (в диапазоне от 1 до 12)
    :param minute: Минута (в диапазоне от 0 до 59)
    :return: Угол, количество полных часов, количество полных минут
    """
    if not (1 <= hour <= 12) or not (0 <= minute <= 59):
        raise ValueError("Некорректные значения часа или минуты")

    # Угол между часовой стрелкой и 12-часовым лучом
    angle_per_hour = 360 / 12
    hour_angle = (hour % 12) * angle_per_hour + (minute / 60) * angle_per_hour

    # Угол между минутной стрелкой и 12-часовым лучом
    angle_per_minute = 360 / 60
    minute_angle = minute * angle_per_minute

    # Общий угол между часовой и минутной стрелками
    angle_between = abs(hour_angle - minute_angle)
    angle_between = min(360 - angle_between, angle_between)  # Выбираем минимальный угол

    # Количество полных часов и минут
    full_hours = hour
    full_minutes = hour * 60 + minute

    return angle_between, full_hours, full_minutes

if __name__ == "__main__":
    # Пример использования функции
    hour_input = int(input("Введите текущий час (от 1 до 12): "))
    minute_input = int(input("Введите текущую минуту (от 0 до 59): "))

    angle, full_hours, full_minutes = calculate_angle(hour_input, minute_input)
    print(f"Угол между часовой и минутной стрелками: {angle} градусов")
    print(f"Количество полных часов: {full_hours}")
    print(f"Количество полных минут: {full_minutes}")
