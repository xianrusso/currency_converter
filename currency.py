import requests

class Currency:

    def __init__(self, base, amount, target):
        self.base = base
        self.amount = float(amount)
        self.target = target

    def convert(self):
        if len(self.base) != 3:
            raise NameError("Please enter the base currency's abbreviation.  (i.e. 'USD' for 'United States Dollar')")

        if len(self.target) != 3:
            raise NameError("Please enter the target currency's abbreviation.  (i.e. 'USD' for 'United States Dollar')")

        url = 'https://api.fixer.io/latest?base='+self.base+'&symbols='+self.target
        r = requests.get(url)
        rd = r.json()
        rate = rd['rates'][self.target]

        def conversion(amount, rate):
            return self.amount * rate

        return conversion(self.amount, rate)
