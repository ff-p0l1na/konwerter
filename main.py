import csv
import json
import pickle
import sys


class CsvHandler:
    def dump(self, data, file):
        writer = csv.writer(file)
        for line in data:
            writer.writerow(line)


    def load(self, file):
        data = []
        reader = csv.reader(file)
        for line in reader:
            data.append(line)
        return data


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


input_file = sys. argv[1]
output_file = sys.argv[2]
#
input_encoding_type, input_handler_class = get_filehandler(input_file)
with open(input_file, 'r' + input_encoding_type) as f:
    data = input_handler_class.load(f)
#
output_encoding_type, output_handler_class = get_filehandler(output_file)
with open(output_file, 'w' + output_encoding_type) as f:
    output_handler_class.dump(data, f)

get_filehandler(input_file)
