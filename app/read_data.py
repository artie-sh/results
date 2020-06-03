# encoding: utf-8

class DataReader:
    results = None
    results_table = []

    def __init__(self):
        self.results = open("../results.csv", 'r').read().splitlines()

        for line in self.results:
            self.results_table.append(line.split(";"))

        self.results_table[0].append("Итого")

        for line in self.results_table[1:]:
            sum = 0
            for result in line[1:]:
                sum += int(result)
            line.append(sum)

    def get_data(self):
        return self.results_table