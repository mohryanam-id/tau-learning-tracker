# testing classes

import pytest

from chapter5_classes.bucket import StringBucket


def test_string_bucket_init():
    string_bucket = StringBucket()
    assert string_bucket.content == ""


def test_string_bucket_insert_space():
    string_bucket = StringBucket()
    string_bucket.insert(' ')
    assert string_bucket.content == " "


def test_string_bucket_cannot_insert_content_directly():
    string_bucket = StringBucket()
    with pytest.raises(AttributeError, match=r"property 'content' of 'StringBucket' object has no setter") as e:
        string_bucket.content = ""
