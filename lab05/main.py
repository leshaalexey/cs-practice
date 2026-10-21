from pathlib import Path

from logstats import count_levels, top_errors, format_report

base = Path(__file__).parent
name = input().strip()
path = base / name

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)
with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

print(sum(counts.values()))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

with open(base / "report.txt", "w", encoding="utf-8", newline="\n") as out:
    out.write(format_report(counts, errors))