from create_positions import create_position
from pprint import pprint


class Portfolio(object):
    positions = []


    def __init__(self,positions):
        self.positions = positions



        # calculate portfolio standard deviation as part of object initiation

    def loop_through_each_position(self):
        counter = 1
        for position in self.positions:
            print('Position Number {counter}'.format(counter=counter))
            counter+=1
            position.print_position_attributes()

    def initial_portfolio_value(self):
        current_value = 0
        for position in self.positions:
            current_value += ( position.number_of_shares * position.initial_price)

def create_portfolio(positions):
    return Portfolio(positions)


portfolio = create_portfolio([create_position('spy',0.05,100),create_position('spy',0.05,100)])
portfolio.loop_through_each_position()
# pprint(vars(portfolio))
