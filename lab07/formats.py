import json
import re


def csv_to_records(text: str) -> list[dict]:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return []
    header = [h.strip() for h in lines[0].split(",")]
    records = []
    for ln in lines[1:]:
        values = [v.strip() for v in ln.split(",")]
        records.append(dict(zip(header, values)))
    return records


def _scalar(value: str):
    value = value.strip()
    if _unquote(value) is not None:
        return _unquote(value)
    if value in ("true", "yes"):
        return True
    if value in ("false", "no"):
        return False
    if re.fullmatch(r"[0-9]+", value):
        return int(value)
    if re.fullmatch(r"[0-9]+\.[0-9]+", value):
        return float(value)
    return value


def _strip_comment(line):
    q = None
    for i, ch in enumerate(line):
        if q:
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
        elif ch == "#":
            return line[:i]
    return line


def _unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return None


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list = None
    for raw in lines:
        line = _strip_comment(raw).strip()
        if not line:
            continue
        if line.startswith("- ") or line == "-":
            if current_list is not None:
                current_list.append(_scalar(line[1:]))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value == "":
            current_list = []
            result[key] = current_list
        else:
            current_list = None
            result[key] = _scalar(value)
    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    merged = []
    for row in rows:
        info = extra.get(row.get(key), {})
        merged.append({**info, **row})
    return merged


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
