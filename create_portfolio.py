class Portfolio(object):
    positions = []


    def __init___(self,positions):
        self.positions = positions

def create_portfolio(positions):
    portfolio = Portfolio(positions)
    return portfolio