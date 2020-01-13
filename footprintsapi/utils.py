"""Collection of common functions and other objects used throughout the program."""

import re
from collections import defaultdict
from typing import Any, Iterable, List, Optional, Tuple, Union


def check_attributes(
    attrs_to_check: list = None, data: dict = None, msg: Optional[str] = None
) -> Union[bool]:
    """Check to see if attributes specified in a list are contained within a dict.

    :param attrs_to_check: List of attributes or keys to check the dict

    :param data: The dict to check against for keys
    """
    if not isinstance(attrs_to_check, list):
        raise TypeError("Invalid data type, must use a list.")

    if not isinstance(data, dict):
        raise TypeError("Invalid data type, must use a dict.")

    if all(key in data for key in attrs_to_check):
        return True

    return False


def cleanup_args(
    args_dict: dict, items_to_remove: list = ["self", "kwargs", "params"]
) -> dict:
    """Iterate through dict and remove items."""
    if not args_dict:
        raise AttributeError("No arguments recieved.")
    if not isinstance(args_dict, dict):
        raise TypeError("Args must be passed as a dict.")

    return {
        k: v
        for k, v in _unpack(args_dict)
        if v is not None and k not in items_to_remove
    }


def _unpack(data: Any) -> Any:
    """Unpack a dict."""
    if isinstance(data, dict):
        return data.items()
    return data


def _copy_dict(data: dict) -> dict:
    """Copy a a dict."""
    return data.copy()


def to_dict(obj: object) -> dict:
    """Convert an object's attributes to a dict."""
    obj_dict = obj.__dict__

    if "__values__" in obj_dict:
        obj_dict = obj.__dict__.get("__values__")

    return {k: v for k, v in _unpack(obj_dict)}


def to_snake_case(value: str) -> str:
    """Convert camel case string to snake case."""
    words = re.findall(r"[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+", value)
    return "_".join(map(str.lower, words))


def keys_to_snake_case(content: dict) -> dict:
    """Convert all keys for given dict to snake case."""
    return {to_snake_case(key): value for key, value in _unpack(content)}


def to_modified_camel(value: str) -> str:
    """Convert the given string to an underscore camel case."""
    content = value.split("_")
    return "_" + to_camel_case(value)


def to_camel_case(value: str) -> str:
    """Convert the given string to camel case."""
    content = value.split("_")
    return content[0] + "".join(
        word.title() for word in content[1:] if not word.isspace()
    )


def keys_to_camel_case(data: dict) -> dict:
    """Convert all keys for given dict to camel case."""
    return {to_camel_case(key): value for key, value in _unpack(data)}


def keys_to_modified_camel(data: dict) -> dict:
    """Convert all keys for given dict to a modified camel case."""
    return {to_modified_camel(key): value for key, value in _unpack(data)}


def parse_keys(data: dict = None, parse_type: str = "modified_camel") -> dict:
    """Convert all keys for given dict/list to snake case recursively.

    :param data: The dict to parse

    :param parse_type: The type of parsing to carry out.
    The main types are `modified_camel`, `camel_case` and `snake_case`.
    """
    if parse_type not in ("modified_camel", "camel_case", "snake_case"):
        raise ValueError(
            "Invalid parse type, use modified_camel, camel_case or snake_case"
        )

    if not isinstance(data, dict):
        raise TypeError("Invalid data type, use dict.")

    formatters = [keys_to_modified_camel, keys_to_camel_case, keys_to_snake_case]

    formatter = None
    for f in formatters:
        if parse_type in f.__name__:
            formatter = f
    return formatter(data)


def pretty_attributes(
    all_attributes: dict, desired_attributes: Iterable[str], max_attributes: int = 3
) -> str:
    """Return a pretty string for the __repr__ body of an object."""
    pretty_str = ""
    found_attributes = 0
    for desired_attribute in desired_attributes:
        if found_attributes >= max_attributes:
            break

        attribute_value = all_attributes.get(desired_attribute, None)
        if attribute_value is not None:
            found_attributes += 1
            pretty_str += f"{desired_attribute}="

            if isinstance(attribute_value, int):
                pretty_str += f"{attribute_value}"
            else:
                pretty_str += f"'{attribute_value}'"

            if not found_attributes >= max_attributes:
                pretty_str += ", "

    # Necessary when the API doesn't return the max number of desired attributes.
    if pretty_str.endswith(", "):
        pretty_str = pretty_str[:-2]

    return pretty_str


def get_attributes(fields_to_iterate: list, attributes_to_fetch: list = None) -> list:
    """Iterate through list of dicts and return list of keys and values."""
    if attributes_to_fetch:
        attributes_to_fetch = [a.lower() for a in attributes_to_fetch]

    attrs = []
    for item in fields_to_iterate:
        label = item["fieldName"].lower()
        try:
            value = item["fieldValue"]["value"]
        except TypeError:
            value = None

        if attributes_to_fetch and label in attributes_to_fetch:
            if isinstance(value, list) and len(value) == 1:
                value = value[0]
            key = to_snake_case(label)
            attrs.append((key, value))

    return attrs


def set_default_attr(obj: object, attr_name_to_set: str, value, default_value=None):
    """Set a default attr if it doesn't already exist."""
    if not hasattr(obj, attr_name_to_set):
        setattr(obj, attr_name_to_set, value or default_value)
