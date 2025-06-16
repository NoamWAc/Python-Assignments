import re
from datetime import datetime, timedelta
from collections import defaultdict

def parse_timelog(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    days = []
    current_day = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current_day:
                days.append(current_day)
                current_day = []
        else:
            current_day.append(stripped)
            if stripped.endswith("End"):
                days.append(current_day)
                current_day = []

    if current_day:
        days.append(current_day)

    return days

def process_day(entries):
    parsed = []
    for line in entries:
        time_str, label = line.split(" ", 1)
        time_obj = datetime.strptime(time_str, "%H:%M")
        parsed.append((time_obj, label))

    blocks = []
    for i in range(len(parsed) - 1):
        start_time, label = parsed[i]
        end_time = parsed[i + 1][0]
        blocks.append((start_time, end_time, label))

    return blocks

def format_time_range(start, end):
    return f"{start.strftime('%H:%M')}-{end.strftime('%H:%M')}"

# This function generates a report from the parsed time log entries. It's commented out because it's an all-in-one function and not meant for modular use.
# def generate_report(input_file, output_file):
#     all_days = parse_timelog(input_file)
#     total_duration = timedelta()
#     durations_by_label = defaultdict(timedelta)

#     with open(output_file, 'w', encoding='utf-8') as out:
#         for day in all_days:
#             blocks = process_day(day)
#             for start, end, label in blocks:
#                 duration = end - start
#                 durations_by_label[label] += duration
#                 total_duration += duration
#                 out.write(f"{format_time_range(start, end)} {label}\n")
#             out.write("\n")  # Blank line between days

#         # Summary
#         out.write("\n")
#         for label, duration in sorted(durations_by_label.items(), key=lambda x: x[0].lower()):
#             minutes = int(duration.total_seconds() // 60)
#             percent = round(100 * duration / total_duration)
#             out.write(f"{label:<25}{minutes:>4} minutes   {percent:>2}%\n")
def summarize_blocks(blocks):
    from collections import defaultdict
    durations_by_label = defaultdict(timedelta)
    total_duration = timedelta()

    for start, end, label in blocks:
        duration = end - start
        durations_by_label[label] += duration
        total_duration += duration

    summary_lines = []
    for label, duration in sorted(durations_by_label.items(), key=lambda x: x[0].lower()):
        minutes = int(duration.total_seconds() // 60)
        percent = round(100 * duration / total_duration) if total_duration.total_seconds() else 0
        summary_lines.append(f"{label:<25}{minutes:>4} minutes   {percent:>2}%")
    
    return summary_lines

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python call_log_parser.py input_file output_file")
        sys.exit(1)

    generate_report(sys.argv[1], sys.argv[2])
