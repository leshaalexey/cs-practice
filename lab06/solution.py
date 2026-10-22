
from collections import Counter

def count_by_extension(paths: list[str]) -> dict[str, int]:
    exts = []
    for p in paths:
        name = p.split('/')[-1]
        ext = name.rsplit('.', 1)[-1].lower() if '.' in name else ""
        exts.append(ext)
    return dict(Counter(exts))
