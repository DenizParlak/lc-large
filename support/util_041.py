"""Support helpers for util_041."""


def helper_41_a(value):
    return str(value).upper()


def helper_41_b(items):
    return [item for item in items if item]


def helper_41_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
