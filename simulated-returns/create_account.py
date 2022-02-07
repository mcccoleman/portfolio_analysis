class Account(object):
    positions = []

    def __init__(self,title,account_type,positions):
        self.title = title
        self.positions = positions
        self.account_type = account_type

def create_account(title,account_type,positions):
    return Account(title,account_type,positions)
