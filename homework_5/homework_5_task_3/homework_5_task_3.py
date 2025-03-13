import sys
import re
from pathlib import Path
from collections import Counter

def load_logs(file_path: str) -> list:
    """Функція зчитування рядків логів"""
    log_lines = []
    with open(file_path, "r", encoding='utf-8') as file: 
        for line in file:
            parsed_line = parse_log_line(line)
            if parsed_line:  # Перевіряєм, що значення не None
                log_lines.append(parsed_line)
    return log_lines

def parse_log_line(line: str) -> dict:
    """Функція парсінгу рядків логів"""
    pattern = r"([0-9]{4}-[0-9]{2}-[0-9]{2})\s([0-9]{2}:[0-9]{2}:[0-9]{2})\s([A-Za-z]+)\s(.*)"
    match = re.search(pattern, line.strip())    # Перевірка формат рядка логу
    if match:
        log_line = {"date": match.group(1),
                    "time": match.group(2), 
                    "code": match.group(3).upper(),
                    "message": match.group(4)}  
        return log_line

def filter_logs_by_level(logs: list, level: str) -> list:
    """Функція фільтрації рівнів"""
    filtered_lines = [log_line for log_line in logs 
                      if log_line["code"] == level]                
    displayed_lines = []
    for line in filtered_lines:  
        displayed_lines.append(" ".join(line.values()))        
    return displayed_lines

def count_logs_by_level(logs: list) -> dict:
    """Функція підрахунку рівнів"""
    counter = Counter(log["code"] for log in logs)
    return counter

def display_log_counts(counts: dict) -> str:
    """Функція відображення логів"""    
    result = "Рівень логування | Кількість\n"
    result += "-----------------|----------\n"
    for code, count in counts.items():
        result += f"{code:<16} | {count}\n"
    return result

if __name__ == "__main__":
    try:
        directory = Path(sys.argv[1])  # Запис шляху файла в змінну
        logs = load_logs(directory)
        count_log_level = count_logs_by_level(logs)
        display_log_level = display_log_counts(count_log_level)
        print(display_log_level)

        if len(sys.argv) > 2:
            level_code = sys.argv[2].upper()   # Запис рівня логу в змінну
            filter_logs = filter_logs_by_level(logs, level_code)
            
            if filter_logs:
                print(f"Деталі логів для рівня {level_code}:\n")
                for log_line in filter_logs:
                    print(log_line)
            else:
                print("No code found")

    except UnicodeDecodeError:
        print("Error: Invalid file type. Please enter a file in the .txt format.")
    except FileNotFoundError:
        print("Error: No such file found. Please check the path.")   
   
