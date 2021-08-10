"""Serialization.

@see: https://www.learnpython.org/en/Serialization

Python provides built-in JSON libraries to encode and decode JSON.
"""

import json
import datetime


def test_json1():
    """JSON serialization."""

    person_dictionary = {'first_name': 'John', 'last_name': 'Smith', 'age': 42,
                         "stated_test_at": str(datetime.datetime(2020, 5, 17, 9, 30, 0))}

    json_string = '{"first_name": "John", "last_name": "Smith", "age": 42, "stated_test_at": "2020-05-17 09:30:00"}'

    person_parsed_dictionary = json.loads(json_string)

    assert person_parsed_dictionary == person_dictionary
