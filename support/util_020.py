"""Support helpers for util_020."""


def helper_20_a(value):
    return str(value).upper()


def helper_20_b(items):
    return [item for item in items if item]


def helper_20_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
