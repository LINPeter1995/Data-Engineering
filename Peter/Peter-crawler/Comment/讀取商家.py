import csv

def 讀取商家清單(csv_path):
    result = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append((row['name'], row['url']))
    return result


