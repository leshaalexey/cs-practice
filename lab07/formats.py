import ast
import json


def csv_to_records(text: str) -> list[dict]:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return []
    header = [h.strip() for h in lines[0].split(",")]
    return [dict(zip(header, [v.strip() for v in ln.split(",")])) for ln in lines[1:]]


def _scalar(value: str):
    value = value.strip()
    if value in ("true", "yes"):
        return True
    if value in ("false", "no"):
        return False
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current = None
    for raw in lines:
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("-"):
            if current is not None:
                current.append(_scalar(line[1:]))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value == "":
            current = []
            result[key] = current
        else:
            current = None
            result[key] = _scalar(value)
    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    return [{**extra.get(row.get(key), {}), **row} for row in rows]


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)