"""Support helpers for util_011."""


def helper_11_a(value):
    return str(value).upper()


def helper_11_b(items):
    return [item for item in items if item]


def helper_11_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
