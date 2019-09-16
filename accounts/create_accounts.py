class accounts(object):
    positions = []

    def __init__(self,positions,dividend_and_interest_taxable):
        self.positions = positions
        self.dividend_and_interest_taxable = dividend_and_interest_taxable