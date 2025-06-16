import sys
import parse_hours_log_file

def main():
    if len(sys.argv) < 2:
        exit("Usage: python call_log_parser.py <log_file_path>")
    
    log_file = sys.argv[1] # Input file containing the hours log
    if not log_file.endswith('.log'):
        exit("Error: The log file must have a '.log' extension.")
    if len(sys.argv) == 3:
        report_file = sys.argv[2]
        if not report_file.endswith('.report'):
            print("Please note: the output file doesn't end with \'.report\'")
    else:
        report_file = log_file.removesuffix(".log") + ".report" # Output file for the report

    all_entries = parse_hours_log_file.parse_timelog(log_file) # Parse the log file into entries

    total_blocks = [] # To store all time blocks for summary

    with open(report_file, 'w', encoding='utf-8') as out: 
        for entry in all_entries: # Iterate through each entry in the log file
            if entry == "__BLANK__":
                out.write('\n')
                continue

            processed = parse_hours_log_file.process_day(entry) # Process each day's entries into time blocks
            total_blocks.extend(processed) # Add to total blocks for summary

            for start, end, label in processed: # Iterate through each time block
                time_range = parse_hours_log_file.format_time_range(start, end)
                out.write(f"{time_range} {label}\n")

            out.write("\n")  # After each day's block

        # Summary
        summary_lines = parse_hours_log_file.summarize_blocks(total_blocks)
        out.write('\n'.join(summary_lines))

    print(f"Report generated: {report_file}")

if __name__ == '__main__':
    main()
