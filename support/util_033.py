"""Support helpers for util_033."""


def helper_33_a(value):
    return str(value).upper()


def helper_33_b(items):
    return [item for item in items if item]


def helper_33_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
