
import csv

with open('item_ids_names.txt') as textfile:
    csvReader = csv.reader(textfile, delimiter=',')
    for row in csvReader:
        row = [col.strip() for col in row]
        with open('output.txt', 'a') as output:
            output.write("Item.objects.create(item_id='" + row[0] + "'," + "name='" + row[1] + "')\n")
        