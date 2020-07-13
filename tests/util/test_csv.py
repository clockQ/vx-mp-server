from mt_util.csv import load_users_by_csv


def test_load_users_by_csv():
    result = load_users_by_csv('users.csv')
    assert len(result) != 0
