from postgresdb.core import validators
from postgresdb.exceptions import ValidationError

class BaseObject(object):
    def __init__(self):
        self.validators = []

class CharField(object):
    def __init(self, min_length, max_length):
        VERIFICATION.verify_list_type(input_detections, ScoredRect, "input_detections")
        # if min_length is not None:
        #     self.validators.append(validators.MinLengthValidator(int(min_length)))
        # if max_length is not None:
        #     self.validators.append(validators.MaxLengthValidator(int(max_length)))
