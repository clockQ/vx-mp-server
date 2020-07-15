from mt_util.csv import load_lstdic_from_csv


def test_load_users_by_csv():
    result = load_lstdic_from_csv('users.csv')
    assert len(result) != 0
