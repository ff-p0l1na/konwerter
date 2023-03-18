import csv
import json
import pickle
import sys


class CsvHandler:
    def dump(self, inside, file):
        writer = csv.writer(file)
        for line in inside:
            writer.writerow(line)

    def load(self, file):
        inside = []
        reader = csv.reader(file)
        for line in reader:
            inside.append(line)
        return inside


def get_filehandler(filename):
    if filename.endswith('.json'):
        encoding_type = ''
        handler_class = json
        return encoding_type, handler_class
    elif filename.endswith('.pickle'):
        encoding_type = 'b'
        handler_class = pickle
        return encoding_type, handler_class
    elif filename.endswith('.csv') or filename.endswith('.txt'):
        encoding_type = ''
        handler_class = CsvHandler()
        return encoding_type, handler_class
    else:
        raise NotImplementedError("Nieobsługiwane rozszerzenie.")


# Argumenty z command line:
input_file = sys.argv[1]
output_file = sys.argv[2]
change = sys.argv[3:]
# Ustalanie miejsca i treści zmiany:
modifications = []
for n in range(len(change)):
    one_piece = change[n].split(',')
    chosen_column = int(one_piece[0])
    chosen_row = int(one_piece[1])
    content = str(one_piece[2])
    col_idx = int(chosen_column - 1)
    row_idx = int(chosen_row - 1)
    modifications.append([col_idx, row_idx, content])
# Odczyt pliku:
input_encoding_type, input_handler_class = get_filehandler(input_file)
with open(input_file, 'r' + input_encoding_type) as f:
    data = input_handler_class.load(f)
# Modyfikacja pliku:
for element in modifications:
    col_idx, row_idx, content = element
    data[row_idx][col_idx] = content
# Zapis pliku (w nowym formacie):
output_encoding_type, output_handler_class = get_filehandler(output_file)
with open(output_file, 'w' + output_encoding_type) as f:
    output_handler_class.dump(data, f)
# Start:
get_filehandler(input_file)

