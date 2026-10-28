"""
Главный исполняемый модуль проекта лабораторной работы №5.
Демонстрация версионирования исходного кода в Git.
"""

import json

def load_config(path: str = "config.json") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    config = load_config()
    print(f"Запуск проекта: {config.get('project_name')}")
    print(f"Версия: {config.get('version')}, Автор: {config.get('author')}")

if __name__ == "__main__":
    main()
