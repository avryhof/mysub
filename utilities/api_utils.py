import json
from collections import OrderedDict
from urllib.parse import quote

import bleach

from utilities.helpers import convert_keys


def clean_api_dict(input_value):
    if isinstance(input_value, OrderedDict):
        input_value = to_dict(input_value)

    return convert_keys(clean_api_results(input_value))


def clean_api_results(api_result, **kwargs):
    """
    This function will accept, a list, dictionary, or string.
    If a list or dictionary is provided, it will recursively traverse through it, and run bleach on all string values.
    If a string is provided, it will bleach that string.
    Any other data type is simply returned as-is.

    :param input_dict:
    :return:
    """
    retn = None

    if isinstance(api_result, str):

        retn = bleach.clean(api_result)

    elif isinstance(api_result, dict):
        retn = {}

        for k, v in api_result.items():

            if isinstance(v, str):
                retn[k] = bleach.clean(v)

            else:
                retn[k] = clean_api_results(v)

    elif isinstance(api_result, list):
        retn = []

        for list_item in api_result:
            if isinstance(list_item, str):

                retn.append(bleach.clean(list_item))

            elif isinstance(list_item, dict) or isinstance(list_item, list):

                retn.append(clean_api_results(list_item))

            else:
                retn.append(list_item)

    else:
        retn = api_result

    return retn


def strip_dict(value):
    if isinstance(value, dict):
        new_value = dict()
        for k, v in value.items():
            new_key = k.strip()
            if isinstance(v, str):
                new_val = v.strip()
                new_value[new_key] = new_val
            else:
                new_value[new_key] = v
        return new_value
    return value


def filter_query_characters(value):
    # Convert to a string, and filter anything that has no business being in a URL

    return quote(str(value))


def http_build_query(query_dict):
    """
    Build HTTP Query parameters without urlencoding them further.
    :param query_dict:
    :return:
    """
    query_vals = []
    for key, val in query_dict.items():
        query_vals.append("%s=%s" % (filter_query_characters(key), filter_query_characters(val)))

    return "&".join(query_vals)


def to_dict(input_ordered_dict):
    return json.loads(json.dumps(input_ordered_dict))
