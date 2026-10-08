def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("неверное количество полей")

    city = parts[0].strip()
    temp_str = parts[1].strip().replace(",", ".")
    date = parts[2].strip()

    if not city or not date:
        raise ValueError("пустой город или дата")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("температура не является числом")

    return {"city": city, "temperature": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    valid = []
    for line in lines:
        if not line.strip():
            continue
        try:
            valid.append(parse_record(line)) # если в принципе какое-то из условий не выполнется и расчитать не выходит
        except ValueError:
            pass
    return valid

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for r in records:
        c = r["city"]
        totals[c] = totals.get(c, 0.0) + r["temperature"]
        counts[c] = counts.get(c, 0) + 1

    return {c: round(totals[c] / counts[c], 1) for c in totals}

def warmest_city(records: list[dict]) -> str:
    if not records:
        return ''
    avgs = average_by_city(records)
    sorted_cities = sorted(avgs.keys(), key=lambda c: (-avgs[c], c))
    return sorted_cities[0]