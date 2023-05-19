import pytest
from Module_01.ex_05.the_bank import Bank
from Module_01.ex_05.the_bank import Account

VALID = Account(
    'Smith Jane',
    zip='911-745',
    value=1000.0,
)

EVEN_ATTR = Account(
    'William John',
    zip='100-064',
    value=6460.0,
    ref='58ba2b9954cd278eda8a84147ca73c87',
)


@pytest.mark.parametrize("account, expected", [
    (VALID, True),
    (EVEN_ATTR, True),
    ("not an account", False),
])
def test_add(account, expected):
    bank = Bank()
    result = bank.add(account)
    assert result == expected
    if result is True:
        result = bank.add(account)
        assert result is False


@pytest.mark.parametrize("account, expected", [
    (VALID, False),
    (EVEN_ATTR, True),
])
def test_is_corrupt(account, expected):
    bank = Bank()
    result = bank.account_is_corrupted(account)
    assert result == expected


def test_transfer_fix():
    bank = Bank()
    john = Account(
        'John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    )
    jane = Account(
        'Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )
    bank.add(john)
    bank.add(jane)
    assert bank.transfer("Jane", "John", 500) is True
    assert bank.transfer("Jane", "John", 200000) is False
    assert bank.fix_account("John") is True
    assert bank.fix_account("Jane") is True
    assert bank.fix_account(12) is False
