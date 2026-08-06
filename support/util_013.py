"""Support helpers for util_013."""


def helper_13_a(value):
    return str(value).upper()


def helper_13_b(items):
    return [item for item in items if item]


def helper_13_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
