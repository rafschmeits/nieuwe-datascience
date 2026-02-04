import csv


file_path = r"C:/xampp/mysql/data/climate_watch/GlobalLandTemperaturesByCountry.csv"

with open(file_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)


print(data[0:5])

for row in data:
    row[-1] = row[-1].replace("Bonaire, Saint", "Bonaire Saint")

print(data[69710:69720])


output_path = r"C:/xampp/mysql/data/climate_watch/GlobalLandTemperaturesByCountry_cleaned.csv"

with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
 
    writer.writerows(data)