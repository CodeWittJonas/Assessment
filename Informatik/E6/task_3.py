def transfer_from_to(accs, account_from, account_to, value):
    """
    Transfers money from one account to another, given that both accounts exist and there is enough money in the sender's account.

    :param accs: A dictionary containing all accounts and their balance
    :param account_from: A string specifying the sender's account
    :param account_to: A string specifying the receiver's account
    :param value: The amount that should be transferred
    :return: A new, updated accounts dictionary (The account dictionary should not be modified directly, instead a copy should be created, modified and returned.
    """

    accounts = dict(accs)

    if account_from in accounts and account_to in accounts:
        if 0 < value <= accounts[account_from]:
            accounts[account_from] -= value
            accounts[account_to] += value

    return accounts


def create_account(accs, name, initial_balance):
    """
    Creates a new account with the given name and initial balance. If an account with the given name already exists, the new account is not created.

    :param accs: A dictionary containing all accounts and their balance
    :param name: The name of the new account to create (must be a non-empty string)
    :param initial_balance: The initial balance of the account (must be non-negative)
    :return: A new, updated accounts dictionary (The account dictionary should not be modified directly, instead a copy should be created, modified and returned.
    """
    accounts = dict(accs)

    if name and name not in accounts and initial_balance >= 0:
        accounts[name] = initial_balance

    return accounts


if __name__ == '__main__':
    accs = {}
    accs = create_account(accs, 'Person 1', 0)

    print(accs)

    accs = create_account(accs, 'Person 2', 100)

    print(accs)

    accs = transfer_from_to(accs, 'Person 2', 'Person 2', 10)
    print(accs)
