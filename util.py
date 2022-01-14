from datetime import datetime
import json


def type_converter(obj):
    if isinstance(obj, datetime):
        return obj.__str__()


def print_json(json_obj):
    print('{}'.format(json.dumps(json_obj, indent=2, sort_keys=False, default=type_converter)))

