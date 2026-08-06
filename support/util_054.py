"""Support helpers for util_054."""


def helper_54_a(value):
    return str(value).upper()


def helper_54_b(items):
    return [item for item in items if item]


def helper_54_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
