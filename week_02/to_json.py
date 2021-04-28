import json
from functools import wraps

def to_json(func):
    @wraps(func)

    def wrapped(**kwargs):
        return json.dumps(func(**kwargs))

    return wrapped



@to_json
def get_data():
    return {
        'data': 42
    }

print(get_data())  # вернёт '{"data": 42}'


