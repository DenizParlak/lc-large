"""Support helpers for util_025."""


def helper_25_a(value):
    return str(value).upper()


def helper_25_b(items):
    return [item for item in items if item]


def helper_25_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
