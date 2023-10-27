import csv

condition_synonyms = set()
condition_synonyms_with_plurals = set()

with open("Data/mondo_and_hp_all_synonyms.csv", encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        condition_synonyms.add(line[3].lower())
        condition_synonyms_with_plurals.add(line[3].lower())
        condition_synonyms_with_plurals.add(line[3].lower() + 's')

condition_strings = set()
with open("Data/clinical_trial_condition_string_counts.csv", encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        condition_strings.add(row[1])
#        if(row[1] not in condition_synonyms):writer.writerow(row)

print("The number of unique condition strings in all clinical trials is:", len(condition_strings))

print("The number of mappable conditions is:", len(condition_strings.intersection(condition_synonyms)))
print("The number of unmappable conditions is:", len(condition_strings.difference(condition_synonyms)))

print("The number of mappable conditions is (with simple plurals):", len(condition_strings.intersection(condition_synonyms_with_plurals)))
print("The number of unmappable conditions is (with simple plurals):", len(condition_strings.difference(condition_synonyms_with_plurals)))