import os

import csv
import itertools
import re

with open('../data/lovecraft_csv/lovecraft_corpus.csv', 'w') as out_file:
    for file in os.listdir('../data/lovecraft'):
        # with open('../data/lovecraft_csv/' + file.split('.')[0] + '.csv', 'w') as out_file:
        with open('../data/lovecraft/' + file, 'r') as in_file:
            writer = csv.writer(out_file, delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE)
            for line in in_file:
                if line != "":
                    split = re.findall(r"[\w']+|[.,!?;]", line)
                    for char in split:
                        writer.writerow([char])
#
# line = 'this. is a test, of things'
# print(line.split())
# print(re.findall(r"[\w']+|[.,!?;]", line))
