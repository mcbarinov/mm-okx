from mm_okx.api.account import get_timestamp


def test_get_timestamp():
    res = get_timestamp()
    assert res.endswith("Z")
