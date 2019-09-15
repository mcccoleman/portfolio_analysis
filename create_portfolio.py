from create_positions import create_position
from pprint import pprint


class Portfolio(object):
    positions = []


    def __init__(self,positions):
        self.positions = positions

    def loop_through_each_position(self):
        for position in self.positions:
            print(position)

def create_portfolio(positions):
    return Portfolio(positions)


portfolio = create_portfolio([create_position('spy',0.05,100),create_position('spy',0.05,100)])
portfolio.loop_through_each_position()
# pprint(vars(portfolio))
