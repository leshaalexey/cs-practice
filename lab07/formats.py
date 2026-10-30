import json


def csv_to_records(text: str) -> list[dict]:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return []
    header = [h.strip() for h in lines[0].split(",")]
    return [dict(zip(header, [v.strip() for v in ln.split(",")])) for ln in lines[1:]]


def _scalar(value: str):
    if value.startswith("[") and value.endswith("]"):
        return [_scalar(v.strip()) for v in value[1:-1].split(",") if v.strip()]
    if value in ("", "~", "null"):
        return None
    if value.lower() in ("true", "yes", "on"):
        return True
    if value.lower() in ("false", "no", "off"):
        return False
    for conv in (int, float):
        try:
            return conv(value)
        except ValueError:
            pass
    return value


def _strip_comment(line: str) -> str:
    for i, ch in enumerate(line):
        if ch == "#" and (i == 0 or line[i - 1] in " \t"):
            return line[:i]
    return line


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current = None
    for raw in lines:
        line = _strip_comment(raw).strip()
        if not line:
            continue
        if line.startswith("-"):
            if current is not None:
                if result[current] is None:
                    result[current] = []
                result[current].append(_scalar(line[1:].strip()))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        result[key] = _scalar(value)
        if value == "":
            current = key
    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    return [{**extra.get(row.get(key), {}), **row} for row in rows]


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)