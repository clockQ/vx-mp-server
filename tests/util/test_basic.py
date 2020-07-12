from mt_util.basic import Basic


def test_get_access_token():
    access_token = Basic().get_access_token()
    assert access_token != "success"
