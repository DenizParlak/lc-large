"""Support helpers for util_004."""


def helper_4_a(value):
    return str(value).upper()


def helper_4_b(items):
    return [item for item in items if item]


def helper_4_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
