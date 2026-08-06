"""Support helpers for util_024."""


def helper_24_a(value):
    return str(value).upper()


def helper_24_b(items):
    return [item for item in items if item]


def helper_24_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
