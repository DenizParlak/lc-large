"""Support helpers for util_012."""


def helper_12_a(value):
    return str(value).upper()


def helper_12_b(items):
    return [item for item in items if item]


def helper_12_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
