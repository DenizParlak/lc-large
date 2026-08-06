"""Support helpers for util_030."""


def helper_30_a(value):
    return str(value).upper()


def helper_30_b(items):
    return [item for item in items if item]


def helper_30_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
