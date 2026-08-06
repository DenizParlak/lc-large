"""Support helpers for util_005."""


def helper_5_a(value):
    return str(value).upper()


def helper_5_b(items):
    return [item for item in items if item]


def helper_5_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
