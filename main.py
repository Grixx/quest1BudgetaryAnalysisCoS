# Quest 1 Final Challenge
#

import csv

class SeattleCSVParser:

    def parse_csv(self, file_path):
        department_list = {}

        with open(file_path, "r") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")

            next(csv_reader)  # Skip Header Row

            for row in csv_reader:  # Parse the csv.
                if not row[0]:  # If Department column is blank, skip the row.
                    continue
                # Department column is populated but NOT in dict AND 2012 Actual = ' '; add to dict as {'department': 0}
                elif not row[3] and row[0] not in department_list.keys():
                    department_list[row[0]] = 0
                # Department column is populated AND IN dict AND 2012 Actual = ' '; continue
                elif not row[3] and row[0] in department_list.keys():
                    continue
                # Department is in dictionary keys; sum the existing value with current row value from csv
                elif row[0] in department_list.keys():
                    department_list[row[0]] = float(department_list[row[0]]) + float(row[3])
                else:  # Department is NOT in dict and 2012 Actual is not blank; add to the dictionary
                    department_list[row[0]] = float(row[3])

        return department_list


test = SeattleCSVParser()
test = test.parse_csv("city-of-seattle-2012-expenditures-dollars.csv")

for k, v in test.items():
    print(k + "\t" + '${:,.2f}'.format(v))
