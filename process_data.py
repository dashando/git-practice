"""
Модуль фильтрации и статистического анализа экспериментальных данных.
"""
import json

def filter_records(records, threshold=50):
    return [r for r in records if r.get("score", 0) >= threshold]

def calculate_average(records):
    if not records:
        return 0.0
    return sum(r["score"] for r in records) / len(records)
