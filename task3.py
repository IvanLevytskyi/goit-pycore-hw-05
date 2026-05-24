import sys
from collections import Counter


def parse_log_line(line: str) -> dict:
    # Split log line into components
    parts = line.split(maxsplit=3)

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3].strip()
    }


def load_logs(file_path: str) -> list:
    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                logs.append(parse_log_line(line))

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print(f"Error: {e}")

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    # Filter logs by selected level
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    # Count records for each logging level
    return Counter(log["level"] for log in logs)


def display_log_counts(counts: dict):
    print("Logging level | Count")
    print("--------------|------")

    for level, count in counts.items():
        print(f"{level:<13} | {count}")


def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        print("Please provide path to log file.")
        return

    file_path = sys.argv[1]

    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    # Show logs for selected level
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()

        filtered_logs = filter_logs_by_level(logs, level)

        print(f"\nLog details for level '{level}':")

        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()