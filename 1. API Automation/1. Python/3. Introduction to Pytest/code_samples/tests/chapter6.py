# fixtures
import pytest

from chapter5_classes.bucket import StringBucket


@pytest.fixture
def string_bucket(scope="session"):
    yield StringBucket()
    # do something


def test_string_bucket_init(string_bucket):
    assert string_bucket.content == ''


def test_string_bucket_insert_space(string_bucket):
    string_bucket.insert(' ')
    assert string_bucket.content == " "


def test_string_bucket_cannot_insert_content_directly(string_bucket):
    with pytest.raises(AttributeError, match=r"property 'content' of 'StringBucket' object has no setter") as e:
        string_bucket.content = ""
