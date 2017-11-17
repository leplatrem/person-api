import json


class AuthZero(object):
    def __init__(self, dynamodb_json):
        self.dynamodb_json = dynamodb_json

    @property
    def to_userinfo(self):
        # XXX TBD to userinfo compat method if needed.
        pass
