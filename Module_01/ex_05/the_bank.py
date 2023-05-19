"""The goal is to discover new built-in functions and deepen class understanding"""
import logging
# Starting to use logging module instead of using print like a bonobo
# and having to delete it everytime when the code works.
logging.basicConfig(level=logging.WARNING,
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')


class Account:
    """A bank account"""

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        self.name = name
        Account.ID_COUNT += 1

        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        """Transfer money to the account

        Args:
                amount (int, float): The value to be added to the account
        """
        self.value += amount


class Bank:
    """The big bank"""

    @staticmethod
    def account_is_corrupted(account: Account) -> bool:
        """Check is an Account object is corrupted

        Args:
                account (Account): the account to check

        Returns:
                bool: True if account is corrupted, False otherwise
        """
        try:
            acc_attr = dir(account)
            if len(acc_attr) % 2 == 0:
                raise AttributeError(
                    "Account must have an odd number of attributes")
            if not all(item in acc_attr for item in ['name', 'id', 'value']):
                raise AttributeError(
                    "One of [name, id, value] not found as attribute")
            if not any(item.startswith(('zip', 'addr')) for item in acc_attr):
                raise AttributeError(
                    "Must have an attribute starting with 'zip' or 'addr'")
            if any(item.startswith('b') for item in acc_attr):
                raise AttributeError(
                    "No attribute can start with a 'b' - don't ask why")
            if not isinstance(account.name, str):
                raise TypeError("Account Name must be a string")
            if not isinstance(account.id, int):
                raise TypeError("Account ID must be an int")
            if not isinstance(account.value, (int, float)):
                raise TypeError("Account Value must be an int / float")
            return False
        except (AttributeError, TypeError) as exception:
            logging.debug(f"account_is_corrupted() - {exception}")
            return True

    def __init__(self):
        self.accounts = []

    def add(self, new_account) -> bool:
        """Add Account object to our list of accounts

        Args:
                new_account (Account): the account to be added

        Returns:
                bool: True if account was added, false if the argument passed was not valid
        """
        try:
            if not isinstance(new_account, Account):
                raise TypeError("This is not a valid Account")
            if new_account in self.accounts:
                raise ValueError("Account already exists")
            self.accounts.append(new_account)
            return True
        except (ValueError, TypeError) as exception:
            logging.debug(f"add() - {exception}")
            return False

    def get_account(self, attribute):
        """Gets the desired account from our list of Accounts based on attribute.

        Args:
                attribute (int or str): id or name of the account to get

        Raises:
                AttributeError: If account does not exist or the attribute is not valid

        Returns:
                Desired account if we could get it, False otherwise
        """
        try:
            if isinstance(attribute, int):
                account = [acc for acc in self.accounts if hasattr(acc, "id")]
            elif isinstance(attribute, str):
                account = [
                    acc for acc in self.accounts if hasattr(acc, "name")]
            else:
                raise AttributeError(
                    "Cannot get account without valid ID or Name")
            if not isinstance(account[0], Account):
                raise AttributeError("Account not in the bank")
            return account[0]
        except AttributeError as exception:
            logging.debug(f"get_account() - {exception}")
            return False

    def transfer(self, origin, dest, amount):
        """Transfers funds

        Args:
                origin (str): name of the first account
                dest (str): name of the origin account
                amount (float): amount of money to transfer

        Returns:
                bool: True if success, False is an error occured
        """
        try:
            origin_acc = self.get_account(origin)
            dest_acc = self.get_account(dest)
            if self.account_is_corrupted(origin_acc) or self.account_is_corrupted(dest_acc):
                raise ValueError("Account is corrupted, can't transfer")
            if origin_acc.value < amount or amount < 0:
                raise ValueError("Not enough funds. GIVE ME THE MONEY!")
            origin_acc.transfer(-amount)
            dest_acc.transfer(amount)
            return True
        except ValueError as exception:
            logging.debug(f"transfer() - {exception}")
            return False

    def fix_account(self, name) -> bool:
        """Fix the account if it's corrupted

        Args:
                name (str): name of the account

        Returns:
                bool: True if success, False if an error occured
        """
        try:
            if not isinstance(name, str):
                raise ValueError("Account name must be a string")
            account = self.get_account(name)
            if not isinstance(account, Account):
                raise ValueError("Account does not exist")
            if self.account_is_corrupted(account) is False:
                logging.debug(
                    "fix_account() - Account is not corrupted, nothing to fix")
                return True
            account_attr = dir(account)
            for attr in ['name', 'id', 'value']:
                if not hasattr(account, attr):
                    setattr(account, attr, None)
            if not any(item.startswith(('zip', 'addr')) for item in account_attr):
                setattr(account, 'zip', None)
            b_attr_list = [
                item for item in account_attr if item.startswith('b')]
            for b_attr in b_attr_list:
                delattr(account, b_attr)
            attr_num = len(account_attr)
            if attr_num % 2 == 0:
                setattr(account, 'lol', 'hihi')
            return True
        except ValueError as exception:
            logging.debug(f"fix_account() - {exception}")
            return False
