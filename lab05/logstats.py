from collections import Counter

LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3 or parts[1] not in LEVELS:
        raise ValueError(f"bad line: {line!r}")
    return {"time": parts[0], "level": parts[1], "message": parts[2]}


def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n):
    c = Counter()
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            c[event["message"]] += 1
    ranked = sorted(c.items(), key=lambda p: (-p[1], p[0]))
    return [[msg, cnt] for msg, cnt in ranked[:n]]


def format_report(counts, errors):
    text = "Отчёт по журналу\n\n"
    for level in sorted(counts):
        text += f"{level}: {counts[level]}\n"
    text += "\nЧастые ошибки:\n"
    for msg, cnt in errors:
        text += f"- {msg} — {cnt}\n"
    return text