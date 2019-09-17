class Account(object):
    positions = []

    def __init__(self,positions):
        self.positions = positions

def create_account(positions):
    return Account(positions)
