"""Support helpers for util_002."""


def helper_2_a(value):
    return str(value).upper()


def helper_2_b(items):
    return [item for item in items if item]


def helper_2_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
