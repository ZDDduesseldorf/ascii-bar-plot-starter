from ascii_barchart.io import load_rows


rows = load_rows("data/points.csv")

def average_value1_by_type(rows):
    
    sums = {}
    counts = {}
    
    for row in rows:
        t = row[0]       
        val1 = row[1]   
        
        
        if t not in sums:
            sums[t] = 0
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
    print("Ergebnis:", result)