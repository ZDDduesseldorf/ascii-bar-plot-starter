def average_value1_by_type(rows):
    sums = {}
    counts = {}

    for type_name, value1, _value2 in rows:
        sums[type_name] = sums.get(type_name, 0) + value1
        counts[type_name] = counts.get(type_name, 0) + 1

    return [
        (type_name, sums[type_name] / counts[type_name])
        for type_name in ("A", "B", "C", "D")
    ]