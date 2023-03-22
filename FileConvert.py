import json
import csv

print('hello world')


# Open the JSON file and read the data
with open(r'C:\Users\heber\AMProject\bq-results-20230321-203706-1679431190091.json', 'rb') as json_file:
    data = json.load(json_file)

# Open the CSV file and write the data
with open(r'C:\Users\heber\AMProject\apdata.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(data[0].keys())
    
    # Write the data rows
    for item in data:
        writer.writerow(item.values())