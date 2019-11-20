#!/usr/bin/python
import sys
import csv
import os
from datetime import datetime
from dateutil.parser import parse
from decimal import Decimal, ROUND_UP

def main(input_file, output_file):
    results = []
    sums = {}
    avg = {}

    with open(input_file) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        header = csv_reader.pop(0)
        for row in csv_reader:
            new_row = dict(zip(header, row))
            new_row['Date'] = parse(new_row['Date'])
            sum_key = "{},{},{}".format(
                new_row["Border"], new_row["Date"].month, new_row["Measure"])
            sums[sum_key] = sums.get(sum_key, 0) + int(new_row["Value"])
            results.append(new_row)
        

    for key in sums.keys():
        [border, month, measure] = key.split(",")
        denominator = int(month) -1
        if denominator == 0:
            avg[key] = 0
        else:
            avg[key] = Decimal(sum([sums.get("{},{},{}".format(border, m, measure),0)
                                  for m in range(1, int(month))]) / denominator).quantize(0, ROUND_UP)

                                  
    with open(output_file, mode='w') as results_csv:
        results_csv.writelines("Border,Date,Measure,Value,Average\n")
        for key in sums.keys():
            [border, month, measure] = key.split(",")
            formated_date = datetime(
                2019, int(month), 1, 0, 0).strftime("%m/%d/%Y %I:%M:%S %p")
            results_csv.writelines(
                ",".join([border, formated_date, measure, str(sums[key]), str(avg[key])]) + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("To run the progrm you need the input and the output as args\n example: python src/border_analytics.py path/input path/output")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
