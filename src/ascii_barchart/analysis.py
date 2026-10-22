def average_value1_by_type(rows):
    totals = {}
    counts = {}

    for category, value1, _value2 in rows:
        totals[category] = totals.get(category, 0) + value1
        counts[category] = counts.get(category, 0) + 1

    return [
        (category, totals[category] / counts[category]) for category in sorted(totals)
    ]
