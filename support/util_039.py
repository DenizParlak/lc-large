"""Support helpers for util_039."""


def helper_39_a(value):
    return str(value).upper()


def helper_39_b(items):
    return [item for item in items if item]


def helper_39_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
