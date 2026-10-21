# averages = average_value1_by_type(rows)
sums = {}
counts = {}

def average_value1_by_type(data_list):
    for item_type, val1, val2 in data_list:
        sums[item_type] = sums.get(item_type, 0.0) + val1
        counts[item_type] = sums.get(item_type, 0) + 1
    return [((i, (sums[i] / counts[i])) for i in sorted(sums.keys()))]