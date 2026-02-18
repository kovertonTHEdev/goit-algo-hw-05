import sys
import os
from collections import defaultdict

ALLOWED_LVLS = {"INFO", "DEBUG", "WARNING", "ERROR"}


def parse_log_line(raw_line):
    clean_line = raw_line.strip()
    parts = clean_line.split(maxsplit=3)
    if len(parts) < 4:
        return None
    date = parts[0]
    time = parts[1]
    level = parts[2].upper()
    msg = parts[3]
    return {"DATE": date, "TIME": time, "LEVEL": level, "DESCRIPTION": msg}


def load_logs(file_path):
    logs = []
    try:
        with open(file_path, "r", encoding="UTF-8") as f:
            for line in f:
                good_logs = parse_log_line(line)
                if good_logs is not None:
                    logs.append(good_logs)
    except PermissionError:
        print("You don't have rights to open this file")
        sys.exit(1)
    return logs


def count_logs_by_level(logs):
    result = defaultdict(int)
    for element in logs:
        level_res = element["LEVEL"]
        result[level_res] += 1

    return result


def filter_logs_by_level(logs, level):
    return [el for el in logs if el["LEVEL"] == level]


def display_log_counts(counts):
    print(f"{'Рівень логування':<20} | {'Кількість':<10}")
    print("-" * 20 + "|" + "-" * 10)
    for level, count in counts.items():
        print(f"{level:<20} | {count:<10}")


def main(file_path, users_lvl):
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    if users_lvl is not None:
        print(f"Деталі логів для рівня {users_lvl}: ")
        filtered = filter_logs_by_level(logs, users_lvl)
        if not filtered:
            print(f"Немає записів рівня {users_lvl}")
        for record in filtered:
            print(record["DATE"], record["TIME"], "-", record["DESCRIPTION"])


users_lvl = None
if len(sys.argv) >= 2:
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print("File not found. Use <file name>")
        sys.exit(1)
else:
    print("Invalid Path. Please, use: python general.py log_file.txt")
    sys.exit(1)
if len(sys.argv) >= 3:
    users_lvl = sys.argv[2].upper()
    if users_lvl not in ALLOWED_LVLS:
        print(f"This {users_lvl} is not authorised and allowed level")
        print(f"List of allowed levels: {ALLOWED_LVLS}")
        sys.exit(1)

if __name__ == "__main__":
    main(file_path, users_lvl)
