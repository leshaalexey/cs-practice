
from collections import Counter

def count_by_extension(paths: list[str]) -> dict[str, int]:
    exts = []
    for p in paths:
        name = p.split('/')[-1]
        ext = name.rsplit('.', 1)[-1].lower() if '.' in name else ""
        exts.append(ext)
    return dict(Counter(exts))

def deepest_path(paths: list[str]) -> str:
    if not paths: return ""
    max_depth = max(p.count('/') for p in paths)
    return min(p for p in paths if p.count('/') == max_depth)

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    val, i = float(n_bytes), 0
    while val >= 1024 and i < len(units) - 1:
        val /= 1024
        i += 1
    return f"{int(val)} {units[i]}" if i == 0 else f"{val:.1f} {units[i]}"
