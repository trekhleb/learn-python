"""Serialization.

@see: https://www.learnpython.org/en/Serialization

Python provides built-in JSON libraries to encode and decode JSON.
"""

import json


def test_json():
    """JSON serialization."""

    person_dictionary = {'name': 'Fareed', 'Company': 'Arbisoft', 'age': 22}
    assert person_dictionary['name'] == 'Fareed'

    json_string = '{"name": "Fareed", "Company": "Arbisoft", "age": 22}'

    # To load JSON back to a data structure, use the "loads" method. This method takes a string
    # and turns it back into the json object data-structure:
    person_parsed_dictionary = json.loads(json_string)

    assert person_parsed_dictionary == person_dictionary
    assert person_parsed_dictionary['name'] == 'Fareed'
    assert person_parsed_dictionary['age'] == 22

    # To encode a data structure to JSON, use the "dumps" method. This method takes an object and
    # returns a String:
    encoded_person_string = json.dumps(person_dictionary)

    assert encoded_person_string == json_string

    assert person_dictionary == json.loads(encoded_person_string)
