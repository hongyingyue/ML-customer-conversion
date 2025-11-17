import csv
import re
from itertools import islice
import json

csv_file_path = 'data/raw/customer_conversion_testing_dataset.csv'
json_file_path = 'demo_row.json'

rid = int(input("Lead ID for demo (1 - 26,145): "))

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # demo_row = next(reader)
    demo_row = next(islice(reader, rid-1, rid))

    cleaned_row = {"data":{}}
    for key, value in demo_row.items():
        # Normalize key
        new_key = key.lower().replace(' ', '_')
        new_key = re.sub(r'[()]', '', new_key)
        # Normalize value
        new_value = str(value).lower().replace(' ', '_')
        if new_key in ["leadid", "conversion_target"]:
            cleaned_row[new_key] = new_value
        else:
            cleaned_row["data"][new_key] = new_value
        # print(f"{new_key}: {new_value}")
        
# Save as JSON
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(cleaned_row, jsonfile, ensure_ascii=False, indent=4)

print(f"\nCleaned row saved to {json_file_path}")
