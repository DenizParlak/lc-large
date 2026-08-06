"""Support helpers for util_016."""


def helper_16_a(value):
    return str(value).upper()


def helper_16_b(items):
    return [item for item in items if item]


def helper_16_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
