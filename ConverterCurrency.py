import json

with open("Currencies.json") as file:
    data = json.load(file)


class ConverterCurrency:
    currencies = list()
    for value in data:
        currencies.append(value)

    @staticmethod
    def converter(fr, to, value):
        money = value / data[fr] * data[to]
        return money
