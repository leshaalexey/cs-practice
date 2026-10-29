import json

def csv_to_records(text):
    """
    CSV с заголовком → список словарей; значения остаются строками.
    """
    if not text or not text.strip():
        return []

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    header = [col.strip() for col in lines[0].split(',')]

    records = []
    for line in lines[1:]:
        values = [val.strip() for val in line.split(',')]
        # Защита от строк короче заголовка
        while len(values) < len(header):
            values.append("")

        row = {}
        for i in range(len(header)):
            row[header[i]] = values[i]
        records.append(row)

    return records


def _parse_value(raw):
    raw = raw.strip()
    if raw.lower() in ("true", "yes"):
        return True
    if raw.lower() in ("false", "no"):
        return False

    try:
        if '.' in raw:
            return float(raw)
        return int(raw)
    except ValueError:
        pass

    return raw


def parse_settings(lines):
    """
    Простой YAML → словарь.
    """
    result = {}
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not line or line.startswith('#'):
            i += 1
            continue

        # Обработка списка: ключ:
        if line.endswith(':') and not line.rstrip().endswith('-'):
            key = line[:-1].strip()
            lst = []
            i += 1
            while i < len(lines) and lines[i].lstrip().startswith('-'):
                item_line = lines[i].lstrip()[1:].strip()
                if '#' in item_line:
                    item_line = item_line[:item_line.index('#')].strip()
                lst.append(_parse_value(item_line))
                i += 1
            result[key] = lst
            continue

        # Обычная пара ключ: значение
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value_part = parts[1].strip() if len(parts) > 1 else ""

            if '#' in value_part:
                value_part = value_part[:value_part.index('#')].strip()

            if value_part == '':
                result[key] = ""
            else:
                result[key] = _parse_value(value_part)

        i += 1

    return result


def merge_by_key(rows, extra, key="id"):
    merged = []
    for row in rows:
        new_row = dict(row)  # копия
        lookup_key = row.get(key)

        if lookup_key in extra:
            extra_info = extra[lookup_key]
            for k, v in extra_info.items():
                if k not in new_row:
                    new_row[k]
