import csv

condition_synonyms = set()

with open("Data/mondo_and_hp_all_synonyms.csv", encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        condition_synonyms.add(line[3].lower())

with open("Data/clinical_trial_condition_string_counts.csv", encoding='utf-8', newline='') as f, open("Data/clinical_trial_condition_string_counts_unmappable.csv", 'w', encoding='utf-8', newline='') as f2:
    reader = csv.reader(f)
    writer = csv.writer(f2)
    writer.writerow(next(reader))
    for row in reader:
        if(row[1] not in condition_synonyms):writer.writerow(row)


