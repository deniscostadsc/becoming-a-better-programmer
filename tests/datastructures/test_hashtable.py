from datastructures import Hashtable


def test_hashtable_is_initially_empty():
    hashtable = Hashtable()
    assert len(hashtable) == 0
