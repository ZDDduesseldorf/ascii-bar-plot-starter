from .io import load_rows

def average_value1_by_type(rows):
    sums = {}
    counts = {}

    for row in rows:
        t = row[0]      # type (e.g., A, B, C, D)[cite: 8]
        val1 = row[1]   # value1[cite: 8]
        
        if t not in sums:
            sums[t] = 0.0
            counts[t] = 0
        
        sums[t] += val1
        counts[t] += 1

    averages = []
    for t in sums:
        avg = sums[t] / counts[t]
        averages.append((t, round(avg, 2)))

    averages.sort()
    return averages

if __name__ == "__main__":
    rows = load_rows("data/points.csv")
    result = average_value1_by_type(rows)
    
    # This prints them cleanly one by one (e.g., A 2.16)
    for category, avg in result:
        print(f"{category} {avg}")