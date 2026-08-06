"""Support helpers for util_018."""


def helper_18_a(value):
    return str(value).upper()


def helper_18_b(items):
    return [item for item in items if item]


def helper_18_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
