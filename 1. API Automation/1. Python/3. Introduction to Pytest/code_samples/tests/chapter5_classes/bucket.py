# Testing Classes
class StringBucket:
    def __init__(self):
        self._content = ''

    @property
    def content(self):
        return self._content

    def insert(self, new_entry=''):
        self._content += new_entry
