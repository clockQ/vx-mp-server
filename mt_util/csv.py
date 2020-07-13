import csv


def load_users_by_csv(file_path):
    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        final_list = list(csvreader)

        keys = final_list[0]
        result = []
        for values in final_list[1:]:
            row = {}
            for (i, v) in enumerate(values):
                row[keys[i]] = v
            result.append(row)

    return result
