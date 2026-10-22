from collections import Counter

def count_by_extension(paths: list[str]) -> dict[str, int]:
    extensions = []
    for path in paths:
        filename = path.split('/')[-1]
        last_dot = filename.rfind('.')
        if last_dot == -1:
            ext = ""
        elif last_dot == len(filename) - 1:
            ext = ""
        else:
            ext = filename[last_dot + 1:].lower()
        extensions.append(ext)
    return dict(Counter(extensions))

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    max_depth = max(p.count('/') for p in paths)
    candidates = [p for p in paths if p.count('/') == max_depth]
    return min(candidates)

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    unit_idx = 0
    while size >= 1024 and unit_idx < len(units) - 1:
        size /= 1024
        unit_idx += 1
    if unit_idx == 0:
        return f"{int(size)} {units[unit_idx]}"
    else:
        return f"{size:.1f} {units[unit_idx]}"
