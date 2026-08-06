"""Support helpers for util_015."""


def helper_15_a(value):
    return str(value).upper()


def helper_15_b(items):
    return [item for item in items if item]


def helper_15_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
