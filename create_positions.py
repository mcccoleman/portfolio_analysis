class Position(object):
    number_of_shares = 0
    last_price = 0
    distribution_yield = 0
    mu = 0

    def __init___(self,number_of_shares,last_price,distribution_yield,mu):
        self.number_of_shares = number_of_shares
        self.last_price = last_price
        self.distribution_yield = distribution_yield
