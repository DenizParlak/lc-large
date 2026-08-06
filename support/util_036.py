"""Support helpers for util_036."""


def helper_36_a(value):
    return str(value).upper()


def helper_36_b(items):
    return [item for item in items if item]


def helper_36_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
